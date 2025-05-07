student ={
    "name" : "SR",
    "age" : 20,
    "address" : {
        "city" : "Delhi",
        "state" : "Delhi",
        "country" : "India"
    },
    "country":"bengladesh"
}

# newStud = student.pop("age")
# newStud = student.items()
# newStud = student.popitem()
newStud = student.setdefault("name")
newStud = student.update("name")

print(newStud)

print("====================")  

print(student)