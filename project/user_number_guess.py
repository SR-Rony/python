import random

print('welcome to number guess game')

user = input('are you play this game yes or no : ').strip().lower()

if user != 'yes':
    print('Ok, Goodbye')
else:
    high_number = input("Enter the high number: ")
    
    if not high_number.isdigit():
        print("Please enter a valid digit number")


    high_number = int(high_number)
    rendom_number = random.randint(0, high_number)
    lift = 5
    while lift >= 0:
        try:
            lift -= 1
            user_number = int(input("Enter your guess number: "))

            if user_number == rendom_number:
                print(f"Congratulations! You guessed the number {rendom_number} correctly.")
                break
            else:
                print(f"Sorry, the correct number was {rendom_number}. Better luck next time! and you have {lift} lift left")
                continue
                
        except ValueError:
            print("Please enter a valid digit number")
            high_number = input("Enter the high number: ")