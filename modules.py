# third party module/packages

"""
A module is a single file containing Python code, 
whereas a package is a collection of modules that are 
organized in a directory hierarchy
"""

# user-defined module

import multiple

l = [2, 4, 6, 8]


# print(multiple.double(l))
# print(multiple.triple(l))
# print(double(l))
# print(triple(l))


# core module

import math
import random
import os

colors = ["white", "black", "green", "yellow"]

num = random.random()
# print(num * 4)
randomIndex = math.floor(num * 4)
print(colors[randomIndex])


# print(math)
# print(math.pi)
# print(math.e)
# print(math.pow(2, 3))
