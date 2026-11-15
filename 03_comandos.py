def es_consulta(comando):

    indice= len(comando)
    if(comando[indice -1] == '?'):
        return True
    else:
        return False

def validar(comando):
    
       
    if not comando:
        return comando + "La consulta no puede estar vacia."
        
    if(comando[0] != ":" and comando[0] != "*"):
            print(comando[0])
            return comando + "\t\tLas consultas deben comenzar con : o *"

    if "  " in comando:
        return comando + "\t\tNo puede haber dos espacios vacios seguidos."

    if comando.count("?") > 1:
        return comando + "\t\tNo puede haber más de un signo de pregunta."

    consulta = es_consulta(comando)
    if "?" in comando and not consulta:
        return comando + "\t\tEl signo ? debe ir al final."

    partes = comando.split()
    cantidad_argumentos = len(partes) - 1

    if consulta:
        if cantidad_argumentos != 0:
            return "Una consulta no lleva argumentos"
        
    elif cantidad_argumentos != 1:
        return "Una orden debe llevar un solo argumento"

    

if __name__ =="__main__":
    comando = "CH1:DISPlay ON?"

    print(es_consulta(":CH1:DISPlay ON?"))  # True
    print(validar(":CH1:DISPlay ON?"))      # Una consulta no lleva argumentos
    print(validar(":CH1:DISPlay ON"))
