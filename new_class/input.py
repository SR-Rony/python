
name = input("Enter your name: ")
age = int(input("Enter your age: "))
isStudent = input ("Are you a student? (yes/no): ").strip().lower() == 'yes'


if isStudent:
    print(f"Hello {name}, you are {age} years old and you are a student.")
    if age < 18:
        print("You are a minor.")

else:
    print(f"Hello {name}, you are {age} years old and you are not a student.")


