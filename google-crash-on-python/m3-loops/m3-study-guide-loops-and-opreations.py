# This study guide provides a quick-reference summary for loops and its operations
# Loops in Python
# This file to review Loops in Python

# 1- While Loops
# A while loop repeatedly executes a block of code as long as a specified condition is true.
# Syntax:
# while condition:
#     # code block to execute
# Example:
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment the count variable # output: Count is: 0, 1, 2, 3, 4

# 2- For Loops
# A for loop iterates over a sequence (like a list, tuple, or string) or other iterable objects.
# Syntax:
# for item in iterable:
#     # code block to execute
# Example:  
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # output: apple, banana, cherry

# 3- Nested Loops
# You can nest loops inside other loops to perform more complex iterations.
# Example:
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)  # output: (1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)


# 4- Knowledge
# 4.1- Terms:

# a **Variable**: 
# A named location in memory that stores a value.
# You can create a variable by assigning a value to it using the `=` operator.
# You should choose meaningful names for your variables to make your code more readable.
# You should know how to properly initialize or increment a variable.
# You will also need to recognize a coding error due to the failure to properly initialize or increment a variable.

# b **Infinite Loop**:
#  A loop that never ends because its condition is always true.
# Know how to recognize an infinite loop and how to fix it.
# Check the condition of the loop to ensure it will eventually become false.
# Check the rannge of the loop to ensure it will eventually end.
# Check the iterable of the loop to ensure it will eventually end.
# Check the loop control statements to ensure they are not causing an infinite loop.

# c **Itrators**: 
# Objects that allow you to traverse through a collection (like a list or a string) one element at a time.
# In Python, you can create an iterator using the `iter()` function.
# Example:
my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(next(my_iterator))  # Output: 1   

# d **Loop Control Statements**: Statements that alter the flow of control in loops.
# They allow you to break out of a loop, skip an iteration, or do nothing.
# - `break`: Exits the loop immediately.
# - `continue`: Skips the current iteration and continues with the next iteration.
# - `pass`: Does nothing and is used as a placeholder.
# Example of break:
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# output: 1, 2
# Example of continue:
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# output: 1, 2, 4, 5
# Example of pass:
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)
# output: 1, 2, 4, 5

# e **Common syntax errors** :
# Misspellings, Incorrect indentations, Missing or incorrect key characters:
# Parenthetical types - ( curved ), [ square ], { curly }
# Quote types - "straight-double" or 'straight-single', “curly-double” or ‘curly-single’
# Block introduction characters, like colons - :
# Data type mismatches.
# Missing, incorrectly used, or misplaced Python reserved words.
# Using the wrong case (uppercase/lowercase) - Python is a case-sensitive language.

# 4.2 **Common Functions:

# 1- Looping with Range
# The `range()` a build in function generates a sequence of numbers, which is often used in loops.
# Syntax: range(start, stop[, step])
# range(start, stop, step) generates numbers starting from `start` (including)up to `stop` (excluding), incrementing by `step`.
# If `start` is omitted, it defaults to 0. If `step` is
# omitted, it defaults to 1.
# Example:
for i in range(1, 6):
    print(i)
    # output: 1, 2, 3, 4, 5

# 2-print() Function Default Behavior 
# The `print()` function in Python prints the specified message to the console.
# By default, it adds a newline character at the end of the message.
# You can change this behavior by using the `end` parameter.
# Example:  
for i in range(1, 6):
    print(i, end=' ')  # Output: 1 2 3 4 5 (all on the same line)
# use this teqnique to print the output of a loop on the same line.

# Coding Skills 
Skill 1
Skill 2
