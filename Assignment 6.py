

from datetime import date

# 1. Count number of boys and girls in a list (boys in tuple format)
def count_boys_girls():
    print("Name :  Princy Shah")
    people = ['Aarohi', ('Rahul',), 'Sneha', ('Karan',), ('Amit',), 'Neha']
    boys = sum(1 for p in people if isinstance(p, tuple))
    girls = len(people) - boys
    print(f"Boys: {boys}, Girls: {girls}")

# 2. Separate roll no., name, and age into 3 lists from a list of tuples
def separate_student_info():
    print("Name : Princy Shah")
    students = [(101, 'Rahul', 18), (102, 'Sneha', 19), (103, 'Karan', 18)]
    roll_nos = [s[0] for s in students]
    names = [s[1] for s in students]
    ages = [s[2] for s in students]
    print("Roll Numbers:", roll_nos)
    print("Names:", names)
    print("Ages:", ages)

# 3. Find number of days between two date tuples
def date_difference():
    print("Name : Princy Shah")
    date1 = (2025, 4, 1)
    date2 = (2025, 4, 14)
    d1 = date(*date1)
    d2 = date(*date2)
    delta = abs((d2 - d1).days)
    print(f"Days between {date1} and {date2}: {delta} days")

# 4. Sort food items by descending price
def sort_food_prices():
    print("Name : Princy Shah")
    food_prices = [('Pizza', 250), ('Burger', 120), ('Pasta', 200), ('Fries', 80)]
    sorted_food = sorted(food_prices, key=lambda x: x[1], reverse=True)
    print("Sorted by price (desc):", sorted_food)

# 5. Remove empty tuples from a list of tuples
def remove_empty_tuples():
    print("Name :  Princy Shah")
    tup_list = [(), ('Rahul',), (), ('Sneha', 20), (), ('Karan',)]
    filtered = [t for t in tup_list if t]
    print("Without empty tuples:", filtered)

# 6. Modify an element of a tuple (via conversion)
def modify_tuple():
    print("Name :  Princy Shah")
    tup = (10, 20, 30)
    tup_list = list(tup)
    tup_list[1] = 99
    tup = tuple(tup_list)
    print("Modified Tuple:", tup)

# 7. Delete an element of a tuple (via conversion)
def delete_tuple_element():
    print("Name : Princy Shah")
    tup = (10, 20, 30, 40)
    tup_list = list(tup)
    del tup_list[2]
    tup = tuple(tup_list)
    print("Tuple after deletion:", tup)

# 8. Code Output Challenge
def output_challenge():
    print("Name :  Princy Shah")
    lst = [('X', 'Y', 'Z'), 40, 50, 60]
    a = lst[0]
    print("Output of a =", a)  # Should print: ('X', 'Y', 'Z')