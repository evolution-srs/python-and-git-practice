# ** Conditions and Branching in Python Hands-on Lab

# Comparision Operation in Python with examples:

# 1. Equal: == 
# Example: 
a=5 
a==6 
# Output: False

# 2. Not equal: !=
# Example: 
a=5 
a!=6 
# Output: True

# Greater than >
# Example: 
a=5 
a>6 
# Output: False

# Less than <
# Example: 
a=5 
a<6 
# Output: True

# Greater or equal: 
# Example: 
a=5 
a>=6 
# Output: False

# Less than or equal:
# Example: 
a=5 
a<=6 
# Output: True
 
# Note: The inequality operation is also used to compare the letters/words/symbols according to 
# the ASCII value of letters. The decimal value following table represents the order of the character
# Upper Case Letters have different ASCII code than Lower Case Letters, 
# which means the comparison between the letters in Python is case-sensitive.

# **Branching in Python**

# Branching allow us to run diffrent statements for diffrent inputs.

# It is helpful to think of an if statement as a locked room, 
# if the statement is True we can enter the room and your program will run some predefined tasks, 
# but if the statement is False the program will ignore the task. 

# Branching Syntax: if condition statment: which contains a word if,any condition statement,
# and a colon at the end.Start your tasks which need to be executed under this condition in a new 
# line with an indent. The lines of code after the colon and with an indent will only be executed 
# when the if statement is True.The tasks will end when the line of code does not 
# contain the indent.

# Example:
age=19
#age=18
#expression that can be true or false
if age>18:
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )
#The statements after the if statement will run regardless if the condition is true or false 
print("move on")    

# Else Stament The else statement runs a block of code if none of the conditions are 
# 
# True before this else statement. Let's use the ACDC concert analogy again. If the user is 17 they
#  cannot go to the ACDC concert, but they can go to the Meatloaf concert. The syntax of the else 
# statement is similar as the syntax of the if statement, as else :
# Notice that, there is no condition statement for else

# Example:
age=18
#age=17
if age>18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")

# **Logical Operator**

# Sometimes you want to check more than one condition at once. For example, you might want to check
#  if one condition and anothercondition are true. Logical operators allow you
#  to combine or modify conditions.
# and
# or 
# not
# These operators are summarized for two variables

# Example:
album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")
