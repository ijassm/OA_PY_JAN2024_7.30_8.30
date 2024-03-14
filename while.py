i = 0

# while i < 10:
#     i += 1
#     print("loop", i)

a = 156
rev = 0


# print(a % 10)
# a //= 10
rev = (rev * 10) + a % 10  # to get last int
a = a // 10  # to remove last int

rev = (rev * 10) + a % 10  # to get last int
a = a // 10  # to remove last int

rev = (rev * 10) + a % 10  # to get last int
a = a // 10  # to remove last int

print(a)
print(rev)
