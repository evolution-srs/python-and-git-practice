# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this 
# time using the enumerate function to check if an element is in an even position or an odd position.
def skip_elements(elements):
    return [element for index, element in enumerate(elements) if index % 2 == 0]
# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. 
# Hint: remember that list and range counters start at 0 and end at the limit minus 1.
def odd_numbers(n):
    return [x for x in range(1, n+1) if x % 2 == 1]
print(odd_numbers(5))      # [1, 3, 5]
# odd_number function returns a list of odd numbers between 1 and n, inclusively.
def odd_numbers(n):
    return [x for x in range(1, n+1) if x % 2 == 1]