

import random

# 1. Convert words in a list to uppercase and store in a set
def list_to_upper_set():
    print("Name : Princy Shah")
    words = ['apple', 'banana', 'grapes', 'mango']
    upper_set = {w.upper() for w in words}
    print("Uppercase Set:", upper_set)

# 2. Create set of 10 random numbers, count <30, delete >35
def filter_random_set():
    print("Name :  Princy Shah")
    nums = {random.randint(15, 45) for _ in range(10)}
    print("Original Set:", nums)
    less_than_30 = len([n for n in nums if n < 30])
    print("Count < 30:", less_than_30)
    nums = {n for n in nums if n <= 35}
    print("Filtered Set (<=35):", nums)

# 3. Create empty set, add names, modify one, delete two
def modify_name_set():
    print("Name :  Princy Shah")
    names = set()
    for _ in range(5):
        name = input("Enter a name to add: ")
        names.add(name)
    print("Set after adding:", names)
    to_modify = input("Enter the name to modify: ")
    new_name = input("Enter the new name: ")
    if to_modify in names:
        names.remove(to_modify)
        names.add(new_name)
    print("Set after modification:", names)
    for _ in range(2):
        name = input("Enter name to delete: ")
        names.discard(name)
    print("Set after deletion:", names)

# 4. Separate names starting with A and B
def separate_names():
    print("Name :  Princy Shah")
    name_set = {'Ankit', 'Aarav', 'Bharat', 'Bhumi', 'Akash', 'Bina'}
    a_names = {name for name in name_set if name.startswith('A')}
    b_names = {name for name in name_set if name.startswith('B')}
    print("Names starting with A:", a_names)
    print("Names starting with B:", b_names)