from tkinter import *

ventana = Tk()
ventana.title("Colores by Josh!")

c = 0
f = 0

for r in range(1, 255, 35):
	for g in range(1, 255, 35):
		for b in range(1, 255, 35):
			nombre = ("R"+str(r)+" "+"G"+str(g)+" "+"B"+str(b))
			color = "#%02x%02x%02x" % (r, g, b)
			boton = Button(ventana, text=nombre, width=10, bg=color)
			boton.grid(column=c, row=f)
			f=f+1

			if f>26:
				f=0
				c=c+1

ventana.mainloop()