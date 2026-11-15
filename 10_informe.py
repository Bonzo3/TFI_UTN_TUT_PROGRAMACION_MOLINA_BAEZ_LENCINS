from importlib import import_module  # noqa: I001


con_unidad = import_module("02_magnitudes").con_unidad
resumen = import_module("09_estadistica").resumen


_UNIDADES = {
    "FREQ": "Hz",
    "PKPK": "V",
    "CYCRMS": "V",
}


def _valor_con_unidad(valor, unidad):
    if valor is None:
        return "no disponible"

    texto = con_unidad(valor, unidad)
    if texto is not None:
        return texto
    return f"{valor:g} {unidad}"


def armar_informe(idn, series, verificaciones):
    """Arma un informe de texto a partir de identificación, series y verificaciones."""
    lineas = ["Instrumento identificado:"]
    if idn:
        identificacion = " ".join(
            str(idn[campo])
            for campo in ("fabricante", "modelo", "serie", "version")
            if idn.get(campo)
        )
        lineas.append(f"  {identificacion}")
    else:
        lineas.append("  No disponible")

    lineas.append("Series de mediciones:")
    for equipo, canales in series.items():
        for canal, magnitudes in canales.items():
            for magnitud, valores in magnitudes.items():
                unidad = _UNIDADES.get(magnitud, "")
                estadisticas = resumen(valores)
                if estadisticas is None:
                    lineas.append(f"  {equipo} {canal} {magnitud}: n=0, sin datos")
                    continue

                lineas.append(
                    f"  {equipo} {canal} {magnitud}: "
                    f"n={estadisticas['n']}, "
                    f"promedio={_valor_con_unidad(estadisticas['promedio'], unidad)}, "
                    f"mínimo={_valor_con_unidad(estadisticas['minimo'], unidad)}, "
                    f"máximo={_valor_con_unidad(estadisticas['maximo'], unidad)}"
                )

    lineas.append("Verificaciones:")
    if isinstance(verificaciones, dict):
        verificaciones = [verificaciones]

    for verificacion in verificaciones:
        resultado = "coincide" if verificacion["coincide"] else "no coincide"
        canal = verificacion["canal"]
        medido = _valor_con_unidad(verificacion["cycrms_medido"], "V")
        teorico = _valor_con_unidad(verificacion["vrms_teorico"], "V")
        lineas.append(
            f"  {canal}: {resultado} (CYCRMS medido={medido}, Vrms teórico={teorico})"
        )

    return "\n".join(lineas)
