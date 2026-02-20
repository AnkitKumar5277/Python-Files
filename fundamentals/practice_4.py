# Python Program to Find the Sum of Natural Numbers
num = 16
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
# The sum is 136

# Write a function to find the sum of first N natural numbers.
# Hint: The formula for the sum of the first N natural numbers is N*(N+1)/2.
# For example, for input 5, the outout should be 15.
def sum_of_natural_numbers(n):
    if n < 1:
        return "Input must be a positive integer."
    return n * (n + 1) // 2  # Using integer division for an exact result
number = 5
result = sum_of_natural_numbers(number)
print(f"The sum of the first {number} natural numbers is {result}.")

# Program to transpose a matrix using a nested loop
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for r in result:
   print(r)
# [12, 4, 3]
# [7, 5, 8]

''' Program to transpose a matrix using list comprehension'''
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
for r in result:
   print(r)

# Python Program to Find Numbers Divisible by Another Number
my_list = [12, 65, 54, 39, 102, 339, 221,]
# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))
print("Numbers divisible by 13 are",result)
# Numbers divisible by 13 are [65, 39, 221]

# Write a function to check if a number is divisible by five.
# Return True if the number is divisible by 5. Otherwise, return False.
def is_divisible_by_five(number):
    return number % 5 == 0
# Example usage
print(is_divisible_by_five(10))  # True
print(is_divisible_by_five(12))  # False
print(is_divisible_by_five(0))   # True
print(is_divisible_by_five(-15)) # True

# Factorial of a number using recursion
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
num = 7
# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
# The factorial of 7 is 5040

# challenge:
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Example usage:
number = 5
print(f"The factorial of {number} is {factorial(number)}.")



