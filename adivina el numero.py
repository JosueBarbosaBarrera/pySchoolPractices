# import random
# secretNumber = random.randint(1,20)
print("The number is between 1 and 20: ")

for guessesTaken in range (1,7):
	print("Take a guess: ")
	guess = int(input())

	if guess < secretNumber:
		print("Your guess is too low")
	elif guess > secretNumber:
		print("Your guess is too high")
	else:
		break
		
if guess == secretNumber:
	print("good job, the number is: "+str(secretNumber)+" and you gyuesed in : "+str(guessesTaken)+ " Guesse!")
else:
	print("Nope, the number was"+str(secretNumber))
