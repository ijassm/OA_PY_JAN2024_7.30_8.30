# Class
class Student:
    firstName = ""
    lastName = ""
    age = 0
    location = ""
    skills = []

    def getDetails(self):
        print("Student Details")
        print("-" * 10)
        print("First Name", self.firstName)
        print("Last Name", self.lastName)
        print("Age", self.age)
        print("Location", self.location)
        print("Skills :")
        for i in self.skills:
            print(i)
        print("-" * 10, end="\n" * 2)

    def getFullName(self):
        print(self.firstName + " " + self.lastName)


# Object

a = Student()
b = Student()

a.firstName = "Merwin"
a.lastName = "J"
a.age = 20
a.location = "Pondy"
a.skills = ["PYTHON", "C", "C++", "JAVA", "HTML", "CSS", "CANVA"]

b.firstName = "Yuvasri"
b.lastName = "S"
b.age = 19
b.location = "London"
b.skills = ["PYTHON", "C", "C++", "JAVA"]


# print(id(a))
# print(id(b))

# print(a)
# print(b)

a.getFullName()
a.getDetails()

b.getFullName()
b.getDetails()
