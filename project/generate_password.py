# python project generate password
import random
import string

def generate_password (min_leng,numbers=True,special_charaters=True):

    latter = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = latter
    if numbers :
        character +=digits
    if special_charaters :
        character +=special
    
    pwd = ""
    meets_charaters = False
    has_number = False
    has_special = False

    while not meets_charaters or len(pwd) < min_leng :
        new_char = random.choice(character)
        pwd += new_char
        
        if new_char in digits :
            has_number = True
        elif new_char in special:
            has_special= True
        
        meets_charaters = True
        if numbers:
            meets_charaters = has_number
        if special_charaters:
            meets_charaters = meets_charaters and has_special

    return pwd
        

min_length = int(input("Enter the minimun lenght: "))
has_number = input("Do you want to have numbers (Y/N): ").lower() =="y"
has_special = input("Do you want to have special characters (Y/N): ").lower() =="y"

pwd = generate_password(min_length,has_number,has_special)

print("The generated password is :", pwd)