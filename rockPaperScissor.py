import random

gameList = ["Rock", "Paper", "Scissors"]
computer = c = 0
commnad = p =0

print("Score : Computer: " + str(c) + " vs Player one: " + str(p))

run = True
while run:
    computer_choice = random.choice(gameList)
    commnad = input("Rock, Paper, Scissors or Quit : ")
    if commnad == computer_choice:
        print("Draw game")
    elif commnad == "Rock":
        if computer_choice == "Scissors":
            print("Winner Player 1")
            p += 1
        else:
            print("Computer Winner")
            c += 1
    elif commnad == "Paper":
        if computer_choice == "Rock":
            print("Winner Player 1")
            p += 1
        else:
            print("Computer Winner")
            c += 1
    elif commnad == "Scissors":
        if computer_choice == "Paper":
            print("Winner Player 1")
            p += 1
        else:
            print("Computer Winner")
            c += 1
    elif commnad == "Quit":
        break
    else:
        print("wrong command")
    print("Player one: " + commnad)
    print("Computer: " + computer_choice)
    print("")
    print("Score : Computer: " + str(c) + " vs Player one: " + str(p))
    print("")