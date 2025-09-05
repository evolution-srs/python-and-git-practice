# This is a quick guide to dictionary operation and methods in Python were learned in this module

# **Knowledge**
# Dictionary data type in Python used to organize elements in to collections
# Dictionary is consist of one key or more, with one vslue or more associated with each key, 
# inside curly brackets {}.
# Example:
my_dictionary = {"keyA":["value1", "value2"], "keyB":["value3", "value4"]}

# **Operations on Dictionary**

# len(dict) - return the number of item in a dictionary
# Examle:
print(len(my_dictionary))
# Output: 2

# For key in dictionary - Iterate over each key in the dictionary
# Example:
for key in my_dictionary:
    print(key)
# Output:
# keyA
# keyB

# For key, value in a dictionary.item() - iterate over each key,value pairs in a dictionary.
# Example:
for key, value in my_dictionary.items():
    print(key, value)
# Output:
# keyA ['value1', 'value2']
# keyB ['value3', 'value4']

# If key in dictionary - check if the key in the dictionary
# Example:
print("keyA" in my_dictionary)
# Output: True

# Dictionary[key]- Acsses a value associated with the value from the dictionary
# Example:
print(my_dictionary["keyA"])
# Output: ['value1', 'value2']

# dictionary[key] = vaule - Assign new value to the associate key in the dictionary.
# Examle:
my_dictionary["keyA"]= ["value5", "value6"]
print(my_dictionary)
# Output:   my_dictionary = {"keyA":["value5", "value6"], "keyB":["value3", "value4"]}

# del dictionary [key] - Removes a value using the associated key from a dictionary.
# Example:
del my_dictionary["keyA"]
print(my_dictionary)
# Output:   
# my_dictionary = {"keyB":["value3", "value4"]} 

# **Methods on Dictionary**

# dictionary.get(key, defult) - Returns the value corresponding to a key, 
# or the default value if the specified key is not present.
# Example: 
my_dictionary.get("keyB, default")
# Output: ['value3', 'value4']

# dictionary.keys() - Returns a sequence containing the keys in a dictionary.
# Example:
my_dictionary.keys()
# Output: ['keyA', 'keyB']

# dictionary.values() - Returns a sequence containing the values in a dictionary.
# Example:
my_dictionary.values()
# Output: [['value5', 'value6'], ['value3', 'value4']]

# dictionary[key].append(value) - Appends a new value for an existing key.
# Example:
my_dictionary["keyA"].append("value7")
print(my_dictionary)
# Output:   
# my_dictionary
# {'keyA': ['value5', 'value6', 'value7'], 'keyB': ['value3', 'value4']}

# dictionary.update(other_dictionary) - Updates a dictionary with the items from another dictionary.
# Existing entries are updated; new entries are added.
# 


# dictionary.clear() - Deletes all items from a dictionary.
# Example:
my_dictionary.clear()
print(my_dictionary)
# Output: {}

# dictionary.copy() - Makes a copy of a dictionary.
# Example:
my_dictionary.copy()
# Output:
# my_dictionary

# **Dictionaries versus Lists **

 # BOTH dictionaries and lists:
# 1- are used to organize elements into collections;

# 2- are used to initialize a new dictionary or list, use empty brackets;

# 3- can iterate through the items or elements in the collection; and

# 4- can use a variety of methods and operations to create and change the collections,
#  like removing and inserting items or elements.

# ONLY Dictionaries:
# are unordered sets;

# have keys that can be a variety of data types, including strings, integers, floats, tuples;.

# can access dictionary values by keys;

# use square brackets inside curly brackets { [ ] };

# use colons between the key and the value(s);

# use commas to separate each key group and each value within a key group;

# make it quicker and easier for a Python interpreter to find specific elements, as compared to a list.

# Example:
pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}  

print(pet_dictionary.get("dogs", 0))
# Should print ['Yorkie', 'Collie', 'Bulldog']

# ONLY Lists:
# are ordered sets;

# access list elements by index positions;

# require that these indices be integers;

# use square brackets [ ];

# use commas to separate each list element.
# Example:
pet_list  = ["Yorkie", "Collie", "Bulldog", "Persian", "Scottish Fold", "Siberian", "Angora", "Holland Lop", "Harlequin"]

print(pet_list[0:3])
# Should print ['Yorkie', 'Collie', 'Bulldog']
