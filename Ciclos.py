class Elemento:
    def __init__(self, valor = 24):
        self.valor = valor

    def usoWhile (self):
        # ciclo repetitivo que se ejecuta mediante verdadero
        # y su salida es por falso
        dato = input("Ingrese una vocal:")
        dato = dato.lower()
        while dato not in ("a","e","i","o","u"):
            dato = input("Ingrese una vocal:").lower()
        print("Muy bien el elemento : {} es una vocal".format(dato))
ciclo = Elemento()
ciclo.usoWhile()