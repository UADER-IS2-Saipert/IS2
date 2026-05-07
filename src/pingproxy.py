#============================
#Ping
#============================

class Ping:

    def execute(self, ip):

        # Solo permite IPs que comiencen con 192.
        if ip.startswith("192."):

            for i in range(10):
                print(f"Ping {i+1} a {ip}")

        else:
            print("ERROR: Dirección IP no permitida")


    def executefree(self, ip):

        # Sin control de IP
        for i in range(10):
            print(f"Ping libre {i+1} a {ip}")

#============================
#Proxy
#============================

class PingProxy:

    def __init__(self):
        self.ping = Ping()


    def execute(self, ip):

        # Caso especial
        if ip == "192.168.0.254":

            print("Acceso especial detectado")
            self.ping.executefree("www.google.com")

        # Reenvía al execute original
        else:
            self.ping.execute(ip)

#=============================
#Prueba
#=============================

proxy = PingProxy()

print("----- Caso válido -----")
proxy.execute("192.168.1.1")

print("\n----- Caso inválido -----")
proxy.execute("10.0.0.1")

print("\n----- Caso especial -----")
proxy.execute("192.168.0.254")