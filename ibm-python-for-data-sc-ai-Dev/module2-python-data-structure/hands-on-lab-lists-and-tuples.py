# Hands-on-Lab Lists and Tuples in Python

# List is a mutable sequence type in Python.
# It can hold a collection of items, which can be of different types.
# Lists are defined using square brackets [].
# Example of a list
my_list = [1, 2, 3, 'four', 5.0]
print(my_list)  # Output: [1, 2, 3, 'four', 5.0]

# You can access elements in a list using indexing.
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'four'
# Negative indexing is also supported.
print(my_list[-1])  # Output: 5.0   

# Lists Operations:

# 1- Slicing
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [2, 3, 4]
#The key rule to remember is:
    # The start index is inclusive.
    # The end index is exclusive.

# 2- Appending items
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6] remember that append adds to the end of the list.

# 3- List is mutable, meaning you can change its content.
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# 4- Removing items
my_list.remove(3)  # Removes the first occurrence of 3
print(my_list)  # Output: [10, 2, 4, 5, 6]  

# 5- Inserting items
my_list.insert(1, 20)  # Inserts 20 at index 1 
print(my_list)  # Output: [10, 20, 2, 4, 5, 6]

# 6- Spliting a list by a delimiter
# For example, if you have a string and want to convert it into a list:
my_string = "apple,banana,cherry"
my_list = my_string.split(",")  # Splits the string into a list
print(my_list)  # Output: ['apple', 'banana', 'cherry']

# 7- Copy and Clone a list
original_list = [1, 2, 3]
cloned_list = original_list.copy()  # Creates a shallow copy of the list
print(cloned_list)  # Output: [1, 2, 3]   
# Note: Cloning a list creates a new list with the same elements, but changes to the cloned list do not affect the original list.

# 8- Sorting a list
my_list = [5, 2, 9, 1, 5, 6]
my_list.sort()  # Sorts the list in ascending order
print(my_list)  # Output: [1, 2, 5, 5, 6, 9]

# 9- Reversing a list
my_list.reverse()  # Reverses the order of the list
print(my_list)  # Output: [9, 6, 5, 5, 2, 1]

# 10- Finding the length of a list
print(len(my_list))  # Output: 6

### Tuple is an immutable sequence type in Python.
# It can hold a collection of items, which can be of different types.
# Tuples are defined using parentheses ().
# Example of a tuple
my_tuple = (1, 2, 3, 'four', 5.0)
print(my_tuple)  # Output: (1, 2, 3, 'four', 5.0)

# You can access elements in a tuple using indexing.
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'four'    

# Negative indexing is also supported.
print(my_tuple[-1])  # Output: 5.0

# Tuples Operations:
# 1- Concatenation
tuple1 = (1, 2, 3)
tuple2 = ('four', 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  
# Output: (1, 2, 3, 'four', 5, 6)
 
 # 2- Slicing
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)
# The key rule to remember is:
# The start index is inclusive.
# The end index is exclusive.

# 3- Finding the length of a tuple
print(len(my_tuple))  # Output: 5

# 4- Counting occurrences of an item
print(my_tuple.count(2))  # Output: 1

# 5- Finding the index of an item
print(my_tuple.index(3))  # Output: 2

# 6- Tuples are immutable, meaning you cannot change their content.
# However, you can create a new tuple based on an existing one.
new_tuple = my_tuple + (6,)  # Adding a new item to create a new tuple
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# 7- Converting a tuple to a list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3] 

# 8- Converting a list to a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)    

# 9- Nested tuples
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1])  # Output: (2, 3)
# Accessing elements in a nested tuple
print(nested_tuple[1][0])  # Output: 2

# 10- Unpacking a tuple
a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3   


C_tuple=(-5, 1, -3)

# --- Difference between sorted() and .sort() ---

# 1. sorted() is a built-in function that returns a new sorted list.
#    It does not modify the original object.
print("\nOriginal tuple:", C_tuple)
new_sorted_list = sorted(C_tuple)
print("Result from sorted():", new_sorted_list)

# 2. .sort() is a list method that sorts the list in-place and returns None.
#    The line `sort.list(C_tuple)` in your original code is incorrect and causes an error.
#    Here is the correct way to use it on a list:
c_list_from_tuple = list(C_tuple) # First, convert the tuple to a list
print("List before .sort():", c_list_from_tuple)
c_list_from_tuple.sort() # Now, sort the list in-place
print("List after .sort():", c_list_from_tuple)

# --- Accessing Simple vs. Nested Tuples ---

print("\n--- Simple vs. Nested Tuple Access ---")
# A simple tuple
simple_tuple = (10, 20, 30)
print("Simple tuple:", simple_tuple)
print("Accessing with one index simple_tuple[1]:", simple_tuple[1])

# A nested tuple (a tuple containing another tuple)
nested_tuple = (10, (20, 30), 40)
print("\nNested tuple:", nested_tuple)
# Accessing with one index gets the entire inner tuple
print("Accessing with one index nested_tuple[1]:", nested_tuple[1])
# Accessing an element *inside* the inner tuple requires a second index
print("Accessing with two indices nested_tuple[1][1]:", nested_tuple[1][1])
