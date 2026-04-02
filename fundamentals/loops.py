# Python Program to Add Two Matrices
# Program to add two matrices using nested loop
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)
# [17, 15, 4]
# [10, 12, 9]
# [11, 13, 18]

n = 10
n0 = 0
n1 = 1
x = 0
if n <= 0:
  print("enter positive integer:"n,":")
  print(n0)
else:
  print("number in fibonacci sequence upto", n,":")
  while x < n:
    print(n0, end = ',')
    nth = n0 + n1
    n0 = n1
    n1 = nth
    x += 1
  # output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,

# Define a generator function
def even_numbers():
    num = 0
    while num <= 10:
        yield num  # Pauses here and returns num, then resumes next time
        num += 2
# Use the generator
evens = even_numbers()  # This doesn't run the function yet
# Get values one by one
print(next(evens))  # Output: 0
print(next(evens))  # Output: 2
print(next(evens))  # Output: 4
# ... and so on
# Or loop through all
for even in even_numbers():
    print(even)
# Output: 0 2 4 6 8 10

# range vs xrange
numbers = range(1, 6)  # Creates a list: [1, 2, 3, 4, 5]
print("Using range():", list(numbers))  # Prints the full list
print("Memory used by range:", numbers.__sizeof__())  # Shows memory size
numbers_gen = range(1, 6)  # Acts like a generator in Python 3
print("Using xrange-like:", list(numbers_gen))  # Prints: [1, 2, 3, 4, 5]
print("Memory used by xrange-like:", numbers_gen.__sizeof__())  # Less memory

# Python Program to Find Armstrong Number in an Interval
# Program to check Armstrong numbers in a certain interval
lower = 100
upper = 2000
for num in range(lower, upper + 1):
   order = len(str(num))
   # initialize sum
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)
# #output
# 153
# 370
# 371
# 407
# 1634

while True:
  n1 = int(input("enter: "))
  n2 = int(input("enter: "))
  print(n1 + n2)

# Python Program to Display the multiplication Table
num = int(input("Display multiplication table of? "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
# output
# 12 x 1 = 12
# 12 x 2 = 24
# 12 x 3 = 36
# 12 x 4 = 48
# 12 x 5 = 60
# 12 x 6 = 72
# 12 x 7 = 84
# 12 x 8 = 96
# 12 x 9 = 108
# 12 x 10 = 120

# Python Program to Find HCF or GCD
def compute_hcf(x,y):
  if x>y:
    smaller = y
  else:
    smaller = x
  for i in range(1, smaller+1):
    if((x%i==0) and (y%i==0)):
      hcf = i
      return hcf
num1 = 54
num2 = 24
print("the h.c.f. is", compute_hcf(num1, num2))
# output
# The H.C.F. is 6

# Source Code: Using the Euclidean Algorithm
def compute_hcf(x,y):
  while(y):
    x,y = x&y
  return x
hcf = compute_hcf(300, 400)
print("the hcf is", hcf)
# The HCF is 100

# Python Program to Remove Punctuations From a String
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in my_str:
  if char not in punctuations:
    no_punct = no_punct + char
print(no_punct)
# Hello he said and went

# Python Program to Multiply Two Matrices
x = [[12,7,3],
     [4,5,6],
     [7,8,9]]
y = [5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
for i in range(len(x)):
  for j in range(len(y[0])):
    for k in range(len(y)):
      result[i][j] += x[i][k] * y[k][j]
for r in result:
  print(r)
# output
# [114, 160, 60, 27]
# [74, 97, 73, 14]
# [119, 157, 112, 23]

# Program to multiply two matrices using list comprehension
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[sum(a*b for a,b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]
for r in result:
     print(r)


# Python Program to Find the Factorial of a Number
# Python program to find the factorial of a number provided by the user.
# change the value for a different result
# num = 7
# To take input from the user
num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   # The factorial of 7 is 5040
# iteration	factorial*i (returned value)
# i = 1	1 * 1 = 1
# i = 2	1 * 2 = 2
# i = 3	2 * 3 = 6
# i = 4	6 * 4 = 24
# i = 5	24 * 5 = 120
# i = 6	120 * 6 = 720
# i = 7	720 * 7 = 5040

# Python program to find the factorial of a number provided by the user
# using recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1 or x == 0:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))
# change the value for a different result
num = 7
# to take input from the user
num = int(input("Enter a number: "))
# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)

# Write a function to calculate the factorial of a number.

# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# For example, for input5, the output should be 120
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Example usage
number = 5
print(f"The factorial of {number} is {factorial(number)}")



