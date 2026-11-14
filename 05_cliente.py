import socket
from importlib import import_module

parsear_idn = import_module("01_identificacion").parsear_idn



class Instrumento():

    #ip = "127.0.0.1"
    #puerto = "5555"

    def enviar(sefl,ip, puerto, orden):
        orden = orden +"\n"
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((ip, puerto))
        cliente.sendall(orden.encode("utf-8"))
        cliente.close()        

    def preguntar(sefl,ip, puerto, orden):
        orden = orden +"\n"
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((ip, puerto))
        cliente.sendall(orden.encode("utf-8"))
        respuesta = cliente.recv(1024).decode("utf-8")
        #print(f"Servidor responde: {respuesta}")
        cliente.close()
        return respuesta

    def cerrar_conexion(self):
        cliente.close()

if __name__ == "__main__":
    instrumento1 = Instrumento()

    instrumento1.preguntar("127.0.0.1", 5555, "*IDN?")
