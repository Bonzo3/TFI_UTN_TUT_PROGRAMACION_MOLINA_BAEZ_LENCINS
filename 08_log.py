import math
from datetime import datetime
from pathlib import Path


_CANALES_VALIDOS = {"CH1", "CH2"}
_MAGNITUDES_VALIDAS = {"FREQ", "PKPK", "CYCRMS"}


def analizar_linea(linea):
    """Devuelve (medicion, motivo); ambas partes son None para líneas ignoradas."""
    texto = linea.strip()
    if not texto or texto.startswith("#"):
        return None, None

    campos = texto.split()
    if len(campos) != 6:
        return None, "la línea no tiene exactamente seis campos"

    fecha, hora, equipo, canal, magnitud, valor_texto = campos
    try:
        datetime.strptime(hora, "%H:%M:%S")
    except ValueError:
        return None, "la hora no es válida"

    if canal not in _CANALES_VALIDOS:
        return None, f"canal no válido: {canal}"

    if magnitud not in _MAGNITUDES_VALIDAS:
        return None, f"magnitud no válida: {magnitud}"

    try:
        valor = float(valor_texto)
    except (OverflowError, TypeError, ValueError):
        return None, f"el valor no se puede convertir a número: {valor_texto}"

    if not math.isfinite(valor):
        return None, f"el valor no es un número finito: {valor_texto}"

    medicion = {
        "fecha": fecha,
        "hora": hora,
        "equipo": equipo,
        "canal": canal,
        "magnitud": magnitud,
        "valor": valor,
    }
    return medicion, None


def leer_log(directorio):
    """Lee mediciones.log y devuelve (series, líneas_rechazadas)."""
    ruta = Path(directorio) / "mediciones.log"
    series = {}
    rechazadas = []

    with ruta.open(encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            medicion, motivo = analizar_linea(linea)
            if motivo is not None:
                rechazadas.append(
                    {
                        "numero_linea": numero_linea,
                        "linea": linea.rstrip("\r\n"),
                        "motivo": motivo,
                    }
                )
                continue

            if medicion is None:
                continue

            equipo = medicion["equipo"]
            canal = medicion["canal"]
            magnitud = medicion["magnitud"]
            series.setdefault(equipo, {}).setdefault(canal, {}).setdefault(
                magnitud, []
            ).append(medicion["valor"])

    return series, rechazadas


if __name__ == "__main__":
    series, rechazadas = leer_log(Path(__file__).parent)

    print("Series de mediciones:")
    for equipo, canales in series.items():
        print(f"Equipo: {equipo}")
        for canal, magnitudes in canales.items():
            for magnitud, valores in magnitudes.items():
                print(f"  {canal} {magnitud}: {valores}")

    print("\nLíneas rechazadas:")
    for rechazo in rechazadas:
        print(
            f"  Línea {rechazo['numero_linea']}: "
            f"{rechazo['linea']} — {rechazo['motivo']}"
        )
