from Vehiculos import Automovil


i=1
num=3


for i in range (0,num):
    print(" Datos del Automovil "+str(i+1))
    mar = input("Inserte la marca del 1° Automovil:")
    mod = input("Inserte el modelo :")
    ruedas = int(input("Inserte el numero de ruedas :"))
    vel = int(input("Inserte la velocidad en km/h: "))
    cili = int(input("Inserte el cilindraje en cc: "))
    
    if (i==0):
        vehiculo1=Automovil(mar,mod,ruedas,vel,cili)
    elif(i==1):
        vehiculo2=Automovil(mar,mod,ruedas,vel,cili)
    elif(i==2):
        vehiculo3=Automovil(mar,mod,ruedas,vel,cili)
    else:
        print("No se puede ingresar mas Vehiculos")
    


print(f'Datos del automovil 1 : Marca {vehiculo1.marca}, Modelo {vehiculo1.modelo}, {vehiculo1.num_ruedas} ruedas, {vehiculo1.velocidad} Km/h, {vehiculo1.cilindrada} cc')
print(f'Datos del automovil 1 : Marca {vehiculo2.marca}, Modelo {vehiculo2.modelo}, {vehiculo2.num_ruedas} ruedas, {vehiculo2.velocidad} Km/h, {vehiculo2.cilindrada} cc')
print(f'Datos del automovil 1 : Marca {vehiculo3.marca}, Modelo {vehiculo3.modelo}, {vehiculo3.num_ruedas} ruedas, {vehiculo3.velocidad} Km/h, {vehiculo3.cilindrada} cc')
