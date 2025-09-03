 # This study guide provides a quick-reference summary for tuples and its operations.

# Knowledge:

# **Tuple-specific operations and methods**
# Tuples are immutable, so they do not have methods that modify their contents. 
# Protecting data: Because tuples are immutable, they can be used in situations where you want to 
# ensure the data you have cannot be changed. This can be particularly helpful when dealing 
# with sensitive or important information that should remain constant throughout 
# the execution of a program.

# Hashable keys: Because they're immutable, tuples can be used as keys on dictionaries, which can 
# be useful for complex keys.
# Example:
my_tuple = (1, 2, 3)
my_dict = {my_tuple: "value"}  # my_dict is now {(1, 2, 3): "value"}

# Efficiency: Tuples are generally more memory-efficient than lists, making them advantageous when
#  dealing with large datasets.

# However, you can still access elements and perform some operations:
# The tuple() operator
# The tuple() operator is used to convert an iterable (like a list, string, or set) into a tuple.

# Example:
# 1- Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple, 
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)

# 2-Tuples with mutable objects
# Although tuples themselves are immutable, they can contain mutable objects, such as lists.
# This means that although the tuple cannot be modified (for example, you can't add or remove elements),
# the mutable elements within the tuple can be changed.

# Example:
# A tuple with a list as an element
my_tuple = (1, 2, ['a', 'b', 'c'])

# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = 'x'  
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])

# 3- Returning multiple values from functions
# One of the most useful aspects of tuples in Python is their ability to return multiple values from a function. 
# This allows a function to produce more than one result, providing flexibility and improving code readability.
# Example:
def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b

result = calculate_numbers(10, 2)
print(result)  # Outputs: (12, 8, 20, 5.0)

# In the above function, the four arithmetic calculations are returned as a tuple, 
# which can be assigned to a single variable (result), or "unpacked" into multiple variables:
def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b
sum_result, diff_result, prod_result, div_result = calculate_numbers(10, 2)
print(sum_result)  # Outputs: 12
print(diff_result)  # Outputs: 8
