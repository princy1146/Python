

# Ready-made exception handling examples

def try1():
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    c = a / b
    print("Division =", c)

def try2():
    try:
        a = int(input("Enter an integer: "))
        b = int(input("Enter another integer: "))
        c = a / b
        print("Division =", c)
    except ZeroDivisionError:
        print("Denominator 0 ????")
        try3()

def try3():
    try:
        a = int(input("Enter an integer: "))
        b = int(input("Enter another integer: "))
        c = a / b
        print("Division =", c)
    except ZeroDivisionError as zde:
        print("Denominator 0 ????")
        print(zde.args)
        input("Press a key.")
        print(zde)
    except ValueError:
        print("Unable to convert string to Int")
    except:
        print("Some unknown error")

def try4():
    try:
        date = eval(input("Enter Date: "))
    except SyntaxError:
        print("Invalid date entered.")
    else:
        print("You entered", date)

def try5():
    try:
        name = input("Enter a file name: ")
        f = open(name, 'r')
    except IOError:
        print("File not found:", name)
    else:
        n = len(f.readlines())
        print(name, "has", n, "lines")
        f.close()

# User-defined exception classes

class NumTooSmall(Exception):
    def __init__(self, arg):
        self.msg = arg
        print("Inside NumTooSmall")

class NumTooBig(Exception):
    def __init__(self, arg):
        self.msg = arg
        print("Inside NumTooBig")

def try6():
    d = {}
    for x in range(10):
        try:
            a = int(input("Enter a number: "))
            d[a] = a*a*a
            if a < 3:
                raise NumTooSmall(a)
            elif a > 30:
                raise NumTooBig(a)
        except ValueError:
            print("Error: Invalid Input")
        except NumTooSmall as me:
            print(a, "< 3")
        except NumTooBig as me:
            print(a, "> 30")
    print("Now in try6 ...")
    print(d)

# Example with finally block
def try7():
    try:
        name = input("Enter a file name: ")
        f = open(name, 'a')
        a, b = [int(x) for x in input("Enter two numbers separated by space: ").split()]
        c = a / b
        print(a, b, c)
        f.write("Writing %d into file.\n" % c)
    except IOError:
        print("File not found:", name)
    except ZeroDivisionError as zde:
        print("Denominator 0 ????")
        print(zde.args)
    finally:
        f.close()
        print(name, "file closed")

# Logical error fix: ensure integer input
def safe_integer_input():
    while True:
        try:
            n = int(input("Enter an integer: "))
            print("You entered:", n)
            break
        except ValueError:
            print("That's not an integer. Try again.")
