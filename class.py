class Student :
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def hello(self):
        print("Hello",self.name ,self.age)

    def ages(self):
        print("Hello",self.name ,self.age)
        return self.age



s1 = Student("SR",25,"A+")
# print(s1.hello(name))
# print(s1.ages(22))