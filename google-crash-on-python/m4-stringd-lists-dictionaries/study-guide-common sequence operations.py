 # This study guide provides a quick-reference summary.

# Knowledge:

# **Common sequence operations**

# Lists and tuples are both sequences and they share a number of sequence operations.
# The following common sequence operations are used by both lists and tuples:

# 1- Len(sequence): Returns the number of items in the sequence.
def sequence_len(sequence):
    return len(sequence)   
#example
print(sequence_len([1, 2, 3]))  # Output: 3

# 2- Index(sequence, item): Returns the index of the first occurrence of item in the sequence.
def sequence_index(sequence, item):
    return sequence.index(item) if item in sequence else -1
#example
print(sequence_index([1, 2, 3], 2))  # Output: 1

# 3- Count(sequence, item): Returns the number of occurrences of item in the sequence.
def sequence_count(sequence, item):
    return sequence.count(item)
#example
print(sequence_count([1, 2, 3, 2], 2))  # Output: 2

# 4- for elements in a sequence, use a for loop to iterate through each element.
def sequence_iterate(sequence):
    for element in sequence:
        print(element)
#example
sequence_iterate([1, 2, 3])  # Output: 1, 2, 3

# 5- if element in sequence: Checks if an element is present in the sequence.
def sequence_contains(sequence, item):
    return item in sequence
#example
print(sequence_contains([1, 2, 3], 2))  # Output: True

# 6- sequence[x]: Accesses the element at index x in the sequence.
def sequence_access(sequence, index):
    return sequence[index]
#example
print(sequence_access([1, 2, 3], 1))  # Output: 2

# 7- sequence[start:end]: Accesses a slice starting at index [start], ending at index [end-1]. 
# If [x] is omitted, the index will start at 0 by default. If [y] is omitted, 
# the len(sequence) will set the ending index position by default.
def sequence_slice(sequence, start, end):
    return sequence[start:end]
#example
print(sequence_slice([1, 2, 3, 4, 5], 1, 4))  # Output: [2, 3, 4]

# 8- for index, element in enumerate(sequence): 
# Iterates over both the indices and the elements in the sequence at the same time.
def sequence_enumerate(sequence):
    for index, element in enumerate(sequence):
        print(index, element)
#example
sequence_enumerate([1, 2, 3])  # Output: 0 1, 1 2, 2 3

# Because integers are not iterable, they need to be converted to a range as such:
# for x in range(len(someList)):
   # print(x)
# this will print out a numerical value up to the length of the original string

