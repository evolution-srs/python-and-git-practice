# List Quiz

#1- Fill in the blank using a for loop. With the given list of "filenames", this code should rename all files
#  with the extension .hpp to the extension .h. The code  should then generate a new list called "new_filenames" 
# that contains the file names with the new extension.
# You are given a list of filenames like this:

import pip


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

# Output the list with all of the ".hpp" files renamed to end with ".h". Leave the other filenames alone.
# For this question, you must use a for loop to create the list. 

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = []
for filename in filenames:
    if filename.endswith(".hpp"):
        new_filenames.append(filename.replace(".hpp", ".h"))
    else:
        new_filenames.append(filename)
print(new_filenames)

# 2- Fill in the blank using a list comprehension. With the given list of "filenames", 
# this code should rename all files with the extension .hpp to the extension .h. The code function should 
# then generate a new list called "new_filenames" that contains the filenames with the new extension.
# you are given a list of filenames like this:

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

# Output the list with all of the ".hpp" files renamed to end with ".h".
# Leave the other filenames alone. For this question, you must use list comprehension to create the list. 

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list comprehension using as many lines of code as your chosen method requires.
new_filenames = [filename.replace(".hpp", ".h") if filename.endswith(".hpp") else filename for filename in filenames]
print(new_filenames)

# 3.Create a function that turns text into pig latin. Pig latin is a simple text transformation that
#  modifies each word by:

# moving the first character to the end of each word;

# then appending the letters "ay" to the end of each word.

# For example, "python" ends up as "ythonpay".

# Make sure that there is no trailing whitespace at the end of the return output.

def pig_latin(text):
    say=""
    words=text.split()
    for word in words:
        word=word[1:]+word[0]+"ay"
        say+=word+" "
    return say.strip()
print(pig_latin("hello how are you"))
print(pig_latin("programming in python is fun"))

#add a new element to a list at a specified index position
# Example:
list=[1,2]
list.insert(2,3)
print(list)

# Fill in the blanks to complete the biography_list() function. 
# This function reads in a list of tuples people, which contains the name, age, and profession of each person.
# Then, prints the sentence "__ is _ years old and works as __." 

# For example, biography_list([("Ira", 30, "a Chef")]) should print: 
# Ira is 30 years old and works as a Chef.
# Make sure that there is a period at the end of each sentence. 
# Otherwise your response will be evaluated as incorrect.

def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples. 
    for person in people:
         # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"   
        name, age, profession = person

        # Format the required sentence and place the 3 variables 
        # in the correct placeholders using the .format() method.
        print(("{} is {} years old and works as {}.").format(name, age, profession))

# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])

