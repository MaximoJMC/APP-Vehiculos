class Oferta:
    def __init__(self, id, placa, precio_por_dia, descripcion, fecha_salida):
        self.id = id
        self.placa = placa
        self.precio_por_dia = precio_por_dia
        self.descripcion = descripcion
        self.fecha_salida = fecha_salida
 
        self.estado = 0  # inicializa con "disponible :0" , no disponible : 1
    #getter y setter
    def obtener_estado(self):
        return self.estado
    
    def modificar_estado(self, estado):
        self.estado = estado