def a_numero(texto):
   
    try:
        numero = float(texto)
        return numero
    except:
        return None



def con_unidad(valor, unidad):
    if unidad not in ("Hz", "V", "s"):
        return None

    if valor >= 1.0E9:
        numero = round(valor / 1.0E9, 3)
        if unidad == "Hz":
            medicion = f"{numero:g} GHz"
            return medicion
        elif unidad == "V":
            medicion = f"{numero:g} GV"
            return medicion
        elif unidad == "s":
            medicion = f"{numero:g} Gs"
            return medicion
        else:
            return None

    elif valor >= 1.0E6:
        numero = round(valor / 1.0E6, 3)
        if numero == 1000:
            return f"1 G{unidad}"

        if unidad == "Hz":
            medicion = f"{numero:g} MHz"
            return medicion
        elif unidad == "V":
            medicion = f"{numero:g} MV"
            return medicion
        elif unidad == "s":
            medicion = f"{numero:g} Ms"
            return medicion
        else:
            return None

    elif valor >= 1.0E3:
        numero = round(valor / 1.0E3, 3)
        if numero == 1000:
            return f"1 M{unidad}"

        if unidad == "Hz":
            medicion = f"{numero:g} kHz"
            return medicion
        elif unidad == "V":
            medicion = f"{numero:g} kV"
            return medicion
        elif unidad == "s":
            medicion = f"{numero:g} ks"
            return medicion
        else:
            return None

    elif valor >= 1.0:
        numero = round(valor, 3)
        if numero == 1000:
            return f"1 k{unidad}"

        if unidad == "Hz":
            medicion = f"{numero:g} Hz"
            return medicion
        elif unidad == "V":
            medicion = f"{numero:g} V"
            return medicion
        elif unidad == "s":
            medicion = f"{numero:g} s"
            return medicion
        else:
            return None

    elif valor >= 1.0E-3:
        numero = round(valor * 1.0E3, 3)
        if numero == 1000:
            return f"1 {unidad}"

        if unidad == "Hz":
            medicion = f"{numero:g} mHz"
            return medicion
        elif unidad == "V":
            medicion = f"{numero:g} mV"
            return medicion
        elif unidad == "s":
            medicion = f"{numero:g} ms"
            return medicion
        else:
            return None

    elif valor >= 1.0E-6:
        numero = round(valor * 1.0E6, 3)
        if numero == 1000:
            return f"1 m{unidad}"

        if unidad == "Hz":
            medicion = f"{numero:g} uHz"
            return medicion
        elif unidad == "V":
            medicion = f"{numero:g} uV"
            return medicion
        elif unidad == "s":
            medicion = f"{numero:g} us"
            return medicion
        else:
            return None

    elif valor >= 1.0E-9:
        numero = round(valor * 1.0E9, 3)
        if numero == 1000:
            return f"1 u{unidad}"

        if unidad == "Hz":
            medicion = f"{numero:g} nHz"
            return medicion
        elif unidad == "V":
            medicion = f"{numero:g} nV"
            return medicion
        elif unidad == "s":
            medicion = f"{numero:g} ns"
            return medicion
        else:
            return None

    elif valor >= 1.0E-12:
        numero = round(valor * 1.0E12, 3)
        if numero == 1000:
            return f"1 n{unidad}"

        if unidad == "Hz":
            medicion = f"{numero:g} pHz"
            return medicion
        elif unidad == "V":
            medicion = f"{numero:g} pV"
            return medicion
        elif unidad == "s":
            medicion = f"{numero:g} ps"
            return medicion
        else:
            return None

    elif valor == 0:
        if unidad == "Hz":
            medicion = "0" + " Hz"
            return medicion
        elif unidad == "V":
            medicion = "0" + " V"
            return medicion
        elif unidad == "s":
            medicion = "0" + " s"
            return medicion
        else:
            return None




if __name__ == "__main__":

    texto ="1.000000E+03"
    texto2 = "Hola mamá"
    texto3 ="1.000000E+06"
    texto4 ="1.000000E+09"
    texto5 ="1.000000E+12"
    print(a_numero(texto))
    print(a_numero(texto2))

    #print(con_unidad(250000000000, "Hz"))
    #print(con_unidad(25000000, "s"))
    print(con_unidad(0.99999999, "Hz"))