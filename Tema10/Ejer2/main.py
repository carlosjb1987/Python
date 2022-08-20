import tkinter as tk

ventana1=tk.Tk()

def iniciar():
    print("Hola")

def medio():
    print("Vas por la mitad del programa")

def adios():
    print("Adiós")



boton1=tk.Button(ventana1, text="Inicio", command=iniciar)
boton1.grid(column=1, row=1)
boton2=tk.Button(ventana1, text="Medio", command=medio)
boton2.grid(column=2, row=1)
boton3=tk.Button(ventana1, text="Adios", command=adios)
boton3.grid(column=3, row=1)

label1=tk.Label(ventana1,text="Aquí tienes un label de letra blanca sobre fondo gris", fg="white", bg="grey",)
label1.grid(column = 2, row=3)


ventana1.mainloop()