import tkinter as tk

def iniciar():
    return seleccion.set(0)

ventana1=tk.Tk()
seleccion=tk.IntVar()
seleccion.set(0)
radio1=tk.Radiobutton(ventana1,text="Opción 1", variable=seleccion, value=1)
radio1.grid(column=0, row=0)
radio2=tk.Radiobutton(ventana1,text="Opción 2", variable=seleccion, value=2)
radio2.grid(column=0, row=1)
radio3=tk.Radiobutton(ventana1,text="Opción 3", variable=seleccion, value=3)
radio3.grid(column=0, row=2)


boton1=tk.Button(ventana1, text="Reiniciar", command=iniciar)
boton1.grid(column=0, row=3)



ventana1.mainloop()
