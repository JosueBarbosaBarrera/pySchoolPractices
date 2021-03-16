#Robot

def born():
	global life
	life = 100
	print("Welcome to the world")
	print("Life = ", life)

def kill():
	global life
	if(life > 0):
		life = 0
	else:
		print("You can't kill yourself, because you are died")
	life = 0
	print("You are Died")
	print("Life = ", life)

def strike():
	global life
	if(life <= 0):
		life = 0
		print("is dead, don't punched more")
		print("'Santo llamando a Batman'")
	else:
		life = life - 10
		print("You were punched")
	print("Life = ", life)

def gainEnergy():
	global life
	if(life >= 100):
		life = 100
		print("You are Fully")
	else: 
		if(life == 0):
			print("You don't gain energy if you are dead")
		else:
			life = life + 20
			if(life > 100):
				life = 100
				print("you got the limit!")
			print("You gain energy")
	print("Your total Energy is = ", life)

def reborn():
	global life
	if(life == 0):
		life = 100
		print("You are alive again")
	else:
		print("You stay alive")
	print("Life = ", life)

def criticalDamage():
	global life
	if(life >= 50):
		life = life - 50
		print("Critical Damage Received")
	else:
		if(life == 0):
			print("You are Died, 'Santo llamando a Batman' ")
		else:
			life = 0
			print("Finish him")
			print("'Santo llamando a Batman'")
	print("Life = ", life)

def controllers():
	while(True):
		# print("1.- strike")
		# print("2.- gainEnergy")
		# print("3.- criticalDamage")
		# print("4.- kill")
		# print("5,- reborn")
		opc = int (input("action "))

		if(opc == 1):
			strike()
		elif(opc == 2):
			gainEnergy()
		elif(opc == 3):
			criticalDamage()
		elif(opc == 4):
			kill()
		elif(opc == 5):
			reborn()

def main():
 	born()
 	controllers()

main()