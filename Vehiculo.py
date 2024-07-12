class Vehiculo:
    def __init__(self, placa, modelo, color,año):
        self.placa = placa
        self.modelo = modelo
        self.color = color
        self.año = año
        self.estado = 0  # inicializar con libre : 0 , ocupado:1

    #getter y setter
    def obtener_estado(self):
        return self.estado
    
    def modificar_estado(self, estado):
        self.estado = estado