#student details using single inheritance
"Computer Programming Tutor"

class Student:
    def __init__(self):
        self.name =input("Enter Your Name:")
        self.school = input("Enter your University Name:")
        self.regno = int(input("Enter your roll Number:"))

class Test (Student):
    def show(self):
        print("========================STUDENT INFO IS===============")
        print ("Name is:",self.name)
        print("University Name is:",self.school)
        print("Roll Number is:",self.regno)


obj = Test()
obj.show()
