
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
            texto_crudo = instrumento.preguntar(comando)
    
            mediciones.append({
                "canal": canal,
                "magnitud": magnitud,
                "unidad": unidad,
                "texto_crudo": texto_crudo,
                "valor": a_numero(texto_crudo),
            })

    return mediciones



if __name__ == "__main__":

    # ---- pruebas sin conexión al servidor ----
    class InstrumentoFalso:
        def __init__(self):
            self.comandos = []

        def preguntar(self, comando):
            self.comandos.append(comando)
            respuestas = {
                ":MEASUrement:CH1:FREQuency?": "1.000000E+03",
                ":MEASUrement:CH1:PKPK?": "2.000000E+00",
                ":MEASUrement:CH1:CYCRms?": "7.071000E-01",
                ":MEASUrement:CH2:FREQuency?": "2.500000E+03",
                ":MEASUrement:CH2:PKPK?": "8.000000E-01",
                ":MEASUrement:CH2:CYCRms?": "ERROR: comando desconocido",
            }
            return respuestas[comando]

    instrumento_falso = InstrumentoFalso()
    filas_prueba = barrer(instrumento_falso, ["CH1", "CH2"])
    assert instrumento_falso.comandos == [
        ":MEASUrement:CH1:FREQuency?",
        ":MEASUrement:CH1:PKPK?",
        ":MEASUrement:CH1:CYCRms?",
        ":MEASUrement:CH2:FREQuency?",
        ":MEASUrement:CH2:PKPK?",
        ":MEASUrement:CH2:CYCRms?",
    ]
    assert filas_prueba == [
        {"canal": "CH1", "magnitud": "FREQuency", "unidad": "Hz",
         "texto_crudo": "1.000000E+03", "valor": 1000.0},
        {"canal": "CH1", "magnitud": "PKPK", "unidad": "V",
         "texto_crudo": "2.000000E+00", "valor": 2.0},
        {"canal": "CH1", "magnitud": "CYCRms", "unidad": "V",
         "texto_crudo": "7.071000E-01", "valor": 0.7071},
        {"canal": "CH2", "magnitud": "FREQuency", "unidad": "Hz",
         "texto_crudo": "2.500000E+03", "valor": 2500.0},
        {"canal": "CH2", "magnitud": "PKPK", "unidad": "V",
         "texto_crudo": "8.000000E-01", "valor": 0.8},
        {"canal": "CH2", "magnitud": "CYCRms", "unidad": "V",
         "texto_crudo": "ERROR: comando desconocido", "valor": None},
    ]
    instrumento_vacio = InstrumentoFalso()
    assert barrer(instrumento_vacio, []) == []
    assert instrumento_vacio.comandos == []
    print("pruebas sin conexión OK")

    # Permite ejecutar únicamente los assert sin abrir la conexión real.
    import sys
    if "--solo-pruebas" in sys.argv:
        sys.exit(0)

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
