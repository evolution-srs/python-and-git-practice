# Exception Hnaling Hands-on Lab

# What is an Exception?
# An exception is an event that occurs during the execution of a program that disrupts the
# normal flow of the program's instructions.
# When an exception occurs, the program stops executing and raises an error message.

# 1-ZeroDivisionError occurs when you try to divide by zero.
# print (10/0) # Output: ZeroDivisionError: division by zero

# 2- ValueError: This error occurs when an inappropriate value is used within the code. 
# An example of this is when trying to convert a non-numeric string to an integer:
num = int("abc") # Output: ValueError: invalid literal for int() with base 10: 'abc'

# 3- FileNotFoundError: This error occurs when trying to access a file that does not exist.
# with open("non_existent_file.txt", "r") as file: 
#     content = file.read() # Output: FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'

# 4- IndexError: This error occurs when trying to access an index that is out of range for 
# a list or array.
my_list = [1, 2, 3]
# print(my_list[3]) # Output: IndexError: list index out of range

# 5- KeyError: This error occurs when trying to access a key that does not exist in a dictionary.
my_dict = {"a": 1, "b": 2}
# print(my_dict["c"]) # Output: KeyError: 'c'

# 6- TypeError: This error occurs when an operation or function is applied to an object of inappropriate type.
# For example, trying to concatenate a string and an integer:
# print("Hello" + 5) # Output: TypeError: can only concatenate str (not "int") to str

# 7- AttributeError: This error occurs when trying to access an attribute or method that does 
# not exist for a particular object.
my_string = "Hello"
# print(my_string.upper()) # Output: HELLO
# print(my_string.non_existent_method()) # Output: AttributeError: 'str' object has no attribute 'non_existent_method'

# 8- ImportError: This error occurs when trying to import a module that does not exist or 
# cannot be found.
# import non_existent_module # Output: ImportError: No module named 'non_existent_module'

# 9- IndentationError: This error occurs when there is an issue with the indentation of the code.
# def my_function():        
# print("Hello") # Output: IndentationError: expected an indented block after function definition on line 1

# 10- SyntaxError: This error occurs when there is a syntax error in the code.
# print("Hello" # Output: SyntaxError: unexpected EOF while parsing

# Handling Exceptions
# 1-try-except block. 
# The code that may raise an exception is placed inside the try block, and the code to handle 
# the exception is placed inside the except block.
# 1- The code that may result in an exception is contained in the try block.
# 2- If an exception occurs, the code directly jumps to except block.
# 3-In the except block, you can define how to handle the exception gracefully, like displaying an error 
# message or taking alternative actions.
# 4- After the except block, the program continues executing the remaining code.
# Example:
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")# Output:Error: Cannot divide by zero


#2- Multiple except blocks try-except-else-finally
# You can have multiple except blocks to handle different types of exceptions separately.
# else allows one to check if there was no exception when executing the try block. 
# This is useful when we want to execute something only if there were no errors.
# finally block is used to define a block of code that will always be executed, regardless of
# whether an exception occurred or not. This is often used for cleanup actions, such as closing
# files or releasing resources.

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
# Output: Please enter a number to divide a0
# The number you provided cant divide 1 because it is 0

# Output: Please enter a number to divide aabc
# You did not provide a number  
# Output: Please enter a number to divide a2
# success a= 0.5
# Processing Complete   
# Output: Please enter a number to divide a
# Something went wrong
# Processing Complete   
# Note: The finally block will always execute, regardless of whether an exception occurred or not.  
# This is useful for cleanup actions that need to be performed regardless of the outcome of the try-except blocks.
# In this example, the user is prompted to enter a number to divide 1.
# Depending on the input, different exceptions may be raised, and the corresponding except blocks will handle
# them. If no exceptions occur, the else block will execute, and finally, the finally block will always execute.

# wright a division function that takes two parameters and returns the result of the division.
# Use exception handling to manage potential errors, such as division by zero or invalid input types.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return result
    finally:
        print("Division operation attempted.")
# Test cases
print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: Error: Cannot divide by zero
print(divide_numbers(10, 'a'))  # Output: Error: Invalid input type. Please provide numbers.
# In this function, we attempt to divide num1 by num2. If a ZeroDivisionError or TypeError occurs, we handle it gracefully by returning an appropriate error message.
# If the division is successful, we return the result. The finally block will always execute, indicating that the division operation was attempted.
# Note: The finally block is optional and can be omitted if not needed.