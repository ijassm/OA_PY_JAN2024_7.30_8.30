s1 = "abcs"
s2 = "cxzca"

o = ""


# for i in s1:
#     if i not in s2:
#         o += i

# for i in s2:
#     if i not in s1:
#         o += i

s = s1 + s2

for i in s:
    if i not in s1 or i not in s2:
        o += i

print(o)

# len1 = len(s1)
# len2 = len(s2)

# if len1 > len2:
