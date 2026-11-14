from importlib import import_module

validar = import_module("03_comandos").validar

def comandos_de_canal(canal, display, acoplamiento, sonda, escala):

    if canal != "CH1" and canal != "CH2":
        return None

    lista_comandos = []
    lista_comandos.append(f":{canal}:DISPlay {display}")
    lista_comandos.append(f":{canal}:COUPling {acoplamiento}")
    lista_comandos.append(f":{canal}:PROBe {sonda}")
    lista_comandos.append(f":{canal}:SCALe {escala}")

    
    for i in lista_comandos:
        print(validar(i))
       

    return lista_comandos


print(comandos_de_canal("CH1", "ON", "  DC", "  10X", "1v"))