import random

while True :

    choice = input("Roll the dice? Y/N : ").lower()

    if choice == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1},{die2})")
    elif choice == "n":
        print("Thank you for plaing!")
        break
    else:
        print("Invelid choice")