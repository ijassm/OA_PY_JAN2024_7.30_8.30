# Syntax error
# Runtime error

# print(name)
# print(5 / 0)

try:
    print(5 / 0)
    pass
    # print(name)
except ZeroDivisionError:
    # print("cannot divide by zero")
    raise ZeroDivisionError("cannot divide by zero")
except Exception as e:
    print("something went wrong : ", e)
else:
    print("everything went fine")
finally:
    print("this is always executed")
