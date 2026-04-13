# Write a function to merge two dictionaries.
# Return the merged dictionary.
# For example, for inputs {'a': 1, 'b': 2} and {'c': 3, 'd': 4}, the output should be {'a': 1, 'b': 2, 'c': 3, 'd': 4}.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = merge_dictionaries(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 2: Using the ** Operator
d1 = {1: 'a', 2: 'b'}
d2 = {2: 'c', 4: 'd'}
print({**d1, **d2})
# {1: 'a', 2: 'c', 4: 'd'}

# Example 3: Using copy() and update()
d1 = {1: 'a', 2: 'b'}
d2 = {2: 'c', 4: 'd'}
d3 = d2.copy()
d3.update(d1)
print(d3)
# {2: 'b', 4: 'd', 1: 'a'}

# Create a dictionary
my_dict = {"name": "Amit", "age": 20}
# 1. Add new key-value pair
my_dict["city"] = "Delhi"  # New element added
print(my_dict)  # Output: {'name': 'Amit', 'age': 20, 'city': 'Delhi'}
# 2. Update existing key with new value
my_dict["age"] = 21  # Age overwritten
print(my_dict)  # Output: {'name': 'Amit', 'age': 21, 'city': 'Delhi'}
# 3. Add multiple key-value pairs using update()
my_dict.update({"job": "Student", "hobby": "Reading"})
print(my_dict)  # Output: {'name': 'Amit', 'age': 21, 'city': 'Delhi', 'job': 'Student', 'hobby': 'Reading'}

fruits = ["apple", "banana", "orange"]
print("apple" in fruits)  # Output: True
print("grape" in fruits)  # Output: False

# Python Program to Merge Two Dictionaries
d1 = {1:'a', 2:'b'}
d2 = {2:'c', 4:'d'}
print(d1|d2)
# {1: 'a', 2: 'c', 4: 'd'}



