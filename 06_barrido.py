
import importlib

cliente = importlib.import_module("05_cliente")
a_numero = importlib.import_module("02_magnitudes").a_numero
con_unidad = importlib.import_module("02_magnitudes").con_unidad

def barrer(instrumento, canales):
    mediciones = []
    magnitudes = [
        ("FREQuency", "Hz"),
        ("PKPK", "V"),
        ("CYCRms", "V"),
    ]

    for canal in canales:
        for magnitud, unidad in magnitudes:
            comando = f":MEASUrement:{canal}:{magnitud}?"
            texto_crudo = instrumento.preguntar("127.0.0.1",5555, comando)
    
            mediciones.append({
                "canal": canal,
                "magnitud": magnitud,
                "unidad": unidad,
                "texto_crudo": texto_crudo,
                "valor": a_numero(texto_crudo),
            })

    return mediciones



if __name__ == "__main__":

    instrumento = cliente.Instrumento()
    mediciones = barrer(instrumento, ["CH1", "CH2"])
    print(*mediciones, sep='\n')
    #print(a_numero(mediciones[texto_crudo]))

    for medicion in mediciones:
        valor = medicion["valor"]

        if valor is None:
            lectura = repr(medicion["texto_crudo"])
        else:
            lectura =  con_unidad(valor, medicion["unidad"])

        print(medicion["canal"], medicion["magnitud"], lectura)