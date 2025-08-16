# hands-on-lab-4.py
# This lab demonstrates various Python concepts including variables, data types, and string manipulation.
# String
# Use quotation marks for defining strings in Python.
# Strings can be defined using single quotes (' ') or double quotes (" ").
# Digitals and spaces '1 2 3 4 5 6 'in strings are preserved as they are.
# Special characters in strings '@#2_#]&*^%$ can be escaped using a backslash (\).

# 13-String Indexing
# 
# String indexing in Python allows you to access individual characters in a string.
# Each character in a string has a unique index, starting from 0 for the first character
# and going up to n-1 for the nth character, where n is the length of the string.
# Example of string indexing:
my_string = "Hello, World!"
first_character = my_string[0]  # This will be 'H'
second_character = my_string[1]  # This will be 'e'
print(my_string[5])  # This will print the 6th character, which is ','
# Negative indexing allows you to access characters from the end of the string.
# The last character can be accessed with index -1, the second last with -2,
# and so on.
last_character = my_string[-1]  # This will be '!'
second_last_character = my_string[-2]  # This will be 'd'
print(my_string[-3])  # This will print the 3rd last character, which is 'l'
#Slicing allows you to extract a substring from a string.
substring = my_string[0:5]  # This will be 'Hello', extracting characters from index 0 to 4
print(substring)  # This will print 'Hello'
# You can also use negative indices for slicing.
substring_negative = my_string[-6:-1]  # This will be 'World', extracting characters from index -6 to -2
print(substring_negative)  # This will print 'World'
# Slicing can also be done with a step value.
substring_step = my_string[0:12:2]  # This will be 'Hlo ol', extracting every second character from index 0 to 11
print(substring_step)  # This will print 'Hlo ol'
# You can also use slicing to reverse a string.
reversed_string = my_string[::-1]  # This will reverse the string, resulting in '!dlroW ,olleH'
print(reversed_string)  # This will print '!dlroW ,olleH'
# String methods can be used to manipulate strings.
# For example, you can convert a string to uppercase or lowercase.
uppercase_string = my_string.upper()  # This will convert the string to uppercase, resulting in 'HELLO, WORLD!'
print(uppercase_string)  # This will print 'HELLO, WORLD!'  
lowercase_string = my_string.lower()  # This will convert the string to lowercase, resulting in 'hello, world!'
print(lowercase_string)  # This will print 'hello, world!'
# You can also find the length of a string using the len() function.
string_length = len(my_string)  # This will be 13, as there are 13 characters in the string
print(string_length)  # This will print 13
# You can check if a substring exists within a string using the 'in' operator.
substring_exists = "World" in my_string  # This will be True, as 'World' is a substring of my_string
print(substring_exists)  # This will print True
# Stride    # You can use stride to skip characters in a string.
# For example, my_string[::2] will return every second character of the string.
is_x_y = (x is y)  # This will be True, as x and y refer to the same object
is_x_z = (x is z)  # This will be False, as x and z are different objects
is_not_x_z = (x is not z)  # This will be True, as x and z are different objects
print(is_x_y, is_x_z, is_not_x_z)  # This will print the results of the identity operations.
#Escape sequences can be used to include special characters in strings.
escape_string = "Hello\nWorld!"  # This will include a newline character between 'Hello' and 'World!'
print(escape_string)  # This will print 'Hello' on one line and 'World!' on the next line
# You can also use escape sequences for tabs, quotes, and other special characters.
escape_tab = "Hello\tWorld!"  # This will include a tab space between 'Hello' and 'World!'
print(escape_tab)  # This will print 'Hello' followed by a tab space and 'World!'
# You can use triple quotes for multi-line strings.
multi_line_string = """This is a multi-line string.It can span multiple lines
and preserve line breaks."""
print(multi_line_string)  # This will print the multi-line string with preserved line breaks    

#use r before the string to treat it as a raw string, ignoring escape sequences.
