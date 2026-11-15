from math import isfinite, sqrt
import importlib

barrido = importlib.import_module("06_barrido")
cliente = importlib.import_module("05_cliente")
def vrms_teorico(vpp):

    if not isinstance(vpp, (int, float)) or not isfinite(vpp) or vpp < 0:
        return None

    else:
        return vpp/(2 * sqrt(2))



def coincide(medido, teorico, tolerancia=0.02):
    if medido is None or teorico is None or teorico == 0:
        return False

    error = abs(medido - teorico) / abs(teorico)
    return error <= tolerancia




def verificar_canal(filas, canal):

    for fila in filas:
        if fila["canal"] == canal:
            if fila["magnitud"] == "PKPK":
                vpp = fila["valor"]
            elif fila["magnitud"] == "CYCRms":
                vrms_medido = fila["valor"]

    teorico = vrms_teorico(vpp)
    
    return {
        "canal": canal,
        "vpp": vpp,
        "vrms_medido": vrms_medido,
        "vrms_teorico": teorico,
        "coincide": coincide(vrms_medido, teorico),
    }  

if __name__ == "__main__":
    #instrumento1 = cliente.Instrumento()
    #filas = barrido.barrer(instrumento1, ["CH1", "CH2"])
    filas_prueba = [
    {"canal": "CH1", "magnitud": "PKPK", "valor": 2.0},
    {"canal": "CH1", "magnitud": "CYCRms", "valor": 1.0},
]
    # ---- pruebas sin conexión al servidor ----
    assert abs(vrms_teorico(2.0) - 0.7071067811865475) < 1e-12
    assert coincide(0.71, vrms_teorico(2.0)) is True
    assert verificar_canal(filas_prueba, "CH1")["coincide"] is False
    print("pruebas OK")
