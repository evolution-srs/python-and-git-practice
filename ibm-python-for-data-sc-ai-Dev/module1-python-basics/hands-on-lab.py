
# hands-on-lab-5.py

# 15-String Format

# -String interpolation (f-strings)
# This is a way to format strings in Python 3.6 and later.
# It allows you to embed expressions inside string literals, using curly braces {}.
name = "Safaa"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# -Using format() method str.format()  
# This method allows you to format strings by inserting variables into a string template.
# by using curly braces {} as placeholders for variables, which are passed as arguments to the format() method
# this is a more flexible way to format strings compared to f-strings, especially for older versions of Python (before 3.6)
# It can also be used to format numbers, dates, and other data types.
# This is another way to format strings in Python. It uses curly braces {} as placeholders for variables which are passed as arguments in the format() method
name = "Safaa"
age = 47
greeting_format = "Hello, my name is {} and I am {} years old.".format(name, age)
print(greeting_format)

# -Using % operator
# %s: This is a placeholder for a string.
# %d: This is a placeholder for an integer.
# % (name, age): This is a tuple containing the variables name and age.
# The values of these variables will replace the placeholders in the string.
name = "Safaa"
age = 47    
greeting_percent = "Hello, my name is %s and I am %d years old." % (name, age)
print(greeting_percent)

# -Additional capabilities
# F-strings are also able to evaluate expressions inside the curly braces, which can be very handy. For example:
x = 10
y = 5   
result = f"The sum of {x} and {y} is {x + y}."
print(result)   

# You can also format numbers, such as controlling the number of decimal places:
pi = 3.141592653589793
formatted_pi = f"Pi is approximately {pi:.2f}."
print(formatted_pi) 

# -Raw String (r’’)
# A raw string is a string prefixed with 'r' or 'R' that treats backslashes as literal characters.
# This is useful for regular expressions or file paths where backslashes are common.    
raw_string = r"This is a raw string with a backslash: \n and it won't interpret it."
print(raw_string)
regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)
raw_string_path = r"C:\new_folder\file.txt"
print("Raw String Path:", raw_string_path)
