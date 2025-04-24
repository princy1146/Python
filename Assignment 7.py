

# 1. Concatenate three dictionaries into a fourth
def concat_dictionaries():
    print("Name : Princy Shah")
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3}
    d3 = {'d': 4, 'e': 5}
    d4 = {**d1, **d2, **d3}
    print("Combined Dictionary:", d4)

# 2. Check if a dictionary is empty
def check_empty_dict():
    print("Name :  Princy Shah")
    d = {}
    if not d:
        print("Dictionary is empty.")
    else:
        print("Dictionary is not empty.")

# 3. Department-wise min and max salary
def dept_salary_stats():
    print("Name :  Princy Shah")
    emp_data = {
        'IT': [45000, 55000, 60000],
        'HR': [30000, 35000],
        'Finance': [50000, 70000, 65000]
    }
    for dept, salaries in emp_data.items():
        print(f"{dept} -> Min: {min(salaries)}, Max: {max(salaries)}")

# 4. Frequency of each character in a string
def char_frequency():
    print("Name : Princy Shah")
    s = input("Enter a string: ")
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    print("Character Frequency:", freq)

# 5. Total grocery bill calculation
def grocery_bill():
    print("Name :  Princy Shah")
    prices = {'milk': 20, 'bread': 15, 'butter': 40, 'eggs': 5}
    quantity = {'milk': 2, 'bread': 1, 'butter': 1, 'eggs': 12}
    total = 0
    for item in prices:
        item_total = prices[item] * quantity.get(item, 0)
        print(f"{item}: {prices[item]} x {quantity.get(item, 0)} = {item_total}")
        total += item_total
    print("Total Bill =", total)