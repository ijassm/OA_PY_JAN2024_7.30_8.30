# username = "ocean"
# password = "1234"

# print("welcome user")
# user = input("Enter your username: ")
# userPass = input("Enter your password: ")

# print(user)
# print(userPass)

# if user == username and userPass == password:
#     print("your loggedin successfully")
# else:
#     print("invalid credentials")

# print("hello")

# 1.  Write a C program to find maximum between two numbers.

# a = input("Enter A value: ")
# b = input("Enter B value: ")

# if a > b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# 2.Write a C program to find maximum between three numbers.

# a = int(input("Enter A value: "))
# b = int(input("Enter B value: "))
# c = int(input("Enter C value: "))

# print(type(a))
# print(type(b))
# print(type(c))

# if a > b and a > c:
#     print("a is greater than b and c")
# if b > a and b > c:
#     print("b is greater than a and c")
# if c > a and c > b:
#     print("c is greater than a and b")

# if a > b and a > c:
#     print("a is greater than b and c")
#     if b < c:
#         print("b is smaller than all")
#     else:
#         print("c is smaller than all")
# elif b > a and b > c:
#     print("b is greater than a and c")
#     if a < c:
#         print("a is smaller than all")
#     else:
#         print("c is smaller than all")
# else:
#     print("c is greater than a and b")
#     if b < a:
#         print("b is smaller than all")
#     else:
#         print("a is smaller than all")


print("Welcome to StarBucks😀")

print("1. Latte")

print("2. Cappuccino")

print("3. Ice cream")

user = int(input("Please choose your menu: "))

price = 0

latte = 200
cappuccino = 350
blackcurrent = 50
chocolate = 40
vanilla = 30
sugar = 20
cream = 30

if user == 1:
    addSugar = input("Do you want to add more sugar: Y/N")
    addCream = input("Do you want strong: Y/N")
    price += latte
    if addSugar == "Y":
        price += sugar
        print(f"sugar price: ₹{sugar}")
    if addCream == "Y":
        price += cream
        print(f"cream price: ₹{cream}")

    print(f"latte price: ₹{latte}")
    print(f"Your total amount: ₹{price}")

elif user == 2:
    addSugar = input("Do you want to add more sugar: Y/N")
    addCream = input("Do you want strong: Y/N")
    price += cappuccino
    if addSugar == "Y":
        price += sugar
        print(f"sugar price: ₹{sugar}")
    if addCream == "Y":
        price += cream
        print(f"cream price: ₹{cream}")

    print(f"latte price: ₹{cappuccino}")
    print(f"Your total amount: ₹{price}")


elif user == 3:
    print("1. blackcurrent")
    print("2. chocolate")
    print("3. vanilla")
    flavour = int(input("What flavour do you want: "))
    if flavour == 1:
        price += blackcurrent
        print(f"blackcurrent price: ₹{blackcurrent}")
    if flavour == 2:
        price += chocolate
        print(f"chocolate price: ₹{chocolate}")
    if flavour == 3:
        price += vanilla
        print(f"vanilla price: ₹{vanilla}")

    print(f"Your total amount: ₹{price}")

else:
    print("Invalid input")
