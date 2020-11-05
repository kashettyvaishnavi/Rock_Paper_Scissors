import random
from time import sleep

choices = ["Charmander","Squirtle","Bulbasur"]

computer = random.choice(choices)
print(computer)

player = False

while player == False:
    name = input("Hello,please enter your name: ")
    print(f"Hello,{name} Welcome to Pokymons Battle Game!!")
    player = input("Which pokymon do you want to choose?\n'Charmander':'Charmander'\n'Squirtle':'Squirtle'\n'Bulbasur':'Bulbasur'\n'Stop the game':'Stop'")
    if player == computer:
        print("It's a tie!!")
    elif player == "Charmander":
        if computer == "Squirtle":
            print("\nPlease, wait we are loading your results...")
            sleep(2)
            print("You lose!!")
        else:
            print("\nlease, wait we are loading your results...")
            sleep(2)
            print("You win!!")
    elif player == "Squirtle":
        if computer == "Bulbasur":
            print("\nPlease, wait we are loading your results...")
            sleep(2)
            print("You lose!!")
        else:
            print("\nPlease, wait we are loading your results...")
            sleep(2)
            print("you win!!")
    elif player == "Bulbasur":
        if computer == "Charmander":
            print("\nPlease, wait we are loading yuor results...")
            sleep(2)
            print("You lose!!")
        else:
            print("\nPlease, wait we are loading your results...")
            sleep(2)
            print("You win!!")
    elif player == "Stop":
        print("Thanks for playing!!")
        break
    else:
        print("That's not a valid play!")


    player = False
