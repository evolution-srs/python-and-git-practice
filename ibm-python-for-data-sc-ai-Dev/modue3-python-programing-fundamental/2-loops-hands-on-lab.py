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
# The while loop is used to repeat a block of code as long as a certain condition is true.
# For example, we can use a while loop to print the elements in the previous dates list except 1973:
dates = [1982,1980,1973]
i = 0
while dates[i] != 1973:
    print(dates[i])
    i = i + 1
print('It took ', i ,'repetitions to get out of loop.')

# Quiz on Loops
# Write a for loop that prints out all the elements between -5 and 5 using the range function.
for i in range(-5,6):
    print(i)
# should print: -5 -4 -3 -2 -1 0 1 2 3 4 5

# Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
Genres=['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for genre in Genres:
    print(genre) # should print: rock R&B Soundtrack R&B soul pop

# Write a for loop that prints out the following list: 
# squares=['red', 'yellow', 'green', 'purple', 'blue']
squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)
# should print: red yellow green purple blue

# Write a while loop to display the values of the Rating of an album playlist stored in 
# thePlayListRatings list. If the score is less than 6, exit the loop.
# The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i =0
while PlayListRatings[i] >= 6:
    print(PlayListRatings[i])
    i = i + 1
# should print: 10 9.5 10 8 7.5

# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. 
# Stop and exit the loop if the value on the list is not 'orange':
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while i < len(squares) and squares[i] =="orange":
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)
# should print: ['orange', 'orange']
