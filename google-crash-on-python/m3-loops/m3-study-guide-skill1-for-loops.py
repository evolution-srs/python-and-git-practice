# Coding Skills:
# Skill 1:
# Using for loops with the range() function
# Use a for loop with the range() function with the end-of-range value included in the range.

# This function will accept an integer variable "end" and count by 10
# from 0 to the "end" value.
def count_by_tens(end):
    # initialize the loop variable
    count = ""

     # The range function parameters instruct Python to start the count  
     # at 0 and stop at the variable given as the upper end of the range. 
     # Since the value of the high end of a range is excluded by default,  
     # you can make Python include the "end" value by adding +1 to it. 
     # The third parameter tells Python to increment the count by 10.
    for i in range(0, end + 1, 10):

        # Initialize the increment variable
        # Although the variable "count" will hold a count of integers,  
        # this example will be converted to a string using "str(number)" 
        # in order to display the incremental count from 0 to the "end" 
        # value on the same line with a space " " separating each number.
        count += str(i) + " "

    # The .strip() method will trim the final space " " from the end of 
    # the string "count"
    return(count.strip())

 # Call the function with 1 integer parameter
print(count_by_tens(100))  # Output: 0 10 20 30 40 50 60 70 80 90 100

# Use a set of nested for loops with the range() function to create a matrix of numbers. 

# Include the upper range value in the range() function using end+1.

# This function uses a set of nested for loops with the range() function 
# to create a matrix of numbers. The upper range value in the range() 
# function should be included in the matrix. The matrix should consist 
# of a set of numbers that fill both rows and columns.
def create_matrix(n1, n2):
    # variables to hold the start and end values of the range
    start = n1
    end = n2 +1

    # Use nested loops to create the matrix, the first loop will create the first column of the matrix
    
    for coulumn in range(n1, n2 ):
        
        # and the nested loop will create the rows of the matrix.
        for row in range(n1, n2):
            # Print the current row and column values
            print(coulumn * row, end=' ')
        print()  # Print a new line after each row

# Call the function with 2 integer parameters. 
matrix(1, 4)
# Output:
# 1 2 3 4

# Predict the final value of a nested for loop with range() functions. 
# For this example, the outer for loop uses an end of range index of 
# 10. The value of index 10 will be 10-1, or 9. 
for oueter-loop in range(10):
# Using the "outer_loop" variable as the end of range for the  
    # inner loop, means the end of range index will be 9. The value 
    # of index 9 will be 9-1, or 8
    for inner_loop in range(oueter-loop):
        print(oueter-loop, inner_loop, end=' ')
    print()  # Output: (0,0), (1,0), (1,1), (2,0), (2,1), (2,2), ..., (9,0), (9,1), ..., (9,8)