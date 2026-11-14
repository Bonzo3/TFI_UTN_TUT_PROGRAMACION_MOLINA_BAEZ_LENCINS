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
    instrumento1 = cliente.Instrumento()
    filas = barrido.barrer(instrumento1, ["CH1", "CH2"])

    print(verificar_canal(filas, "CH1"),sep='\n')
    print(verificar_canal(filas, "CH2"),sep='\n')