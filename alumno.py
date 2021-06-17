from .persona import persona
from .docente import docente

class Alumno(persona, docente):

    def __init(self):
        self.nombre= "Anderson"
        super().__init__(1, self.nombre, 24)

    def saludar(self):
        print("Hola mi nombre es "+ self.nombre)

    def mostrar_edad(self, edad):
        print("Edad: "+ edad)