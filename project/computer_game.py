import random

print("hello welcome to the computer game")

plaing = input("Do you want to play the game? (yes/no): ").strip().lower()

if plaing != "yes":
    quit("Goodbye!")

print("Great! Let's start the game. :)")

name_list = ['rony', 'simon', 'john', 'jane', 'doe']

name = random.choice(name_list)

changes = 3

while changes > 0:
    print(f"You have {changes} attempts left to guess the name.")
    guess = input("Guess a name from the list (rony, simon, john, jane, doe): ").strip().lower()

    if(name == guess):
        changes -= 1
        print(f"Congratulations! You guessed the name  correctly. The name is {name}. and you guessed it in {changes} attempts.")
        break
    else:
        print("Sorry, that's not correct. The number was", name)
        changes -= 1