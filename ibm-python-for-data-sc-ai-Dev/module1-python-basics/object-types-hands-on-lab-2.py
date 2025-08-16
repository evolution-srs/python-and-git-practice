hands_on_lab_2.py

# 8-Types of objects in python
#Word: String- Numbers: Integer, Float- Boolean: True/False
# In Python, there are several built-in data types:   
# - String: A sequence of characters, e.g., "Hello, Python!"
# - Integer: A whole number, e.g., 42   
# - Float: A number with a decimal point, e.g., 3.14
# - Boolean: Represents True or False values.

# 9-Print the type of an object
type_of_string = "Hello, Python!"
type_of_integer = 42        
type_of_float = 3.14
type_of_boolean = True
print(type(type_of_string))  # This will print <class 'str'> for string.
print(type(type_of_integer))  # This will print <class 'int'> for integer.
print(type(type_of_float))    # This will print <class 'float'> for float.
print(type(type_of_boolean))  # This will print <class 'bool'> for boolean. 

# 10-Converting from one object type to a different object type
# In Python, you can convert between different data types using built-in functions.
# For example: 
# - To convert a string to an integer: int("42")
# - To convert an integer to a string: str(42)          
# - To convert a float to an integer: int(3.14)
# - To convert an integer to a float: float(42)     
# - To convert a boolean to an integer: int(True) or int(False)
# - To convert an integer to a boolean: bool(0) or bool(1)
int("42")          # Converts string to integer
str(42)           # Converts integer to string      
int(3.14)        # Converts float to integer
float(42)        # Converts integer to float    
int(True)        # Converts boolean True to integer (1)
int(False)       # Converts boolean False to integer (0)
type(True)         # This will print <class 'bool'> for boolean.
type(False)        # This will print <class 'bool'> for boolean.
int(True)          # This will print 1, as True is converted to integer.
int(False)         # This will print 0, as False is converted to integer.


# 11-Expressions
# An expression in Python is a combination of values and operators that can be evaluated to produce a result.
# For example:  
result = 5 + 3 * 2  # This is an expression that evaluates to 11.
# And just like mathematics, multiplication and division has priority .
print(result)  # This will print the result of the expression, which is 11. 
#And just like mathematics, expressions enclosed in parentheses have priority.
result_with_parentheses = (5 + 3) * 2  # This evaluates to 16.

# 12-Variables
# A variable in Python is a name that refers to a value.
# Variables are used to store data that can be referenced and manipulated in a program.
# You can create a variable by assigning a value to it using the equals sign (=).
my_variable = 42  # This creates a variable named my_variable with the value 42.
print(my_variable)  # This will print the value of my_variable, which is 42
## Use another variable to store the result of the operation between variable and value

y = x / 60
y  # This creates a variable y that stores the result of dividing x by 60.
# overwrite the value of the variable
x = 100  # This changes the value of x to 100.
#Name variables meaningfully
user_age = 25  # This creates a variable named user_age with the value 25
