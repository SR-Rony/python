
class account :
    def __init__(self,name,blance,pin):
        self.name = name
        self.balnce = blance
        self.pin = pin

    def deposit(self,amount):
        print("Deposit amount is : ",amount)
        self.balnce +=amount
        print("Deposit is successfull")
        print("Your new balance is : ",self.balnce)

    def withdraw(self,amount):
        print("Withdraw ammount is : ",amount)
        self.balnce -= amount
        print("Withdraw is successfull")
        print("Your new balance is : ",self.balnce)
    def check_balance(self):
        print("Your current balance is : ",self.balnce)


coustomar1 = account("SR-Rony",100,1234)

print("coustomar name is : ",coustomar1.name)
print("coustomar balance is : ",coustomar1.balnce)
print("coustomar pin is : ",coustomar1.pin)
coustomar1.deposit(900)
coustomar1.withdraw(300)
coustomar1.check_balance()







# class Student :
#     def __init__(self,name,marks,):
#         self.name = name
#         self.marks = marks

#     def avaerage(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         result =  sum/3

#         print("Average of marks is : ",result)



# s1 = Student("SR",[60,90,50])

# s1.avaerage()
