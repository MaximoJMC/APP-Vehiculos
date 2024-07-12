
#importamos cada modulo
from Vehiculo import Vehiculo
from Cliente import Cliente
from Conductor import Conductor
from Alquiler import Alquiler
from Servicio import Servicio
from Oferta import Oferta


# Crear una instancia de la clase vehículo
vehiculo1 = Vehiculo("ABC123", "Toyota", "Rojo","2020")
# Crear una instancia de la clase cliente
cliente1 = Cliente(1, "Juancito", "Perez", "987654321", "12345678")
# Crear una instancia de la clase conductor
conductor1 = Conductor(1, "12345", "Carlitos", "Gonzales","A1")
# Crear una instancia de la clase  oferta
oferta1 = Oferta(1, "ABC123", 100.0, "Toyota Rojo 2020", "01/01/2024")
# Crear una instancia de la clase alquiler
alquiler1 = Alquiler(1, "01/01/2024", 5, vehiculo1, cliente1)
alquiler1.calcular_total(oferta1.precio_por_dia)
alquiler1.modificar_estado(1)
# Crear una instancia de la clase  servicio
servicio1 = Servicio(1001, 1, 50.0, 10, 1, "ABC123")
servicio1.calcular_total()

# Ver resultados
print(f"Vehículo : {vehiculo1.placa}/ Modelo : {vehiculo1.modelo} / Estado: {vehiculo1.obtener_estado()}")
print(f"Alquiler : {alquiler1.codigo} / Total a pagar: {alquiler1.total}")
print(f"Servicio : {servicio1.id} / Nombre del chofer : {conductor1.nombre} / Total a pagar: {servicio1.total}")
