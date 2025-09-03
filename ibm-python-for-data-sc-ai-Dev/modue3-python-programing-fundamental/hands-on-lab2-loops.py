# **Loops in Paython**

# We use loops to repeat a given operation many times.
# Repeated executions like this are performed by loops.
# We will look at two types of loops, for loops and while loops.

# Range for loops:
# Example:
# Before we discuss loops lets discuss the range object. 
# It is helpful to think of the range object as an ordered list. For now, 
# let's look at the simplest case. If we would like to generate an object that contains elements 
# ordered from 0 to 2 we simply use the following command:
range(3) # one element
range(0,3) # three elements 0,1,2

# For Loops:
# The for loops enable you to exexute a block of code multiple times
# For example, you would use this if you would like to print out every element in a list.
# Let's try to use a for loop to print all the years presented in the list dates:
dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])

#We can change the elements in a list:
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

# We can access the index and the elements of a list as follows:
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)    

# ** While Loops**



