import math

def calculate_area_of_circle(radius):
    """Return the area of a circle given the radius."""
    return math.pi * radius ** 2
class Circle:
    """Class to represent a circle."""
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2
if __name__ == "__main__":
    circle = Circle(5)
    print("Circle Area:", circle.area())
    print("Area using function:", calculate_area_of_circle(5))

# single inheritence
class Father: # base class
    def car(self):
        print("Father ki car hai")

class Son(Father):
    def bike(self): # derived class
        print("son ki bike hai")

s = Son()
s.car()
s.bike()

# 👨‍👩‍👦 2. Multiple Inheritance
class Mother:
    def cooking(self):
        print("Mother ko cooking aati hai")

class Father:
    def driving(self):
        print("father ko driving aati hai")

class Child(Mother, Father):
    def study(self):
        print("child padhai karta h")

c = Child()
c.cooking()
c.driving()
c.study()

# 🪜 3. Multilevel Inheritance
class GrandFather:
    def house(self):
        print("grandfather ka house haI")

class Father(GrandFather):
    def car(self):
        print("father ki car hai")

class Son(Father):
    def bike(self):
        print("son ki bike hai")

s = Son()
s.house()
s.car()
s.bike()
print("---------------")

# 🌳 4. Hierarchical Inheritance
class Subject:
    def base(self):
        print("base subject: science")

class Physics(Subject):
    def topic(self):
        print("Topic: Motion")

class Chemistry(Subject):
    def topic(self):
        print("Topic: Atoms")

p = Physics()
c = Chemistry()
p.base()
p.topic()
c.topic()
print("--------------")

# ⚙️ 5. Hybrid Inheritance (Combination)
class A:
    def displayA(self):
        print("class A")
class B(A):
    def displayB(self):
        print("class B")
class C(A):
    def displayC(self):
        print("class C")
class D(B, C):
    def displayD(self):
        print("class D")
d = D()
d.displayA()
d.displayB()
d.displayC()
d.displayD()

# 🧩 6. super() Method
print("--------------")
class Employee:
    def __init__(self, name):
        self.name = name

class Programmer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

p = Programmer("Ankit", "Python")
print(p.name)
print(p.language)

# 🏷️ 7. Class Method
class Student:
    college = "IGNOU"
    @classmethod
    def info(cls):
        print("College name:", cls.college)

Student.info()

# 🏡 8. @property Decorator
class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
e = Employee("Ankit")
print(e.name)

# 🔐 9. Getters and Setters
class Employee:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

e = Employee("Ankit")
print(e.name)
e.name = "Hadin"
print(e.name)

# ➕ 10. Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y}"


p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)

# 🎀 11. Decorator
def decorator(func):
    def wrapper():
        print("Cake decorate kar rahe h")
        func()
        print("Decoration done")
    return wrapper()

@decorator
def make_cake():
    print("cake ready ho gaya")

# make_cake()

# 📜 12. List Comprehension
squares = []
for i in range(5):
    squares.append(i*i)
print(squares)

squares = [i * i for i in range(5)]
print(squares)

# 📚 13. Dictionary Comprehension
numbers = [1,2,3,4]
squares = {}
for n in numbers:
    squares[n] = n * n
print(squares)

squares = {n: n*n for n in numbers}
print(squares)

# 1. Class and Object
# Class is a blueprint for creating objects. Objects are instances of a class.
class Employee:
    company = "TechCorp"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary

    def increment(self, amount):
        self.salary += amount
        return self.salary

emp1 = Employee("Alice", 30, 50000)
emp2 = Employee("Bob", 25, 45000)

print(f"Employee 1: {emp1.name}, Age: {emp1.age}, Salary {emp1.get_salary()}, Company: {emp1.company}")
print(f"Employee 2: {emp2.name}, Age: {emp2.age}, Salary {emp2.get_salary()}, Company: {emp2.company}")

emp1.increment(5000)
print(f"Employee 1 after increment: {emp1.get_salary()}")

# 2. Class Attribute vs Instance Attribute
# Class attributes belong to the class, instance attributes belong to the object.
class Sample:
    a = "Ankit"
obj = Sample()
obj.a = "Vikky"
Sample.a = "Rohan"
print(f"Class attribute: {Sample.a}")
print(f"Instance attribute: {obj.a}")

# 3. Self Parameter
# 'self' refers to the instance calling the method. It is automatically passed.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

cat = Cat("Whiskers", 3)
cat.info()
cat.make_sound()

# 4. Static Method
# Static methods don’t require self and are decorated with @staticmethod.
class StaticExample:
    @staticmethod
    def greet():
        print("Hello, I am a static method!")

StaticExample.greet()
obj = StaticExample
obj.greet()

# 5. Constructor (__init__)
# Constructor is called automatically when an object is created.
class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print(f"Programmer {self.name} intialized with salary {self.salary} and pin {self.pin}")
p = Programmer("Ankit", 120000000, 240011)
print(f"{p.name}, {p.salary}, {p.pin}, {p.company}")

r = Programmer("Rohan", 1200000, 340000)
print(f"{r.name}, {r.salary}, {r.pin}, {r.company}")



# 1. Class and Object
# Class is a blueprint for creating objects. Objects are instances of a class.
class Employee:
    # Class attribute (shared by all objects)
    company = "TechCorp"

    def show_details(self):
        print(f"Employee works at {self.company}")

emp1 = Employee()   # instance attribute
emp2 = Employee()
emp1.show_details()
emp2.show_details()

# 2. Class vs Instance Attributes
# Class attributes belong to the class, instance attributes belong to specific objects
class Sample:
    a = "Ankit" #class attribute

# creating an object
obj = Sample()
obj.a = "Vikky" #instance attribute
Sample.a = "Rohan" # changing class attribute

print(Sample.a)
print(obj.a)

# 3. Self Parameter
# Self refers to the instance calling the method
class Cat:
    def __init__(self, name, age):
        self.name = name #instance
        self.age = age #instance

    def info(self):
        print(f"i am a cat. My name is {self.name} i am {self.age} years old")

#creating object and calling method
cat1 = Cat("Whiskers", 3)
cat1.info()

# Creating object and calling method
cat1 = Cat("Whiskers", 3)
cat1.info()

# 4. static method
# Static methods don't use self and are marked with @staticmethod
class StaticExample:
    @staticmethod
    def greet():
        print("Hello from static method !")

obj = StaticExample()
obj.greet()
StaticExample.greet()

# calling static method without self
obj = StaticExample()
obj.greet()
StaticExample.greet()

# 5. Constructor (__init__)
# Constructor initializes objects when they are created
class Programmer:
    company = "Microsoft" # class attribute

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

    def show_info(self):
        print(f"name : {self.name}, salary: {self.salary}, pin : {self.pin}, company : {self.company}")

p1 = Programmer("Ankit", 12000000, 23424)
p2 = Programmer("Hayy", 12000403, 34242)
p1.show_info()
p2.show_info()

# 6. Modelling a Problem in OOP
# Nouns -> Class (e.g., Car)
# Adjectives -> Attributes (e.g., color, speed)
# Verbs -> Methods (e.g., drive, stop)
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        print(f"the {self.color} car is driving at {self.speed} km/n")

    def stop(self):
        print(f"the {self.color} car has stopped")

    #creating object and using methods
car1 = Car("Red", 120)
car1.drive()
car1.stop()




