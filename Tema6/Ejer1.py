class Vehiculo:
    color="azul"
    ruedas= 4
    puertas= 2

class Coche (Vehiculo):
    velocidad= 176
    cilindrada= 2200

c = Coche()

print("El color del coche es ",c.color, " y su cilindrada es ", c.cilindrada)

