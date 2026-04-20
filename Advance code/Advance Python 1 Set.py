# Advance Python 1 set
'''
def readFile(filename):
  with open(filename,"r") as f:
    print(f.read())

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
'''

# real method is below ->
'''
def readFile(filename):
  try:
    with open(filename,'r') as f :
      print(f.read())
  except FileNotFoundError:
    print(f"File{filename} is not found")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
'''

# write a program to print third fifthe and seventh element from a list using enurmerate function
'''
l = [1,2,3,4,5,6,7,8,9,10]
for index, item in enumerate(l):
  if index == 2 or index == 4 or index == 6:
     # print(index, item)
    print(f"the{index + 1}th element is {item}")
'''

# write a list comprehension to print a list which contains the multipication table of a user entered number
'''
n = int(input("Enter your number : "))
table = [ n*i for i in range(1,11) ]
print(table)
'''

# write a program to display a / b where a and b are integers if b = 0, display infinite by handling the zero division error
'''
a = int(input("enter number a : "))
b = int(input("enter number b : "))
try:
  print(a/b)
except:
  print("Infinite")
'''

# store the multipication tables generated in problem 3 in a file named tables table.txt
'''
n = int(input("enter your number : "))

table = [n*i for i in range(1,11)]
print(table)
with open("tables.txt","a") as f:
  f.write(str(table))
  f.write('\n')
'''





