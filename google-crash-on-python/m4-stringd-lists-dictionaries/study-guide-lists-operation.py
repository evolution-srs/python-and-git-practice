 # This study guide provides a quick-reference summary for list and its operations.

# Knowledge:

# **List-specific operations and methods**

# One major difference between lists and tuples is that lists are mutable (changeable) and tuples 
# are immutable (not changeable). There are a few operations and methods that are specific to changing data within lists:

# list[index] = x - Replaces the element at index [n] with x.
# Example:
# my_list = [1, 2, 3]   
# my_list[1] = 4         # my_list is now [1, 4, 3]

# list.append(x) - Appends x to the end of the list.
# Example:
my_list = [1, 2, 3]   
my_list.append(4)      # my_list is now [1, 2, 3, 4]

# list.insert(index, x) - Inserts x at index position [index].
# Example:
my_list = [1, 2, 3]   
my_list.insert(1, 4)  # my_list is now [1, 4, 2, 3]

# list.pop(index) - Returns the element at [index] and removes it from the list. 
# If [index] position is not in the list, the last element in the list is returned and removed.
# Example:
my_list = [1, 2, 3]
my_list.pop(1)        # Returns 2, my_list is now [1, 3]    
my_list.pop()         # Returns 3, my_list is now [1]

# list.remove(x) - Removes the first occurrence of x in the list.
# Example:
my_list = [1, 2, 3, 2]
my_list.remove(2)     # my_list is now [1, 3, 2]

# list.sort() - Sorts the items in the list.
# Example:
my_list = [3, 1, 2]
my_list.sort()        # my_list is now [1, 2, 3]

# list.reverse() - Reverses the order of items of the list.
# Example:
my_list = [1, 2, 3]
my_list.reverse()     # my_list is now [3, 2, 1]

# list.clear() - Deletes all items in the list.
my_list = [1, 2, 3]
my_list.clear()       # my_list is now []

# list.extend(other_list) - Appends all the elements of other_list at the end of list
# Example:
my_list = [1, 2, 3]
my_list.extend([4, 5])  # my_list is now [1, 2, 3, 4, 5]

# map(function, iterable) - Applies a given function to each item of an iterable (such as a list) 
# and returns a map object with the results
# Example:
my_list = [1, 2, 3]
squared_list = map(lambda x: x**2, my_list)  # squared_list is now [1, 4, 9]


# zip(*iterables) - Takes in iterables as arguments and returns an iterator that generates tuples,
#  where the i-th tuple contains the i-th element from each of the argument iterables.
# Example:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)  # zipped is now [(1, 'a'), (2, 'b'), (3, 'c')]  
# Note: The zip function returns an iterator in Python 3, so you may need to convert it to a list 
# or another type to see the results.

# List comprehensions:
# A list comprehension is an efficient method for creating a new list from a sequence or a range in a single line of code.
# It is a best practice to add descriptive comments about any list comprehensions used in your code, as their purpose can 
# be difficult to interpret by other coders.

# 1- [expression for variable in sequence] - Creates a new list based on the given sequence. 
#  Each element in the new list is the result of the given expression.

# Example:
my_list = [ x*2 for x in range(1,11) ]  # my_list is now [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 2- [expression for variable in sequence if condition] - Creates a new list based on a specified sequence. Each element is the result of the given expression; elements are added only if the specified condition is true. 

# Example:
my_list = [ x for x in range(1,101) if x % 10 == 0 ]  # my_list is now [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Note that tuples do not have comprehensions but a similar functionality can be achieved with: 

tuple(i for i in (1, 2, 3))

# When to use for loops or list comprehensions:
# In Python, list comprehensions are generally used for creating new lists from existing ones in a concise and readable manner,
# especially when the task involves simple transformations or filtering of elements. 

# for loops are more versatile and are preferred when the operation is more complex, requires multiple lines of code,
# involves statements other than expression (like print, pass, continue, break), or when you need to iterate over a list 
# without creating a new one.
