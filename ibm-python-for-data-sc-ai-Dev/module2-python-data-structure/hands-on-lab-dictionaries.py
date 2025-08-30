# Hands-on Lab Dictionaries in Python

# Dictionaries consist of key and value, It is helpful to compare a dictionary to a list.
# Instead of being indexed numerically like a list, dictionaries have keys.
# These keys are the keys that are used to access values within a dictionary.
# Each key is separated from its value by a colon ":".
# Commas separate the items, and the whole dictionary is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces, like this "{}"


# Example: 
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5}
print(Dict) # Output: {'key1': 1, 'key2': '2', 'key3': [3, 3, 3], 'key4': (4, 4, 4), 'key5': 5}

# The keys can be strings: 
print(Dict["key1"]) # Output: 1

# Keys can also be any immutable object such as a tuple:
Dict[(0, 1)] = 0
print(Dict) # Output: {'key1': 1, 'key2': '2', 'key3': [3, 3, 3], 'key4': (4, 4, 4), 'key5': 5, (0, 1): 0}

#In summary, like a list, a dictionary holds a sequence of elements.#
# Each element is represented by a key and its corresponding value.#
# Dictionaries are created with two curly braces containing keys and values separated by a colon.
# For every key, there can only be one single value, however, multiple keys can hold the same value.
# Keys can only be strings, numbers, or tuples, but values can be any data type.

# Retreive the Key value ussing .key()
print(Dict.keys()) #output :
#dict_keys(['key1', 'key2', 'key3', 'key4', 'key5', (0, 1)])
