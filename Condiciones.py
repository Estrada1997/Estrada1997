class Cifra:
    contador = 0 # variable de clase 
    #__init__ Método constructor que se ejecuta al momento de instanciar la clase que tiene.
    # Su objetivo es crear e inicializar los atributos de la clase.
    # Self es un objeto que representa a la clase que se crea.
    def __init__(self,val_1 = 2, val_2 = 6):
        self.valor1 = val_1  # variable de instancia
        self.valor2 = val_2
        # valores = val_1 + val_2
        self.valor3 = val_1
        #variables de instancias

    def usoIF(self):
        # if / elif / else : perimiten cumplir la ejecución de uno o varios bloques.
        if self.valor1 == self.valor2:
            print("Valores 1:{}, valores 2:{}: Los valores son iguales".format(self.valor1,self.valor2))
        elif self.cantidad1 == self.cantidad3:
             print("valor 1:{}, valor 3:{}: Lo valores son iguales".format(self.valor1,self.valor3))
        else:
            print("Los volores no son iguales")
# usar clase
# condición1 = Valor ()
# print(condición1.valor1)
# print(condición1.valor2)

cond2 = Cifra(20,20)
cond2.usoIF()
print(cond2.valor1)