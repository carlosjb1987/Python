import pickle

class Coche:
    marca=""
    puertas=4

    def __init__(self, marca, puertas):
        self.marca=marca
        self.puertas=puertas
    
    def getMarca(self):
        return self.marca

c1= Coche("Peugeot", 5)

f=open("datos.bin", "wb")
pickle.dump(c1, f)
f.close()

e=open('datos.bin', 'rb' )
cargaContenido=pickle.load(e)
e.close()

print(cargaContenido.getMarca())
