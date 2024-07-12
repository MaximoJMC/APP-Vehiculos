class Alquiler:
    def __init__(self, codigoCliente, fechaAlquiler, dias, vehiculo, cliente):
        self.codigo = codigoCliente
        self.fecha = fechaAlquiler
        self.dias = dias
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.total = 0.0
        self.estado = 0  # inicializa con estado pendiente : 0 / devuelto : 1

    def calcular_total(self, precio_por_dia):
        self.total = self.dias * precio_por_dia

    #getter y setter
    def obtener_estado(self):
        return self.estado

    def modificar_estado(self, estado):
        self.estado = estado