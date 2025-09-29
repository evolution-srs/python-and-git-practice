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

def Mult (a ,b):
    """This function returns the product of two numbers or concatenates two strings."""
    c = a * b
    return c
    Mult(2, "The BodyGuard ")
print(Mult(2, "The BodyGuard "))

# Variables types
# Local variables: defined inside a function are local to that function and cannot be accessed outside
#  of it.
def local_example():
    x = 10  # Local variable
    print(f"Local variable x inside function: {x}")
# Global variables: defined outside any function and can be accessed from anywhere in the code.
# To modify a global variable inside a function, you need to use the 'global' keyword.
# NOTE: It is generally recommended to avoid using global variables when possible, 
# as they can lead to code that is harder to understand and maintain. 

#Count the Frequency of Words Appearing in a String Using a Dictionary.
def word_frequency(text):
    # intialize an empty dictionary to store word frequencies
    frequency = {}
    # split the text into words
    words = text.split()
    # iterate through each word in the list
    for word in words:
        # if the word is already in the dictionary, increment its frequency by 1
        if word in frequency:
            frequency[word] += 1
        # otherwise, add the word to the dictionary with a frequency of 1
        else:
            frequency[word] = 1
    return frequency
# Example usage
text = "hello world hello"
result = word_frequency(text)
print(result)  # Output: {'hello': 2, 'world': 1}   

# write a function that divides the first input by the second input:
def divide(a, b):
    # this function divides a by b and handles division by zero
    #check if the second input is zero
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b
# Example usage
result = divide(10, 2)  

# Write a function code to find total count of word little in the given string: 
# "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white 
# as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb 
# was sure to go"**
def count_little(text):
    # convert the string into lowercase to make the search case-insensitive
    text = text.lower()
    # split the text into words
    words = text.split()
    # count the occurrences of the word "little"
    count = words.count("little")
    return count
# Example usage
text = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
result = count_little(text)
print(result)  # Output: 4