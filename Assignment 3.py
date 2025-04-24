
# 1. Count how many vowels are there in a string.
def count_vowels(s):
    print("Name : Princy Shah")
    count = 0
    for ch in s.lower():
        if ch in 'aeiou':
            count += 1
    print(f"Number of vowels: {count}")

# 2(A). Convert all characters to lowercase (without built-in function)
def to_lower(s):
    print("Name :  Princy Shah")
    result = ''
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    print("Lowercase:", result)

# 2(B). Convert all characters to uppercase (without built-in function)
def to_upper(s):
    print("Name :  Princy Shah")
    result = ''
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    print("Uppercase:", result)

# 2(C). Toggle case (without built-in function)
def toggle_case(s):
    print("Name : Princy Shah")
    result = ''
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    print("Toggle case:", result)

# 3. Check whether one string is in another
def check_substring(s1, s2):
    print("Name : Princy Shah")
    if s1 in s2:
        print(f"'{s1}' is found in '{s2}'")
    else:
        print(f"'{s1}' is not found in '{s2}'")

# 4. Remove one string from another string
def remove_substring(base, remove):
    print("Name :  Princy Shah")
    final = ''
    i = 0
    while i < len(base):
        if base[i:i+len(remove)] == remove:
            i += len(remove)
        else:
            final += base[i]
            i += 1
    print("String after removal:", final)