

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        if self.nota >4:
            print ("Su nombre es ", self.nombre, " y su nota es ", self.nota, "por lo que ha aprobado") 
        else:
            print ("Su nombre es ", self.nombre, " y su nota es ", self.nota, "por lo que ha suspendido") 

uno= Alumno("Carlos", 3)
uno.imprimir()
