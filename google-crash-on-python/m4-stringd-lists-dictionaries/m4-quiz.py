music_genres = ["rock", "pop", "country"]
music_genres.append("blues")    
print(music_genres)
# Should print ['rock', 'pop', 'country', 'blues']
speed_limits = {"street": 35, "highway": 65, "school": 15}
print(speed_limits["highway"])
# Should print 65

country = "Luxembourg"
print(country[3:6])
# Should print: emb
print(country[-5])
# Should print: b
print(country[8:])
# Should print: rg
# Should print: emb, b, burg    



#Question 1
#The format of the input variable “address_string” is: numeric house number, 
# followed by the street name which may contain numbers and could be several words long 
# (e.g., "123 Main Street", "1001 1st Ave", or "55 North Center Drive"). 

#Complete the string methods needed in this function so that input like "123 Main Street" will produce the output "House number 123 on a street named Main Street". This function should:

#accept a string through the parameters of the function;

#separate the address string into new strings: house_number and street_name; 

#return the variables in the string format: "House number X on a street named Y". 

def format_address(address_string):
  # Declare variables
    house_number = ""
    street_name = ""
  # Separate  the house number from the street name.
    address_parts = address_string.split()
  
    for address in address_parts:
        # check if the adress part is a number
        if address.isdigit():
            house_number = address
        else:
            street_name += address + " "
        # Remove the extra space at the end of the last "street_name".
        street_name = street_name.strip()
    # Use a string method to return the required formatted string.
    # Note that the variables need to be in the same order as the
    # {} placeholders within the string.
    # Also note that there is a space after "named" and before the last {}.
    return "House number {} on a street named {}".format(house_number, street_name)
print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street" 
print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"


print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"

# Question 2 
# Fill in the blank to complete the “string_words” function. This function should split up the words 
# in the given “string” and return the number of words in the “string”.  
# Complete the string operation and method needed in this function so that a function call like 
# "string_words("Hello, World")" will return the output "2".
def string_words(string):
  # Split the string into words and Return the number of words in the list.
    return len(string.split())

print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4

# # Question 2 
# Consider the following scenario about using Python lists: 

# A professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance
# list of students in the order they arrived in the classroom. 
# Aniyah was the first one to note which students arrived, and then Imani took over. 
# After class, they each entered their lists into the computer and emailed them to the professor.
# The professor wants to combine the two lists into one and sort it in alphabetical order. 

# Complete the code by combining the two lists into one and then sorting the new list. 
# This function should: accept two lists through the function’s parameters; combine the two lists;
# sort the combined list in alphabetical order; return the new list.

def alphabetize_lists(list1, list2):
  # Initialize new list
    new_list = []
    # Combine the lists
    new_list = list1 + list2
    # Sort the combined list
    new_list.sort()
   
    return new_list
Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']

# Question 4
# Fill in the blank to complete the squares() function. 
# This function should use a list comprehension to create a list of squared integers
# (using either the expression n*n or n**2).
# The function receives two variables and should return the list of squares that occur between 
# the start and end variables inclusively (meaning the range should include both 
# the “start” and “end” values). 
# Complete the list comprehension in this function so that input like squares(2, 3) 
# will produce the output [4, 9].

def squares(start, end):
    return [x*x for x in range(start, end+1)]

print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Question 5
# Fill in the blanks to complete the countries() function.
# This function accepts a dictionary containing a list of continents (keys) and several countries 
# for each continent (values).
# For each continent, format a string to print the names of the countries only.
# The values for each key should appear on their own line without the key.
 #Should print for {"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']
def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key-value pairs of the dictionary.
    for continent, countries in countries_dict.items():
        result += str(countries) + "\n"
        # Use a string method to format the required string.
    

    return result
    
print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))


# question 6
# Consider the following scenario about using Python dictionaries: 

# Tessa and Rick are hosting a party. Both sent out invitations to their friends, and each one collected 
# responses into dictionaries, with names of their friends and how many guests each friend was bringing.
# Each dictionary is a partial guest list, but Rick's guest list has more current information about
#  the number of guests. 

# Complete the function to combine both dictionaries into one, with each friend listed only once,
# and the number of guests from Rick's dictionary taking precedence, if a name is included in 
# both dictionaries. Then print the resulting dictionary. This function should:

# accept two dictionaries through the function’s parameters; combine both dictionaries into one,
# with each key listed only once; the values from the “guests1” dictionary taking precedence, 
# if a key is included in both dictionaries; then print the new dictionary of combined items.

def combine_guests(guests1, guests2):
 # Use a dictionary method to combine the dictionaries.
    guests2.update(guests1)
    return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}

# Question 7
# Consider the following scenario about using Python dictionaries:

# A teacher is using a dictionary to store student grades. The grades are stored as a point value out 
# of 100.  Currently, the teacher has a dictionary setup for Term 1 grades and wants to duplicate it
#  for Term 2. The student name keys in the dictionary should stay the same, but the grade values
#  should be reset to 0.

# Complete the “setup_gradebook” function so that input like “{"James": 93, "Felicity": 98, "Barakaa": 80}” will produce a resulting dictionary that contains  “{"James": 0, "Felicity": 0, "Barakaa": 0}”. This function should: 

# accept a dictionary “old_gradebook” variable through the function’s parameters;make a copy of the 
# “old_gradebook” dictionary; iterate over each key and value pair in the new dictionary;

# replace the value for each key with the number 0; return the new dictionary

def setup_gradebook(old_gradebook):
    # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook = old_gradebook.copy()
    # Complete the for loop to iterate over the new gradebook. 
    for student, grade in new_gradebook.items():
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[student] = 0
    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}