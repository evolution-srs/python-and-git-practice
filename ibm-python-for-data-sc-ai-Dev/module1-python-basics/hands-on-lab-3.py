
# hands-on-lab-4.py

# 13-Operators
# Operators in Python are used to perform operations on variables and values.
# There are several types of operators: 
# - Arithmetic operators: +, -, *, /, %, ** (exponentiation)
# - Comparison operators: ==, !=, <, >, <=, >= for comparing values
# - Logical operators: and, or, not for combining boolean expressions
# - Assignment operators: =, +=, -=, *=, /= for assigning values to variables
# - Bitwise operators: &, |, ^, ~, <<, >> for bit-level operations
# - Identity operators: is, is not for checking object identity
# - String operators: + (concatenation), * (repetition) for string manipulation
# Example of arithmetic operators:
a = 10  
b = 5
sum_result = a + b  # This will be 15
difference_result = a - b  # This will be 5
product_result = a * b  # This will be 50   
quotient_result = a / b  # This will be 2.0
modulus_result = a % b  # This will be 0 (remainder of division)
exponent_result = a ** b  # This will be 100000 (10 raised to the power of 5)
print(sum_result, difference_result, product_result, quotient_result, modulus_result, exponent_result)  # This will print the results of the arithmetic operations.     
# Example of comparison operators:
is_equal = (a == b)  # This will be False, as 10 is not equal to 5
is_not_equal = (a != b)  # This will be True, as 10 is not equal to 5
is_greater = (a > b)  # This will be True, as 10 is greater than 5
is_less = (a < b)  # This will be False, as 10 is not less than 5
is_greater_or_equal = (a >= b)  # This will be True, as 10 is greater than or equal to 5
is_less_or_equal = (a <= b)  # This will be False, as
# 10 is not less than or equal to 5
print(is_equal, is_not_equal, is_greater, is_less, is_greater_or_equal, is_less_or_equal)  # This will print the results of the comparison operations.
# Example of logical operators:
logical_and = (a > 0 and b > 0)  # This will be True, as both a and b are greater than 0
logical_or = (a > 0 or b < 0)  # This will be True, as a is greater than 0
logical_not = not (a < 0)  # This will be True, as a is not less than 0
print(logical_and, logical_or, logical_not)  # This will print the results of the logical operations.
# Example of assignment operators:
c = 20
c += 5  # This will be 25, equivalent to c = c + 5
c -= 10  # This will be 15, equivalent to c = c - 10
c *= 2  # This will be 30, equivalent to c = c * 2
c /= 3  # This will be 10.0, equivalent to c = c / 3
c %= 4  # This will be 2.0, equivalent to c = c % 4
print(c)  # This will print the final value of c after all assignment operations.
# Example of bitwise operators: 
bitwise_and = a & b  # This will be 0, as 10 (1010 in binary) AND 5 (0101 in binary) is 0000
bitwise_or = a | b  # This will be 15, as 10 (1010 in binary) OR 5 (0101 in binary) is 1111
bitwise_xor = a ^ b  # This will be 15, as 10 (1010 in binary) XOR 5 (0101 in binary) is 1111
bitwise_not = ~a  # This will be -11, as NOT 10 (1010 in binary) is 11111111111111111111111111110101 in two's complement
bitwise_left_shift = a << 1  # This will be 20, as shifting 10 (1010 in binary) left by 1 gives 10100
bitwise_right_shift = a >> 1  # This will be 5, as shifting 10 (1010 in binary) right by 1 gives 0101
print(bitwise_and, bitwise_or, bitwise_xor, bitwise_not, bitwise_left_shift, bitwise_right_shift)  # This will print the results of the bitwise operations.
# Example of identity operators:
x = [1, 2, 3]
y = x  # y is a reference to the same list as x
z = [1, 2, 3]  # z is a different list with the same content
is_x_y = (x is y)  # This will be True, as x and y refer to the same object
is_x_z = (x is z)  # This will be False, as x and z are different objects
is_not_x_z = (x is not z)  # This will be True, as x and z are different objects
print(is_x_y, is_x_z, is_not_x_z)  # This will print the results of the identity operations.
# Example of string operators:
str1 = "Hello"
str2 = "World"
str_concat = str1 + " " + str2  # This will be "Hello World", concatenating two strings
str_repeated = str1 * 3  # This will be "HelloHelloHello", repeating the string three times
print(str_concat, str_repeated)  # This will print the concatenated and repeated strings.
# Example of using operators in a simple program:
def calculate_area(length, width):
    return length * width



