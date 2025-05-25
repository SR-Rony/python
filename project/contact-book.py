#Welcome to python project contact book

users = {}

while True :
    print("\nContact Book App")
    print("1. Creat Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = input("Enter your choice = ")

    if choice =='1':
        name = input("Enter your name : ")
        if name in users :
            print(f"Contact name {name} already exists !")
        else :
            age = input('Enter age = ')
            email = input('Enter email = ')
            phone = input('Enter phone number = ')
            users[name] ={"age":int(age),"email":email,"phone":int(phone)}
            print("new user created is successfull")
            
    elif choice == "2" :
        name = input("Enter your name to view = ")
        if name in users :
            user = users[name]
            print(f'Name : {name} Age: {age,},phone : {phone}')
        else :
            print("Invalid name ",name)