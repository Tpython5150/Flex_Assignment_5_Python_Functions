'''
The Calculator App 1 Task 1, 2, 3

The aim of the assignment is to build a basic calculator that can perform addition, subtraction,
multiplication, and division.

Task 1: Create functions for each arithmatic operation.
Task 2: Implement user input to recieve number and an operation choice.
Task 3: Ensure your program can handle division by zero and other potential 
        errors.

'''
import math

def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    return x / y
    
def main():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    return x, y

while True:
    operator = input("Enter: [a]dd: [s]ubtract: [m]ultiply: [d]ivide: [q]uit: ").lower()
    
    if operator == 'a':
        x, y = main()
        result = add_numbers(x, y)
        print(f"Result: {result}")
    elif operator == 's':
        x, y = main()
        result = subtract_numbers(x, y)
        print(f"Result: {result}")
    elif operator == 'm':
        x, y = main()
        result = multiply_numbers(x, y)
        print(f"Result: {result}")
    elif operator == 'd':
        x, y = main()
        result = divide_numbers(x, y)
        print(f"Result: {result}")
    elif operator == 'q':
        print("That's all folks!")
        break
    else:
        print("Invalid input. Please try again!")
    
    

   










