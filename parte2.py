from Vehiculos import Vehiculo
from Vehiculos import Automovil
from Vehiculos import Particular
from Vehiculos import Carga
from Vehiculos import Bicicleta
from Vehiculos import Motocicleta




particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print(f' Marca {particular.marca}, Modelo {particular.modelo}, {particular.num_ruedas} ruedas, {particular.velocidad} Km/h, {particular.cilindrada} cc puestos {particular.num_puestos}')
print(f' Marca {carga.marca}, Modelo {carga.modelo}, {carga.num_ruedas} ruedas, {carga.velocidad} Km/h, {carga.cilindrada} cc puestos {carga.peso_carga}')
print(f' Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.num_ruedas} ruedas Tipo {bicicleta.tipo} ')
print(f' Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.num_ruedas} ruedas Tipo {motocicleta.tipo} Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, N° de Radios: {motocicleta.nro_radios}')



# Verificar las relaciones
print("Verificación de relaciones:")
print(f"¿Es motocicleta1 un Vehículo? {isinstance(motocicleta, Vehiculo)}")
print(f"¿Es motocicleta1 un Automóvil? {isinstance(motocicleta, Automovil)}")
print(f"¿Es motocicleta1 un Automóvil Particular? {isinstance(motocicleta, Particular)}")
print(f"¿Es motocicleta1 un Automóvil de Carga? {isinstance(motocicleta, Carga)}")
print(f"¿Es motocicleta1 una Bicicleta? {isinstance(motocicleta, Bicicleta)}")
print(f"¿Es motocicleta1 una Motocicleta? {isinstance(motocicleta, Motocicleta)}")