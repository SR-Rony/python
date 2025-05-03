# my bank acount
print("Welcome to the bank")
# coustomar = (input("you have a bank account? (Yes/No) : "))

# if coustomar =="No":
#     print("Create a new account")
#     name = input("Enter your name : ")
#     email = input("Enter your email : ")
#     phone = input("Enter your phone number : ")
#     blance = int(input("Enter your balance : "))
#     pin = input("Enter your pin : ")

# else:
#     print("Login to your account")
#     name = input("Enter your name : ")
#     pin = input("Enter your pin : ")


class CreateAcount:
    def __init__(self,name,email,phone,blance,pin):
        self.name = name
        self.email = email
        self.phone = phone
        self.balnce = blance
        self.pin = pin
    
    def balance(self):
        print("Your balance is : ",self.balnce)
    
    def deposit(self,amount):
        self.balnce += amount
        print("Your new balance is : ",self.balnce)
        print("Deposit successful")

    def withdraw(self,amount):
         self.balnce -= amount
         print("successfully withdrawed")
         print("Your new balance is : ",self.balnce)



coustomar1 = CreateAcount("SR","srrony@gmail.com",1234567890,10000,1234)
print(coustomar1.name)
coustomar1.withdraw(200)
coustomar1.deposit(500)
coustomar1.balance()
