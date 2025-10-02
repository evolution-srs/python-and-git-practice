# 1D Numpy in Python - Hands on Lab
# Objective:
#1- Import and use the numpy library
#2- Perform basic operations on 1D numpy arrays
#3- Understand and manipulate array attributes
#4- Perform indexing and slicing on 1D numpy arrays

# Numpy is a powerful library in Python used for numerical computing.
# It provides support for arrays, matrices, and many mathematical functions to operate on these 
# data structures.
# Numpy stands for "Numerical Python" and is widely used in data science, machine learning,
# and scientific computing due to its efficiency and ease of use.
# To use numpy, you first need to install it using pip if you haven't already:
# pip install numpy
# Once installed, you can import it in your Python script as follows:
import numpy as np

# arry object in numpy is called ndarray (n-dimensional array)
# You can create a 1D numpy array using the np.array() function:
array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d)

# Check numpy version
print(np.__version__)

# Check array type
print(type(array_1d))   
# check the data type of the array elements
print(array_1d.dtype)
# Basic Operations on 1D Numpy Arrays
# You can perform various operations on 1D numpy arrays, such as addition, subtraction, multiplication, and division.
array_2d = np.array([10, 20, 30, 40, 50])
result = array_1d + array_2d
print(result)
result = array_1d - array_2d
print(result)
result = array_1d * array_2d
print(result)
result = array_1d / array_2d
print(result)
# You can also perform mathematical functions like sum, mean, and standard deviation.
print(np.sum(array_1d))
print(np.mean(array_1d))
print(np.std(array_1d))
print(np.var(array_1d))
print(np.min(array_1d))
print(np.max(array_1d))

# Array Attributes and Methods
# Numpy arrays have several attributes that provide information about the array.
print(array_1d.shape)  # Shape of the array
print(array_1d.size)   # Total number of elements in the array
print(array_1d.ndim)  # Number of dimensions of the array
# You can also use methods to manipulate the array, such as reshaping and flattening.
reshaped_array = array_1d.reshape(5, 1)  # Reshape to 5 rows and 1 column
print(reshaped_array)
flattened_array = reshaped_array.flatten()  # Flatten back to 1D
print(flattened_array)  

#  Indexing and Slicing
# You can access elements in a 1D numpy array using indexing and slicing.   
print(array_1d[0])  # First element 
print(array_1d[2])  # Third element
print(array_1d[-1]) # Last element
print(array_1d[1:4]) # Elements from index 1 to 3
print(array_1d[:3])  # First three elements
print(array_1d[2:])  # Elements from index 2 to the end

#  You can also use boolean indexing to filter elements based on a condition.
filtered_array = array_1d[array_1d > 2]  # Elements greater than 2
print(filtered_array)

# Mathematical functions:
print(np.sqrt(array_1d))  # Square root of each element
print(np.exp(array_1d))   # Exponential of each element
print(np.log(array_1d))   # Natural logarithm of each element
print(np.sin(array_1d))   # Sine of each element (in radians)
print(np.cos(array_1d))   # Cosine of each element (in radians)
print(np.tan(array_1d))   # Tangent of each element (in radians
print(np.round(array_1d, 2))  # Round each element to 2 decimal places
print(np.floor(array_1d))     # Floor of each element
print(np.ceil(array_1d))      # Ceiling of each element
# Linspace and arange:
linspace_array = np.linspace(0, 1, 5)  # 5 evenly spaced values between 0 and 1
print(linspace_array)
arange_array = np.arange(0, 10, 2)    # Values from 0 to 10 with a step of 2
print(arange_array)

# Statistical functions:
print(np.median(array_1d))  # Median of the array
print(np.percentile(array_1d, 25))  # 25th percentile
print(np.percentile(array_1d, 75))  # 75th percentile
print(np.corrcoef(array_1d, array_2d))  # Correlation coefficient between two arrays
print(np.cov(array_1d, array_2d))       # Covariance matrix between two arrays

# Sorting and searching:
sorted_array = np.sort(array_1d)  # Sort the array
print(sorted_array)
indices = np.argsort(array_1d)    # Indices that would sort the array
print(indices)
print(np.where(array_1d > 2))     # Indices of elements greater than 2
print(np.unique(array_1d))        # Unique elements in the array
# Copying and viewing:
array_copy = array_1d.copy()      # Create a copy of the array  
print(array_copy)
array_view = array_1d.view()      # Create a view of the array  
print(array_view)
# Modifying elements:
array_1d[0] = 10                   # Modify the first element
print(array_1d) 
array_1d[1:3] = [20, 30]          # Modify elements from index 1 to 2
print(array_1d)

# Exercise:
u = np.array([1, 0])
v = np.array([0, 1])
z = np.array([2, 4])

# u-v
print(u - v)
# u+v
print(u + v)
# u.v (dot product)
print(np.dot(u, v))
# z*2
print(z * 2)

#Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1]. Cast both lists to a numpy array 
# then multiply them together:
list1 = [1, 2, 3, 4, 5]
list2 = [1, 0, 1, 0, 1]
array1 = np.array(list1)
array2 = np.array(list2)
result = array1 * array2
print(result)

# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    plt.grid()#add grid
    plt.show()#show the plot

# Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. Then, plot the arrays as vectors 
# using the fuction Plotvec2 and find their dot product:
a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print(np.dot(a, b))

# Convert the list [1, 0] and [0, 1] to numpy arrays a and b. Then, plot the arrays as vectors using 
# the function Plotvec2 and find their dot product:
a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print(np.dot(a, b)) 
#Convert the list [1, 1] and [0, 1] to numpy arrays a and b. Then plot the arrays as vectors 
# using the fuction Plotvec2 and find their dot product:
a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print(np.dot(a, b))
