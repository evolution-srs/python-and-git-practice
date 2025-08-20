number = 1 # Initialize the variable
while number < 8:  # Complete the while loop condition
    print(number, end=" ")
    number +=1 # Increment the variable

# Should print 1 2 3 4 5 6 7 

for number in range(2,13,2):
    print(number)

# Should print:
# 2
# 4
# 6
# 8
# 10
# 12

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
# divided by the divisor.           
# Complete the code so that a function call like “divisible(100,10)” will return the number “10”.
def divisible(max, divisor):
    # Initialize a counter to keep track of divisible numbers
    count = 0
    # Ensure the loop starts from 0 and goes up to max - 1
    # Loop through numbers from 0 to max - 1
    for i in range(0, max):
        # Check if the current number is even and divisible by the divisor
        if i % divisor == 0:
            # Increment the counter if the condition is met
            count += 1
    # Return the final count of divisible numbers
    return count
# Print the divisible function result for testing


print(divisible(100, 10)) # output should be 10
print(divisible(10, 3)) # output should be 4
print(divisible(144, 17)) # output should be 8

# The “odd_numbers” function. This function should return a space-separated string of all odd positive numbers, up to and including the “maximum” variable that's passed into the function.#
# Complete the for loop so that a function call like “odd_numbers(6)” will return the numbers “1 3 5”.
def odd_numbers(maximum):
    return_string = "" # intilizing a variable the string
    # for loop to itrate through the range to maximum including the maximum.
    for i in range(1, maximum + 1):
        # Check if the number is odd.
        if i % 2 != 0:
            # If it is odd, add it to the return string with a space.
            return_string += str(i) + " "
    # Return the final string, stripping any trailing spaces.
    return return_string.strip()

print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed

for outer_loop in range(2, 6+1):
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print(inner_loop)