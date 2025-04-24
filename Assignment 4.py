

# 1. Print all alphabets in upper case and in lower case
def print_alphabets():
    print("Name :  Princy Shah")
    for ch in range(65, 91):
        print(chr(ch), end=' ')
    print()
    for ch in range(97, 123):
        print(chr(ch), end=' ')
    print()

# 2. Multiplication table of a given number
def multiplication_table(n):
    print("Name :  Princy Shah")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# 3. Count no. of alphabets and digits in a string
def count_alpha_digits(s):
    print("Name :  Princy Shah")
    alpha = digit = 0
    for ch in s:
        if ch.isalpha():
            alpha += 1
        elif ch.isdigit():
            digit += 1
    print(f"Alphabets: {alpha}, Digits: {digit}")

# 4. Check for prime, perfect, Armstrong, palindrome, automorphic
def check_properties(n):
    print("Name :  Princy Shah")
    is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
    is_perfect = sum(i for i in range(1, n) if n % i == 0) == n
    is_armstrong = n == sum(int(d)**len(str(n)) for d in str(n))
    is_palindrome = str(n) == str(n)[::-1]
    is_automorphic = str(n*n).endswith(str(n))

    print(f"Prime: {is_prime}, Perfect: {is_perfect}, Armstrong: {is_armstrong}, Palindrome: {is_palindrome}, Automorphic: {is_automorphic}")

# 5. Generate all Pythagorean Triplets with side length <= 30
def pythagorean_triplets(limit=30):
    print("Name :  Princy Shah")
    for a in range(1, limit):
        for b in range(a, limit):
            c = (a**2 + b**2)**0.5
            if c == int(c) and c <= limit:
                print(f"({a}, {b}, {int(c)})")

# 6. Print 24 hours with AM, PM, Noon, Midnight
def print_24_hours():
    print("Name :  Princy Shah")
    for h in range(24):
        if h == 0:
            print("12 Midnight")
        elif h < 12:
            print(f"{h} AM")
        elif h == 12:
            print("12 Noon")
        else:
            print(f"{h-12} PM")

# Helper factorial function
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# 7. Print nCr and nPr
def nCr_nPr(n, r):
    print("Name :  Princy Shah")
    ncr = factorial(n) // (factorial(r) * factorial(n - r))
    npr = factorial(n) // factorial(n - r)
    print(f"nCr = {ncr}, nPr = {npr}")

# 8. Print factorial of a number
def print_factorial(n):
    print("Name :  Princy Shah")
    print(f"Factorial of {n} = {factorial(n)}")

# 9. Print N natural numbers in reverse
def print_reverse(n):
    print("Name :  Princy Shah")
    for i in range(n, 0, -1):
        print(i, end=' ')
    print()

# 10. Generate N Fibonacci numbers
def fibonacci_series(n):
    print("Name :  Princy Shah")
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# 11. Calculate sin(x) using Taylor Series Expansion
def sin_x(x_deg, terms=10):
    print("Name :  Princy Shah")
    x = x_deg * 3.14159 / 180
    sinx = 0
    for i in range(terms):
        sign = (-1)**i
        sinx += sign * (x**(2*i + 1)) / factorial(2*i + 1)
    print(f"sin({x_deg}) ≈ {sinx}")
