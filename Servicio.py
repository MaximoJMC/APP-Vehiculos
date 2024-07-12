class Servicio:
    def __init__(self, id, id_conductor, precio_por_hora, horas_servicio, codigo_cliente, placa):
        self.id = id
        self.id_conductor = id_conductor
        self.precio_por_hora = precio_por_hora
        self.horas_servicio = horas_servicio
        self.codigo_cliente = codigo_cliente
        self.placa = placa
        self.total = 0.0

    def calcular_total(self):
        self.total = self.horas_servicio * self.precio_por_hora