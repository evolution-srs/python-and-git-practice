hands-on-lab-1.py
# This is a hands-on lab for Python basics.
# 1-print('Hello, Python!') print() is a function. 
# You passed the string 'Hello, Python!' as an argument to instruct Python on what to print.
print('Hello, Python!')  # This will print the string to the console.

# 2-import sys
# -print(sys.version)
# sys is a built-in module that contains many system-specific 
# parameters and functions, including the Python version in use. 
# Before using it, we must print the version of Python we are using.
import sys
print(sys.version)  # This will print the version of Python currently in use.

# 3-print(sys.version_info)
# -sys.version_info is a tuple that contains the version information of Python.  
import sys
print(sys.version_info)  # This will print the version information as a tuple.

# / # This is a single-line comment in Python.
# Comments are used to explain code and are ignored by the interpreter. 
# They can be single-line (using #) or multi-line (using triple quotes).

# 5-Print string error messages
# frint("Hello, Python!")
# This line contains a typo in the function name 'frint' instead of 'print'.
# This will raise a NameError because 'frint' is not defined.
# To fix it, we should change 'frint' to 'print'.
# 6-built-in error message
# print("Hello, Python!) 
# This line has a syntax error due to a missing closing quote.
# The correct line should be:  
print("Hello, Python!")

# 7-# Erros
# ((	print("This will be printed")
#	frint("This will cause an error")
#	print("This will NOT be printed")))
# This code block contains a mix of correct and incorrect function calls.
# The first print will execute, the second will raise an error, ))
# and the third will not execute due to the error in the second line.
#print("This will be printed")  # This will print the string to the console. 
#frint("This will cause an error")  # This will raise a NameError.
#print("This will NOT be printed")  # This line will not execute due to the error above.