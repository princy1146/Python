

import random
from functools import reduce

# 1. Define three functions and call them from a list
def fun():
    print("Function fun() called.")

def disp():
    print("Function disp() called.")

def msg():
    print("Function msg() called.")

def function_list_call():
    print(" Princy Shah")
    funcs = [fun, disp, msg]
    for f in funcs:
        f()

# 2. Add corresponding elements of two lists using map and lambda
def add_two_lists():
    print(" Princy Shah")
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [6, 5, 4, 3, 2, 1]
    result = list(map(lambda x, y: x + y, l1, l2))
    print("Resultant List:", result)

# 3. Generate random list and square the values
def square_random_numbers():
    print(" Princy Shah")
    lst = random.sample(range(-15, 16), 10)
    squares = list(map(lambda x: x**2, lst))
    print("Original:", lst)
    print("Squares:", squares)

# 4. Filter palindromes from a list
def filter_palindromes():
    print(" Princy Shah")
    lst = ['madam', 'Python', "malayalam", 12321]
    is_palindrome = lambda s: str(s) == str(s)[::-1]
    result = list(filter(is_palindrome, lst))
    print("Palindromes:", result)

# 5. Filter faculty names longer than 8 characters
def long_faculty_names():
    print(" Princy Shah0")
    faculty = ['Dr. Sharma', 'Anil', 'Rameshwari', 'Meenal', 'Rajendra', 'Devanshi']
    result = list(filter(lambda name: len(name) > 8, faculty))
    print("Names > 8 characters:", result)