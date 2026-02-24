print("Pramod", 123, "Amit", "John", sep='*',end="      ")
print("Pramod", 123, "Amit", "John", sep='*')

a, b, c = 45, 54, 67
print(a)
print(b)
print(c)
print(a,b,c,sep=" | ")

import keyword
print(keyword.kwlist)

_ = 12
print(_)

a = 10
_ = 45
_ = _+1 
print(_)

abc123 = 78
_pramod = "amit"
_abc = 23
# &123 = 23   x

pi = 3.14
name = "Pramod"
isMale = True

print(type(pi))
print(type(isMale))
print(type(name))

# # Complex numbers - Python - iota
# # i - root to per -1

complex_number = 2 + 3j
print(complex_number.real)
print(complex_number.imag)

b = abs(-10) # Return the absolute value of the argument.
print(b)
c =abs(-9)
print(c)
# 10
# 9

name = "This is a Big line"
print(type(name))
name = name + str(1)  # can only concatenate str (not "int") to str
print(name)

first_name = "Pramod"
last_name = "Dutta"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))

a = "ankit"
b = "kumar"
c = a + " "+ b
print(c)

dir = r'C:\pramod\n.txt'
print(dir)

dir = r"C:\pramod\t.txt"
print(dir)

dir = "C:\pramod\t.txt"
print(dir)

print(5 % 2) # Modules
print(5 // 2)

# 2 | 5 | 2 - Quotient
#   | 4 |
# --------
#     1 - Remainder

print(13 // 2)
print(13 % 2)

q, r = divmod(5, 2)
print(q)
print(r)

radius = 2
import math
print(math.pi)
print(math.pow(radius,2))
area = math.pi * math.pow(radius, 2)
print("Area of the circle is -> ", area)

def greet():
    print("Hello, Welcome to Python World!")
    
greet()
greet()
greet()

print("dasdadads")
greet()



