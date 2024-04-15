# Arbitrary Arguments, *args


# def sum(a, b):
#     return a + b

# print(sum(2, 5))
# print(sum(2, 5, 4))


def sum(*args):
    s = 0
    for i in args:
        s += i
    return s


# print(sum(3, 5, 7))
# print(sum(3))
# print(sum(3, 5))
# print(sum(3, 5, 4, 6, 7))


# Keyword Arguments


def person(name, age, location):
    print("Name: " + name)
    print("Age: " + str(age))
    print("Location: " + location)


# person("XYZ", 20, "pondy")
# person(location="pondy", age=20, name="ABC")


# Arbitrary Keyword Arguments, **kwargs


def person(**kwargs):
    print("Name: " + kwargs["name"])
    print("Age: " + str(kwargs["age"]))
    print("Location: " + kwargs["location"])


# person(name="XYZ", age=20, location="pondy")


# Default Parameter Value


def my_function(country="Norway"):
    print("I am from " + country)


# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
