"""Verifica la propagación conservadora con Th fijo; no altera las mediciones."""

import json
from pathlib import Path


def temperatura(m_a, m_h, t_a, capacidad):
    # c_a=1 cal/(g °C), L_f=80 cal/g, Th=0 °C fijo.
    return ((m_a + capacidad) * t_a - 80 * m_h) / (m_a + m_h + capacidad)


m_1, m_2, t_1, t_2, t = 87.6, 69.4, 24.0, 18.0, 22.0
capacidad = m_2 * (t - t_2) / (t_1 - t) - m_1
# Derivadas respecto a las cinco mediciones originales, sin calores intermedios.
gradiente_c = [
    -1,
    (t - t_2) / (t_1 - t),
    -m_2 * (t - t_2) / (t_1 - t) ** 2,
    -m_2 / (t_1 - t),
    m_2 * (t_1 - t_2) / (t_1 - t) ** 2,
]
delta_c = sum(abs(g) * u for g, u in zip(gradiente_c, [0.05, 0.05, 1, 1, 1]))

resultados = {
    "hipotesis": {"Th_C": 0, "delta_Th_C": 0, "c_cal_g_C": 1, "Lf_cal_g": 80},
    "calibracion": {"C_cal_C": capacidad, "delta_C_cal_C": delta_c},
    "hielo": {
        "Q_cal": 6.2 * (80 + 21),
        "delta_Q_cal": (80 + 21) * 0.10 + 6.2,
        "incertidumbre_relativa_porcentaje": 100 * 16.3 / 626.2,
    },
}

for nombre, cap, dcap in [("con_calorimetro", capacidad, delta_c), ("sin_calorimetro", 0, 0)]:
    entradas = [122.5, 6.2, 24.0, cap]
    teorica = temperatura(*entradas)
    denominador = entradas[0] + entradas[1] + cap
    gradiente = [
        (24 - teorica) / denominador,
        (-80 - teorica) / denominador,
        (122.5 + cap) / denominador,
        (24 - teorica) / denominador,
    ]
    # Contraste de las derivadas analíticas con diferencias centrales.
    for indice, analitica in enumerate(gradiente):
        paso = 1e-4
        mas, menos = entradas.copy(), entradas.copy()
        mas[indice] += paso
        menos[indice] -= paso
        numerica = (temperatura(*mas) - temperatura(*menos)) / (2 * paso)
        if abs(numerica - analitica) > 1e-7:
            raise ArithmeticError("Derivada inconsistente")
    contribuciones = [abs(g) * u for g, u in zip(gradiente, [0.05, 0.10, 1, dcap])]
    resultados[nombre] = {
        "T_C": teorica,
        "contribuciones_C": dict(zip(["ma", "mh", "Ta", "Ccal"], contribuciones)),
        "delta_T_C": sum(contribuciones),
    }

salida = Path(__file__).resolve().parents[1] / "data/incertidumbres_verificadas.json"
salida.write_text(json.dumps(resultados, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(resultados, indent=2, ensure_ascii=False))
