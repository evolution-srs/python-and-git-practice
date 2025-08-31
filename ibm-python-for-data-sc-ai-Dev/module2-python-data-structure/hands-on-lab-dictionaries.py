# Hands-on Lab Dictionaries in Python

# Dictionaries consist of key and value, It is helpful to compare a dictionary to a list.
# Instead of being indexed numerically like a list, dictionaries have keys.
# These keys are the keys that are used to access values within a dictionary.
# Each key is separated from its value by a colon ":".
# Commas separate the items, and the whole dictionary is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces, like this "{}"


# Example: 
# It's best practice (PEP 8) to use lowercase_with_underscores for variable names.
sample_dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5}
print(sample_dict) # Output: {'key1': 1, 'key2': '2', 'key3': [3, 3, 3], 'key4': (4, 4, 4), 'key5': 5}

# The keys can be strings: 
print(sample_dict["key1"]) # Output: 1

# Keys can also be any immutable object such as a tuple:
sample_dict[(0, 1)] = 0
print(sample_dict) # Output: {'key1': 1, 'key2': '2', 'key3': [3, 3, 3], 'key4': (4, 4, 4), 'key5': 5, (0, 1): 0}

#In summary, like a list, a dictionary holds a sequence of elements.
# Each element is represented by a key and its corresponding value.
# Dictionaries are created with two curly braces containing keys and values separated by a colon.
# For every key, there can only be one single value, however, multiple keys can hold the same value.
# Keys can only be strings, numbers, or tuples, but values can be any data type.

# Retreive the Key value ussing .key()
print(sample_dict.keys()) #output :
#dict_keys(['key1', 'key2', 'key3', 'key4', 'key5', (0, 1)])

# Operation on Dictionaries:
# 1. Accessing Values
# You can access the value of a specific key using square brackets [].
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic["The Bodyguard"]) # Output: 1992

# 2. Adding or Updating a Key-Value Pair
# You can add a new key-value pair or update an existing one.
soundtrack_dic['Graduation'] = '2007'
print(soundtrack_dic) # Output: {'The Bodyguard': '1992', 'Saturday Night Fever': '1977', 'Graduation': '2007'}

# 3. Deleting a Key-Value Pair
# You can remove a key-value pair using the 'del' keyword.
del(soundtrack_dic['The Bodyguard'])
print(soundtrack_dic) # Output: {'Saturday Night Fever': '1977', 'Graduation': '2007'}

# 4. Verifying if a Key Exists
# The 'in' keyword can be used to check if a key is in the dictionary.
print('Saturday Night Fever' in soundtrack_dic) # Output: True
print('The Bodyguard' in soundtrack_dic) # Output: False

# 5. Getting all Keys
# The .keys() method returns a view object that displays a list of all the keys.
print(soundtrack_dic.keys()) # Output: dict_keys(['Saturday Night Fever', 'Graduation'])

# 6. Getting all Values
# The .values() method returns a view object that displays a list of all the values.
print(soundtrack_dic.values()) # Output: dict_values(['1977', '2007'])

# 7. Getting all Key-Value Pairs
# The .items() method returns a view object that displays a list of a given dictionary's key-value tuple pairs.
print(soundtrack_dic.items()) # Output: dict_items([('Saturday Night Fever', '1977'), ('Graduation', '2007')])

# 8. Getting a Value with a Default (Safe Access)
# The .get() method is a safer way to access a key's value. It returns the value for the specified key if 
# it exists.
# If the key does not exist, it returns None, or a specified default value, instead of raising a KeyError.
print(soundtrack_dic.get('Graduation')) # Output: 2007
print(soundtrack_dic.get('Thriller')) # Output: None
print(soundtrack_dic.get('Thriller', 'Not Found')) # Output: Not Found

# 9. Merging Dictionaries
# The .update() method merges a dictionary with another dictionary or with an iterable of key-value pairs.
new_releases = {'Thriller': '1982', 'Back in Black': '1980'}
soundtrack_dic.update(new_releases)
print(soundtrack_dic) # Output: {'Saturday Night Fever': '1977', 'Graduation': '2007', 'Thriller': '1982', 'Back in Black': '1980'}

# 10. Clearing a Dictionary
# The .clear() method removes all items from the dictionary.
soundtrack_dic.clear()
print(soundtrack_dic) # Output: {}

# ---
# Advanced Example: Structuring Data
# Dictionaries are powerful, but their structure is key.
#
# Bad Structure: Using numbered keys for different items. This is hard to loop through and manage.
bad_inventory = {
    'productno1': 'Mobile phone', 
    'productno1_quantity': 5, 
    'productno1_price': 20000,
}
# To add a new product, you have to manually create all new keys
bad_inventory['productno2'] = 'Laptop'
bad_inventory['productno2_quantity'] = 10
bad_inventory['productno2_price'] = 50000

# Better Structure: A list of dictionaries. Each item in the list is a complete record for one product.
inventory_list = [
    {'name': 'Mobile Phone', 'quantity': 5, 'price': 20000, 'release_year': 2020},
    {'name': 'Laptop', 'quantity': 10, 'price': 50000, 'release_year': 2023}
]

# Adding a new product is clean and easy
new_product = {'name': 'Tablet', 'quantity': 8, 'price': 15000, 'release_year': 2021}
inventory_list.append(new_product)

# Accessing a product and its properties is intuitive
print(f"The first product is a {inventory_list[0]['name']} which costs {inventory_list[0]['price']}.")
print(f"The third product is a {inventory_list[2]['name']}.")
