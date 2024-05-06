# ability 1
# def hof(func, iter):
#     print(func, iter)

# ability 2
# def hof(func, iter):
#     return func


# def s():
#     print("callback function")


# print(hof(s, (2, 4, 6)))

# usecase

l = [1, 2, 3, 4, 5]


# def double(l):
#     output = []
#     for i in l:
#         logic = i * 2
#         output.append(logic)
#     return output


# def triple(l):
#     output = []
#     for i in l:
#         logic = i * 3
#         output.append(logic)
#     return output


# def quadruple(l):
#     output = []
#     for i in l:
#         logic = i * 4
#         output.append(logic)
#     return output


# def quintuple(l):
#     output = []
#     for i in l:
#         logic = i * 5
#         output.append(logic)
#     return output


# print(double(l))
# print(triple(l))
# print(quadruple(l))
# print(quintuple(l))


def hof(func, iter):
    output = []
    for i in iter:
        logic = func(i)
        output.append(logic)
    return output


print(hof(lambda i: i * 2, l))
print(hof(lambda i: i * 3, l))
print(hof(lambda i: i * 4, l))

print(hof(lambda i: i * 5, l))
print(list(map(lambda i: i * 5, l)))
