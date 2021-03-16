import time
import numpy as np
import sys

def imprimir_con_retraso(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
# crear la clase
class Pokemon:
	def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud="==================="):
		#guardar variables como atributos
		self.nombre = nombre
		self.tipos = tipos
		self.movimientos = movimientos
		self.ataque = EVs["ataque"]
		self.defensa = EVs["defensa"]
		self.puntos_de_salud = puntos_de_salud
		self.barras = 20 # Amount puntos_de_salud barras

	def impresa(self, Pokemon2):
		""" imprimir info de lucha"""
		print("----BATALLA DE POKEMON-----")
		print(f"\n{self.nombre}")
		print("tipo/", self.tipos)
		print("ataque/", self.ataque)
		print("defensa/", self.defensa)
		print("Nv./", 3*(1+np.mean([self.ataque, self.defensa])))
		print("\nVS")
		print(f"\n{Pokemon2.nombre}")
		print("tipo/", Pokemon2.tipos)
		print("ataque/", Pokemon2.ataque)
		print("defensa/", Pokemon2.defensa)
		print("Nv./", 3*(1+np.mean([Pokemon2.ataque, Pokemon2.defensa])))
		time.sleep(2)

	def ventaja(self, Pokemon2):
		""" Actualiza poderes de taque y defensa devuelve dos cadena de info """
		version = ["fuego","agua","planta"]
		for i,k in enumerate(version):
			
			if self.tipos == k:
				
				if Pokemon2.tipos == k:
				# Son de lmismo tipo
					cadena_1_ataque = "\nNo es muy efectivo"
					cadena_2_ataque = "\nNo es muy efectivo"

				"""POKEMON es FUERTE"""
				if Pokemon2.tipos == version[(i+1)%3]:
					Pokemon2.ataque *= 2
					Pokemon2.defensa *= 2
					self.ataque /= 2
					self.defensa /=2
					cadena_1_ataque = "\nNo es muy efectivo"
					cadena_2_ataque = "\nEs muy eficaz"

				"""POKEMON es DEBIL"""
				if Pokemon2.tipos == version[(1+2)%3]:
					self.ataque *= 2
					self.defensa *=2
					Pokemon2.ataque /= 2
					Pokemon2.defensa /= 2
					cadena_1_ataque = "\nEs muy eficaz"
					cadena_2_ataque = "\nNo es muy eficiente"
			return cadena_1_ataque, cadena_2_ataque

	def turno(self, Pokemon2, cadena_1_ataque, cadena_2_ataque):
		"""Empieza pokemon 1, elije ataque y calcular	
		los nuevos puntos de salud.
		Has lo mismo con pokemon 2, Siga hasta que los puntos de salud de
		uno """

		while(self.barras > 0) and (Pokemon2.barras > 0):
			#imprime los puntos_de_salud de cada pokemon
			print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
			print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")

			# POKEMON 1
			
			print(f"Adelante {self.nombre}!")
			for i , x in enumerate(self.movimientos):
				print(f"{i+1}.", x)
			index = int(input("Elige un movimiento: "))
			imprimir_con_retraso(f"\n{self.nombre} uso {self.movimientos[index-1]}!")
			time.sleep(1)
			imprimir_con_retraso(cadena_1_ataque)

			# Determinar el dano
			Pokemon2.barras -= self.ataque
			Pokemon2.puntos_de_salud = ""

			for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
				Pokemon2.puntos_de_salud += "="

			time.sleep(1)
			print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
			print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
			time.sleep(.5)

			# verificar si Pokemon se debilito

			if Pokemon2.barras <= 0:
				imprimir_con_retraso("\n..." + Pokemon2.nombre + " se debilito.")
				break


			# POKEMONS 2
			print(f"Adelante {Pokemon2.nombre}!")
			for i , x in enumerate(Pokemon2.movimientos):
				print(f"{i+1}.", x)
			index = int(input("Elige un movimiento: "))
			imprimir_con_retraso(f"\n{Pokemon2.nombre} uso {Pokemon2.movimientos[index-1]}!")
			time.sleep(1)
			imprimir_con_retraso(cadena_2_ataque)

			#determinar el dano
			self.barras -= Pokemon2.ataque
			self.puntos_de_salud = ""

			#agregar barras adicionales mas defensa boost
			for j in range(int(self.barras+.1*self.defensa)):
				self.puntos_de_salud += "="

			time.sleep(1)
			print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
			print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
			time.sleep(.5)

			# verificar si Pokemon2 se debilito

			if self.barras <= 0:
				imprimir_con_retraso("\n..." + self.nombre + " se debilito.")
				break

	def lucha(self, Pokemon2):
		# imprime informacion de lucha
		self.impresa(Pokemon2)
		# considera la ventaja del tipo
		cadena_1_ataque, cadena_2_ataque = self.ventaja(Pokemon2)
		# la lucha continua mienras aun quengasn puntos de salud
		self.turno(Pokemon2, cadena_1_ataque, cadena_2_ataque)

		#recibe sinero (premio)
		money = np.random.choice(5000)
		imprimir_con_retraso(f"\nEl oponente te pago ${money}.\n")



if __name__ == '__main__':
	# crear pokemon objeto
	Charizard = Pokemon("Charizard", "fuego", ["Lanzallamas","Pirotecnia","Giro Fuego","Ascuas"], {"ataque":12, "defensa":8})
	Blastoise = Pokemon("Blastoise", "agua", ["Pistola Agua","Burbuja","Hidropulso","Hidrobomba"], {"ataque":10, "defensa":10})
	Venusaur = Pokemon("Venusaur", "planta", ["Latigo Cepa","Hoja Afilada","Rayo Solar","Abatidoras"], {"ataque":8, "defensa":12})
	Charizard.lucha(Blastoise)