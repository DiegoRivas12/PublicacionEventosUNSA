from Evento import Evento

class Simposio(Evento):
    def __init__(self):
        self.Fecha = None
        self.Hora = None

    
    def mostrarFechas(self):
        super().mostrarFechas()
        print(self.Fecha)
        print(self.Hora)
        
g = Simposio()
g.mostrarFechas()
