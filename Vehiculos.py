

class Vehiculo:
    def __init__(self, marca: str, modelo: str, num_ruedas: int):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas
    
    
class Automovil(Vehiculo):
    def __init__(self, marca:str, modelo:str, num_ruedas:int, velocidad:int, cilindrada:int):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    
    def __str__(self):
        return print(f'{self.marca}, Modelo: {self.modelo}, Velocidad: {self.velocidad} Km')


#*******************************Parte 2 **************


class Particular(Automovil):
    def __init__(self, marca: str, modelo: str, num_ruedas: int, velocidad: float, cilindrada: float, num_puestos: int):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puestos = num_puestos

    def __str__(self):
        return (f"Automóvil Particular(marca={self.marca}, modelo={self.modelo}, "
                f"num_ruedas={self.num_ruedas}, velocidad={self.velocidad}, "
                f"cilindrada={self.cilindrada}, num_puestos={self.num_puestos})")


class Carga(Automovil):
    def __init__(self, marca: str, modelo: str, num_ruedas: int, velocidad: float, cilindrada: float, peso_carga: float):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return (f"Automóvil de Carga(marca={self.marca}, modelo={self.modelo}, "
                f"num_ruedas={self.num_ruedas}, velocidad={self.velocidad}, "
                f"cilindrada={self.cilindrada}, peso_carga={self.peso_carga})")


class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, num_ruedas: int, tipo: str):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Bicicleta(marca={self.marca}, modelo={self.modelo}, num_ruedas={self.num_ruedas}, tipo={self.tipo})"


class Motocicleta(Bicicleta):
    def __init__(self, marca: str, modelo: str, num_ruedas: int, tipo: str, nro_radios: int, cuadro: str, motor: str):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return (f"Motocicleta(marca={self.marca}, modelo={self.modelo}, "
                f"num_ruedas={self.num_ruedas}, tipo={self.tipo}, "
                f"nro_radios={self.nro_radios}, cuadro={self.cuadro}, motor={self.motor})")



#vehiculo2 = Automovil("Honda", "Civic", 4)


# Imprimir atributos para verificar

#print(vehiculo2.marca)

