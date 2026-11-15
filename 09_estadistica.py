import math
from importlib import import_module
from pathlib import Path


def resumen(valores):
    if not valores:
        return None

    n = len(valores)
    promedio = sum(valores) / n
    desvio = (
        0.0
        if n == 1
        else math.sqrt(sum((valor - promedio) ** 2 for valor in valores) / (n - 1))
    )
    return {
        "n": n,
        "minimo": min(valores),
        "maximo": max(valores),
        "promedio": promedio,
        "desvio": desvio,
    }


def fuera_de_rango(valores, minimo, maximo):
    return [
        posicion
        for posicion, valor in enumerate(valores)
        if valor < minimo or valor > maximo
    ]


if __name__ == "__main__":
    leer_log = import_module("08_log").leer_log
    series, rechazadas = leer_log(Path(__file__).parent)
    frecuencias_ch1 = series["ADS3202"]["CH1"]["FREQ"]
    estadisticas = resumen(frecuencias_ch1)

    print("Resumen de frecuencias de CH1:", estadisticas)
    print("Líneas rechazadas:", len(rechazadas))

    assert abs(estadisticas["promedio"] - 1000) / 1000 < 0.005
    assert estadisticas["desvio"] < 5
