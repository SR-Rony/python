
# python range function

start = int(input("Enter the start number : "))
end = int(input("Enter the end number : "))

skip = int(input("Enter the skip number : "))

result = range(start,end)

if start > end:
    print("Start number should be less than end number")

for i in result:
    
    if i == skip:
        print("Skip number : ",i)
        continue
    print("Number : ",i)


 
# x = range(2,100,2)

# print(len(x))


# for i in x:
#     if i % 2 ==0:
#         print("Even number : ",i)
#     else:
#         print("Odd number : ",i)