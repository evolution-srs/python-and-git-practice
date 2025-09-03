 # This study guide provides a coding skills practice for list quiz.

# Skill Group 1
# Use a for loop to modify elements of a list.

# Use the list.append() method.

# Use the string.endswith() and string.replace() methods to modify the elements within a list.

# This block of code changes the year on a list of dates.
# The "years" list is given with existing elements. 
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The variable "updated_years" is initialized as a list data type 
# using empty square brackets []. This list will hold the new list
# with the updated years. 
updated_years = []
# The for loop checks each "year" element in the list "years".
for year in years:
    # The if-statment checks the "year" end with the substring "2023".
    if year.endswith("2023"):
        # If True, then a temporary variable "new" will hold the 
        # modified "year" element where the "2023" substring is 
        # replaced with the substring "2024".
        new = year.replace("2023", "2024")
        # Then, the list "updated_years" is appended with the changed
        # element held in the temporary variable "new".
        updated_years.append(year.replace("2023", "2024"))
    # If False, the original "year" element will be appended to the 
    # the "updated_years" list unchanged.
    else:
        updated_years.append(year)

print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]


# Skill Group 2
#Use a list comprehension to return values
# This list comprehension creates a list of squared numbers (n*n). It
# accepts two integer variables through the function’s parameters.
def squares(start, end):
    # The list comprehension calculates the square of a variable integer 
    # "n", where "n" ranges from the "start" to "end" variables inclusively.
    # To be inclusive in a range(), add +1 to the end of range variable.
    return [n*n for n in range(start, end+1)]

print(squares(0, 3)) 
# Should print [0, 1, 4]

print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Skill Group 3
# Use a list comprehension to modify elements of a list.

# Use the string.replace() method within a list comprehension.

# Use the string[index] method within a list comprehension.

# This block of code also changes the year on a list of dates using a
# different approach than demonstrated in Skill Group 1. By using a 
# list comprehension, you can see how it is possible to refactor the
# code to a shorter, more efficient code block.

# The "Years" list is given with existing elements
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024".
# This action will be executed if the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]

print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

# Skill Group 4
# Use the string.split() method to separate a string into a list of individual words.
# Iterate over the new list using a for loop.
# Modify each element in the list by slicing the element’s string at a given [1:] index position and appending
#  the substring to the end of the element.
# Convert a list back into a string.

# This function splits a given string into a list of elements. Then, it
# modifies each element by moving the first character to the end of the 
# element and adds a dash between the element and the moved character. 
# For example, the element "2two" will be changed to "two-2". Finally,
# the function converts the list back to a string, and returns the
# new string.

def change_string(given_string):

    # Initialize "new_string" as a string data type by using empty quotes.`
    new_string = ""

    # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:
        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items: 
        # + Each list "element" (starting at index position [1:]), 
        # + a dash "-", 
        # + append the first character of the "element" (using the index 
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-" + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string

print(change_string("1one 2two 3three 4four")) # Should print "one-1 two-2 three-3 four-4 five-5"  


# Skill Group 5
# Use the string.join() method to concatenate a string that provides a list name and its elements.

# This function accepts a list name and a list of elements, and returns
# a string with the format: "The "list_name" list includes: element1, 
# element2, element3". 
def list_elements(list_name, elements):
    # This task can be completed in a single line of code. The 
    # concatenation of strings, "list_name", and the list "elements" can
    # occur on the return line. In this case, the string "The " is added 
    # to the "list_name", plus the string " list includes: ", then the
    # "elements" are joined using a comma to separate each element of the 
    # list.
    return "The " + list_name + " list includes: " + ", ".join(elements)

print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"

# Skill Group 6
# Use map() and convert the map object to a list so we can print all the results at once.

# A simple function to add 1 to a given number
def add_one(number):
    return number + 1

# A list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
result = map(add_one, numbers)

# Convert the map object to a list to print the result
print(list(result))

# Outputs: [2, 3, 4, 5, 6]

# Skill Group 7
# Use zip() to combine a list of names and ages into a list of tuples, and print all the tuples at once.

# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Use zip to combine the lists
combined = zip(names, ages)

# Convert the zip object to a list to print the result
print(list(combined))

# Outputs: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]