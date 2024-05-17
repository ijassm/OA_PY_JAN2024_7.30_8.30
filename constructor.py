# Class
class Student:

    def __init__(self, firstName, lastName, age, location, skills):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.location = location
        self.skills = skills

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

a = Student(
    "Merwin", "J.", 20, "Pondy", ["PYTHON", "C", "C++", "JAVA", "HTML", "CSS", "CANVA"]
)
b = Student("Manogari", "S.T", 30, "Pondy", ["PYTHON"])


a.getFullName()
a.getDetails()

b.getFullName()
b.getDetails()
