def parsear_idn(respuesta):

    equipos = {}
    
    #for fabricante, modelo, serie, version, *descarte in respuesta:
    lista=respuesta.split(",")

    if len(lista) < 4:
        return None
    
    fabricante, modelo, serie, version, *descarte = lista

    equipos = {"fabricante": fabricante.strip(),
                "modelo" : modelo.strip(),
                "serie" : serie.strip(),
                "version" : version.strip(),
               }

    return equipos


if __name__ =="__main__":
    IDN = "OWON,XDM1041,25470803,V4.4.0,3"
    IDN1 = ""
    IDN2 = "ERROR: comando desconocido"
    IDN3 = " OWON , ADS3202 , 25470803 , V1.2.0 "
    IDN4 = "OWON,ADS3202,25470803"
    print("Resultado", parsear_idn(IDN))
    print("Resultado", parsear_idn(IDN1))
    print("Resultado", parsear_idn(IDN2))
    print("Resultado", parsear_idn(IDN3))
    print("Resultado", parsear_idn(IDN4))