import random


nameList = ["rony","sabina","sagor","sabron","love"]

guessName = random.choice(nameList)

print(guessName)

count = 0
life = 5

while life > count:
    myName = input("inter your name : ")

    if myName == guessName :

        print(f"you wine live chang {life} result name is {myName}")
        break

    elif myName != guessName:
        count +=1
        print(f"you loss please try again your change : {life} ")


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