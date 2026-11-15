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


if __name__ == "__main__":
    # ---- pruebas ----
    comandos_ch1 = comandos_de_canal("CH1", "ON", "DC", "10X", "1v")
    assert comandos_ch1 == [
        ":CH1:DISPlay ON",
        ":CH1:COUPling DC",
        ":CH1:PROBe 10X",
        ":CH1:SCALe 1v",
    ]
    assert all(validar(comando) is None for comando in comandos_ch1)

    comandos_ch2 = comandos_de_canal("CH2", "OFF", "AC", "1X", "2v")
    assert comandos_ch2 == [
        ":CH2:DISPlay OFF",
        ":CH2:COUPling AC",
        ":CH2:PROBe 1X",
        ":CH2:SCALe 2v",
    ]
    assert all(validar(comando) is None for comando in comandos_ch2)
    assert comandos_de_canal("CH3", "ON", "DC", "10X", "1v") is None

    print("pruebas OK")
