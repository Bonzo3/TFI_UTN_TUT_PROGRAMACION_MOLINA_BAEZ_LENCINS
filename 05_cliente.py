import socket
from importlib import import_module

parsear_idn = import_module("01_identificacion").parsear_idn



class Instrumento:

    def __init__(self, ip="127.0.0.1", puerto=5555):
        self.cliente = socket.create_connection((ip, puerto))
        self.pendiente = b""

    def enviar(self, comando):
        self.cliente.sendall((comando + "\n").encode("utf-8"))

    def preguntar(self, comando):
        self.enviar(comando)
        while b"\n" not in self.pendiente:
            fragmento = self.cliente.recv(1024)
            if not fragmento:
                raise ConnectionError("El instrumento cerró la conexión antes de completar la respuesta")
            self.pendiente += fragmento

        respuesta, self.pendiente = self.pendiente.split(b"\n", 1)
        return respuesta.decode("utf-8").rstrip("\r")

    def cerrar(self):
        self.cliente.close()

if __name__ == "__main__":
    instrumento1 = Instrumento()

    # ---- pruebas: requieren el instrumento virtual encendido ----
    try:
        respuesta = instrumento1.preguntar("*IDN?")
        assert respuesta == "OWON,ADS3202,25470803,V1.2.0"
        assert parsear_idn(respuesta)["modelo"] == "ADS3202"
        assert instrumento1.preguntar(":COMANDO_INEXISTENTE?").startswith("ERROR:")
        print("pruebas OK")
    finally:
        instrumento1.cerrar()
