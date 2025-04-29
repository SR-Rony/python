#all conditional statements add
# number = 19
# if (number >18):
#     print("You are eligible to vote in year 18+")
# elif (number == 18):
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

number= float(input("Enter a number:"))

if(number >= 90):
    print("A+")
elif(number >= 80):
      print("A")
elif(number >= 70):
    print("B")
elif(number >= 60):
    print("C")
elif(number >= 50):
    print("D")
elif(number >= 40):
    print("E")
else:
    print("F")


    #even or odd    

num = number % 2
if (num == 0):
    print("Even")
else:
    print("Odd")

a= 5
b= 7
c= 3
if(a > b and a > c):
    print("a is greater")
elif(b > a and b > c):
    print("b is greater")
else:
    print("c is greater")