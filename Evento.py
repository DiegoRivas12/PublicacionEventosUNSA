
from abc import ABC, abstractmethod
class Evento(ABC):#Clase abstracta
    def __init__(self):
        self.id_evento = None
        self.Nombre = None
        self.Tipo = None
        self.Descripcion = None
        self.Puntuación = None
        self.Encargado = None
        self.Temas = None

    def Evento(self, ):
        pass
    @abstractmethod
    def mostrarFechas(self):
        print('Fechas:')
        

