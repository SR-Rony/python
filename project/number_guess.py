import random

def guess_number() :

    print('welcome to number guess number')

    low_number= int(input("Enter the low number :"))
    high_number = int(input("Enter the hight number :"))

    print(f"You have 7 change to guess tha number between {low_number} and {high_number} let,s start !")

    num = random.randint(low_number,high_number)
    chang = 7
    guess = 0

    while guess < chang :

        guess += 1
        guessNum = int(input('Enter you guess number : '))

        if num == guessNum :
            print(f"Currect the number is {num} you guess it in {guess} attempts.")
            break

        elif num != guessNum and guess >=chang :
            print(f"The number was {num} your batter luck next time")

        elif guessNum > num :
            print("Too high try a low number")

        elif guessNum < num :
            print("Too low try a high number")
        
        else :
            print("Invelid number")

guess_number()


# nameList = ["rony","sabina","sagor","sabron","love"]

# guessName = random.choice(nameList)

# print(guessName)

# count = 0
# life = 5

# while life > count:
#     myName = input("inter your name : ")

#     if myName == guessName :

#         print(f"you wine live chang {life} result name is {myName}")
#         break

#     elif myName != guessName:
#         count +=1
#         print(f"you loss please try again your change : {life} ")


# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# number_guessed = random.randrange(10)

# print("The number is : ",number_guessed)

# chances = 3
# count = 0

# while count <=chances:
#     guess = int(input("Take a guess: "))
#     count +=1
#     if guess == number_guessed:
#         print(f"ongratulations!you guessed the number in {count}tha games number {number_guessed}")
#         break
#     elif guess >=count and guess != number_guessed:
#         chances -= 1
#         print (f"oops! you have {chances} chances left")
#     elif guess >number_guessed:
#         print("Your guess is too high.")
#     elif guess < number_guessed:
#         print("Your guess is too low.")