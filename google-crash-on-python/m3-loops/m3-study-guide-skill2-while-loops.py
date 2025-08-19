# Coding Skills
# Skill 2: Using while loops
# Use a while loop to print a sequence of numbers .
# For this example, the while loop will count down by threes starting 
# from 18 and ending at 0.
starting_number = 18

# The while loop will continue to loop until it reaches 0.
while starting_number >= 0:
# To make the sequence of numbers easier to read, include a space
    # between each number in the sequence. You can override the default 
    # behavior of the print() function by using the "end=" parameter with
    # the print() function. The syntax for adding a space is: end=" " 
    print(starting_number, end=" ")
    # Decrement the starting number by 3.
    starting_number -= 3
# Print a new line after the loop completes.
print()# The output of this code will be:
# 18 15 12 9 6 3 0
# This shows the sequence of numbers counting down by threes from 18 to 0.
# The while loop continues until the condition (starting_number >= 0) is no longer true

#  Use a while loop to count the number of digits in a numerical value 

# This function accepts a CEO's salary as a variable. 
# It counts the number of digits in the salary and 
# returns the sentence like:
# "The CEO has a 6-figure salary."
def X_figure(salary):

     # Initializes the counter as an integer.
     tally = 0

     # The if-statement checks if the variable "salary" 
    # is equal to 0.
    if salary ==0:
    # If true, then it increments the counter to 
        # show there is 1 digit in 0
        tally += 1
    
     The body of the while loop counts the digits 
        # in "salary" by counting the number of times 
        # "salary" can be divided by 10 until "salary" 
        # is no longer >= 1.
        salary = salary/10
        # Add 1 to the counter to tally the number of 
        # times the loop runs.
        tally += 1
        # Return the results of the "tally" of the number
    # of digits in "salary".
    return tally

# Call the X_figure function with 1 parameter, converted to a string,
# inside a print function with additional strings.
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")
# Output: The CEO has a 7-figure salary.    

#“factorial” function. This function will accept an integer variable “n” through the function parameters
#  and produce the factorials of this number (by multiplying this value by every number less than 
# the original number [n*(n-1)], excluding 0).  
def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1 # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1

#the “rows_asterisks” function. This function should print rows of asterisks (*),
#  where the number of rows is equal to the “rows” variable. 
# The number of asterisks per row should correspond to the row number 
# (row 1 should have 1 asterisk, row 2 should have 2 asterisks, etc.). 
#Complete the code so that “row_asterisks(5)” will print:

def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(rows):
        # Complete the inner loop range to control the number of * in each row
        for y in range(x + 1):
            # Print an asterisk without a newline
            print("*", end="")

#the “divisible” function. This function should count the number of values from 0 to the “max” parameter
# minus 1 that are evenly divisible by the “divisor” parameter. This means they do not have a remainder when divided by the divisor. Complete the code so that a function call like “divisible(100,10)” #
#will return the number “10”.            
