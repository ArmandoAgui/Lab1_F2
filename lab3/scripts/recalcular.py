"""Recalcula OLS no ponderado y genera datos PGFPlots. Sin dependencias externas.
Datos transcritos de las tablas originales de 04_analisis.tex; no son nuevas mediciones.
Los errores estándar son condicionales: no incluyen errores en x ni sesgos instrumentales.
"""
import csv
import json
import math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def cargar(nombre):
    with (ROOT / 'data' / nombre).open() as archivo:
        return [{k: float(v) for k, v in row.items()} for row in csv.DictReader(archivo)]
def ols(x, y, origen=False):
    N = len(x)
    xb, yb = sum(x)/N, sum(y)/N
    Sxx = sum((a-xb)**2 for a in x)
    m = (sum(a*b for a,b in zip(x,y))/sum(a*a for a in x) if origen
         else sum((a-xb)*(b-yb) for a,b in zip(x,y))/Sxx)
    b = 0.0 if origen else yb-m*xb
    residual = [v-m*u-b for u,v in zip(x,y)]
    SSE = sum(r*r for r in residual)
    s2 = SSE/(N-(1 if origen else 2))
    return {'m': m, 'b': b, 'se_m': math.sqrt(s2/(sum(a*a for a in x) if origen else Sxx)),
            'se_b': None if origen else math.sqrt(s2*(1/N+xb*xb/Sxx)),
            'R2_centrado': 1-SSE/sum((v-yb)**2 for v in y),
            'SSE': SSE, 'residuos_Hz': residual, 'N': N}
h = cargar('armonicos.csv'); agua = cargar('agua.csv')
L, D, T = 0.360, 0.050, 25.0
Lf = L+0.3*D; A = math.pi*D*D/4; vT = 331.25+0.585*T
ah = ols([r['n'] for r in h], [r['f_Hz'] for r in h])
for r in agua:
    r['L_m'] = Lf-r['V_cm3']*1e-6/A
    r['invL_m1'] = 1/r['L_m']
x = [r['invL_m1'] for r in agua]; y = [r['f_Hz'] for r in agua]
aw = ols(x,y); az = ols(x,y,True)
for fit, escala in [(ah,4*Lf),(aw,4),(az,4)]:
    fit['v_m_s'] = escala*fit['m']
    fit['se_v_solo_ajuste_m_s'] = escala*fit['se_m']
    fit['discrepancia_porcentual'] = abs(fit['v_m_s']-vT)/vT*100
res = {'geometria': {'L_m':L,'D_m':D,'Lf_m':Lf,'A_m2':A,'T_C':T,'vT_m_s':vT},
       'armonicos': ah, 'agua_intercepto_libre': aw, 'agua_origen':az,
       'diapasones': [{'f_Hz':f,'V_teorico_cm3':A*(Lf-vT/(4*f))*1e6} for f in [256,320,384,480]]}
(ROOT/'data'/'resultados_ajustes.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
(ROOT/'data'/'armonicos_plot.dat').write_text('n f\n'+''.join(f"{r['n']:.0f} {r['f_Hz']:.2f}\n" for r in h))
(ROOT/'data'/'agua_plot.dat').write_text('Lcm invL f\n'+''.join(f"{r['L_m']*100:.10f} {r['invL_m1']:.10f} {r['f_Hz']:.2f}\n" for r in agua))
(ROOT/'data'/'parametros.tex').write_text(
    '% Generado por scripts/recalcular.py; mantener precisión interna.\n'+
    f"\\def\\PendienteArmonicos{{{ah['m']:.10f}}}\n\\def\\InterceptoArmonicos{{{ah['b']:.10f}}}\n"+
    f"\\def\\PendienteAgua{{{aw['m']:.10f}}}\n\\def\\InterceptoAgua{{{aw['b']:.10f}}}\n"+
    f"\\def\\PendienteOrigen{{{az['m']:.10f}}}\n")
print(json.dumps(res,indent=2,ensure_ascii=False))
