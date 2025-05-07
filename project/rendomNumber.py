import random

print("welcome to number gussing games")

guessNumber = random.randint(1,100)


while True :
    try:
        userNumber = int(input("Please give tha choice your number: "))
        
        if guessNumber < userNumber :
            print("to high number")
        elif guessNumber > userNumber:
            print("to low number")
        else :
            print("you guessed tha number",guessNumber)
            break

    except ValueError :
        print("please inter a valid number")

# while True :

#     choice = input("Roll the dice? Y/N : ").lower()

#     if choice == "y":
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)
#         print(f"({die1},{die2})")
#     elif choice == "n":
#         print("Thank you for plaing!")
#         break
#     else:
#         print("Invelid choice")