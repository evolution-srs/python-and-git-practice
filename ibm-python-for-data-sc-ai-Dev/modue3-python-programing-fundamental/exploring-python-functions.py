# ** Functions in Python **

# A function is a block of reusable code that performs a specific task.
# Functions help in organizing code, improving readability, and avoiding repetition.
# Functions enable you to break down complex problems into smaller, manageable parts.

# Type of Functions:
# 1. Built-in Functions: These are pre-defined functions provided by Python, such as print(), len(), type(), etc.
# 2. User-defined Functions: These are functions that you create to perform specific tasks.
# 3. Anonymous Functions (Lambda Functions): These are small, unnamed functions defined using the lambda keyword.

# ** Defining a Function **
# 1-you can define a function using the 'def' keyword followed by the function 'name' and parentheses().
# example: def greet():
# 2- The function contain parameters or arguments inside the parentheses, where you can define them also.
# example: def greet(name):
# 3- The function body starts with a colon (:) and is indented, you can also place 
# documentation (notes explain the code)before the body.
# example:
def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")
# 4- The function can return a value using the 'return' statement after the function block.
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b
# 5- You can call the function by using its name followed by parentheses, passing any required arguments.
greet("Alice")  # Output: Hello, Alice

# For example, we can create a function that multiplies two numbers. 
# The numbers will be represented by the variables a and b:
def multiply(a, b):
    """This function returns the product of two numbers."""
    return a * b
result = multiply(3, 4)
print(result)  # Output: 12

# the same function can be used for diffrent type of data