

import random
import collections

# 1. Create a list of odd and even integers, replace, flatten, sort
def list_operations():
    print(" Princy Shah")
    odd_list = random.sample(range(1, 100, 2), 5)
    even_list = random.sample(range(2, 100, 2), 4)
    print("Odd List:", odd_list)
    print("Even List:", even_list)
    
    odd_list[2] = even_list
    print("After replacing 3rd odd element with even list:", odd_list)

    flat_list = []
    for item in odd_list:
        if isinstance(item, list):
            flat_list.extend(item)
        else:
            flat_list.append(item)

    flat_list.sort()
    print("Flattened & Sorted List:", flat_list)

# 2. Generate 20 random numbers and find all occurrences of a given number
def find_occurrences():
    print(" Princy Shah")
    numbers = [random.randint(1, 10) for _ in range(20)]
    print("Generated List:", numbers)
    target = int(input("Enter number to find: "))
    positions = [i for i, val in enumerate(numbers) if val == target]
    print(f"Occurrences of {target} at positions:", positions)

# 3. Generate 50 random numbers (1-30), remove duplicates
def remove_duplicates():
    print(" Princy Shah")
    nums = [random.randint(1, 30) for _ in range(50)]
    print("Original List:", nums)
    no_duplicates = list(set(nums))
    print("Without Duplicates:", no_duplicates)

# 4. Separate +ve and -ve numbers
def separate_positive_negative():
    print(" Princy Shah")
    nums = [random.randint(-50, 50) for _ in range(30)]
    positives = [n for n in nums if n > 0]
    negatives = [n for n in nums if n < 0]
    print("Original List:", nums)
    print("Positive Numbers:", positives)
    print("Negative Numbers:", negatives)

# 5. Convert list of 5 strings to uppercase
def convert_uppercase():
    print(" Princy Shah")
    words = ["python", "list", "random", "program", "university"]
    upper_words = [w.upper() for w in words]
    print("Uppercase Words:", upper_words)

# 6. Convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    print(" Princy Shah")
    temps_f = [random.randint(32, 100) for _ in range(5)]
    temps_c = [(f - 32) * 5 / 9 for f in temps_f]
    print("Fahrenheit:", temps_f)
    print("Celsius:", temps_c)

# 7. Stack using list (Menu-driven)
def stack_menu():
    print(" Princy Shah")
    stack = []
    while True:
        print("\n1.Push 2.Pop 3.Display 4.Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            val = input("Enter value to push: ")
            stack.append(val)
        elif ch == 2:
            if stack:
                print("Popped:", stack.pop())
            else:
                print("Stack is empty")
        elif ch == 3:
            print("Stack:", stack)
        elif ch == 4:
            break
        else:
            print("Invalid choice")

# 8. Queue using deque (Menu-driven)
def queue_menu():
    print(" Princy Shah")
    queue = collections.deque()
    while True:
        print("\n1.Insert 2.Delete 3.Display 4.Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            val = input("Enter value to insert: ")
            queue.append(val)
        elif ch == 2:
            if queue:
                print("Deleted:", queue.popleft())
            else:
                print("Queue is empty")
        elif ch == 3:
            print("Queue:", list(queue))
        elif ch == 4:
            break
        else:
            print("Invalid choice")

# 9. Elements from list1 not in list2 using list comprehension
def difference_in_lists():
    print("Name : Princy Shah")
    list1 = [random.randint(1, 20) for _ in range(10)]
    list2 = [random.randint(1, 20) for _ in range(10)]
    diff = [x for x in list1 if x not in list2]
    print("List1:", list1)
    print("List2:", list2)
    print("Difference (List1 - List2):", diff)