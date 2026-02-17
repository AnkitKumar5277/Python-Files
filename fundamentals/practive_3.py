# Python Program to Find LCM
# Python Program to find the L.C.M. of two input number
def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
num1 = 54
num2 = 24
print("The L.C.M. is", compute_lcm(num1, num2))
# The L.C.M. is 216
# Number1 * Number2 = L.C.M. * G.C.D.
# Program to Compute LCM Using GCD
# Python program to find the L.C.M. of two input number

# This function computes GCD 
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm
num1 = 54
num2 = 24 
print("The L.C.M. is", compute_lcm(num1, num2))

Write a function to calculate the lowest common multiple (LCM) of two numbers.

# The formula to calculate LCM is lcm(a, b) = abs(a*b) // gcd(a, b), where gcd() is the greatest common divisor of a and b.
# For example, with inputs 12 and 15, the output should be 60.
import math
def lcm(a, b):
    # Find the greatest common divisor (GCD) of a and b
    gcd = math.gcd(a, b)
    # Use the formula to calculate LCM
    return abs(a * b) // gcd
# Example usage
print(lcm(12, 15))  # Output: 60


# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
# Python program to convert decimal into other number systems
dec = int(input("Enter No."))
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

# output
# The decimal value of 344 is:
# 0b101011000 in binary.
# 0o530 in octal.
# 0x158 in hexadecimal.

# Python Program to Find ASCII Value of Character
# ASCII stands for American Standard Code for Information Interchange.
# Program to find the ASCII value of the given character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
# output
# The ASCII value of 'p' is 112

# Python Program to Print the Fibonacci sequence
# Program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
# #output 
# How many terms? 7
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8

#challenge
def fibonacci_less_than(n):
    # Start with the first two Fibonacci numbers
    sequence = [0, 1]
    # Keep adding numbers to the list until the next one is too big
    while True:
        next_number = sequence[-1] + sequence[-2]  # Add the last two numbers
        if next_number >= n:  # Stop if the next number is too big
            break
        sequence.append(next_number)  # Add the next number to the list
    return sequence


# Python Program to Display Powers of 2 Using Anonymous Function
# Display the powers of 2 using anonymous function
# terms = 10
# Uncomment code below to take input from the user
terms = int(input("How many terms? "))
# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))
print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
# # output
# The total terms are: 10
# 2 raised to power 0 is 1
# 2 raised to power 1 is 2
# 2 raised to power 2 is 4
# 2 raised to power 3 is 8
# 2 raised to power 4 is 16
# 2 raised to power 5 is 32
# 2 raised to power 6 is 64
# 2 raised to power 7 is 128
# 2 raised to power 8 is 256
# 2 raised to power 9 is 512

# Python Program to Check Armstrong Number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
# Output 1
# Enter a number: 663
# 663 is not an Armstrong number
# Output 2
# Enter a number: 407
# 407 is an Armstrong number

num = 1634
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   
#challenge
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
# Example usage:
number = 12345
result = sum_of_digits(number)
print(result)  # Output: 15
