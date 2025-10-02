# 2D Numpy in Python
# Objectives¶

# Operate comfortably with numpy
# Perform complex operations with numpy

# Create a 2D numpy array from a list of lists
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

import numpy as np
b = np.array(a)
print(b)

# Show the numpy array dimensions
print(b.ndim)
# Show the numpy array shape
print(b.shape)
# Show the numpy array size
print(b.size)
# Show the numpy array data type
print(b.dtype)

# Accessing elements in a 2D numpy array
# Access the element at row 1, column 2
print(b[1, 2])
# Access the element at row 2, column 1 
print(b[2, 1])
# Access the element at row 1, column 0
print(b[1, 0])

# Slicing a 2D numpy array
# Slice the first two rows and all columns
print(b[0:2, :])

# Slice all rows and the first two columns
print(b[:, 0:2])

# Slice rows 1 to 2 and columns 1 to 2
print(b[1:3, 1:3])

# Basic operations on a 2D numpy array
# Add 5 to each element
print(b + 5)
# Multiply each element by 2
print(b * 2)
# Divide each element by 2
print(b / 2)

# Subtract 3 from each element
print(b - 3)    
# Square each element
print(b ** 2)
# Compute the square root of each element
print(np.sqrt(b))
# Compute the natural logarithm of each element
print(np.log(b))

# Matrix operations on a 2D numpy array
# Transpose the array
print(b.T)
# Compute the sum of all elements
print(np.sum(b))
# Compute the mean of all elements
print(np.mean(b))

# We can also perform matrix multiplication with the numpy arrays A and B as follows:
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(np.dot(A, B))
# Alternatively, we can use the @ operator for matrix multiplication:
print(A @ B)

# Exercise:
# Consider the following list a, convert it to Numpy Array.
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
b = np.array(a)
print(b)
# Calculate the numpy array size.
print(b.size)
# Calculate the numpy array shape.
print(b.shape)
# Access the element at row 2, column 3.
print(b[2, 3])
# Access all element at row 2.
print(b[2, :])
# Slice the first two rows and all columns.
print(b[0:2, :])
# Slice all rows and the first two columns
print(b[:, 0:2])   

