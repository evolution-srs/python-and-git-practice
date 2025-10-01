# Selecting Data in a DataFrame

# Use Pandas Library to create DataFrame and Series
# Locate data in the DataFrame using loc() and iloc() functions
# Use slicing

# 1- Pandas is a powerful library for data manipulation and analysis in Python. 
# It provides data structures like DataFrame and Series that make it easy to work with structured data.

# 2- A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure
#  with labeled axes (rows and columns).
# A Pandas DataFrame will be created by loading the datasets from existing storage.
# Storage can be SQL Database, CSV file, Excel file, etc.
# It can also be created from the lists, dictionaries, and from a list of dictionaries.

# 3- A Series is a one-dimensional labeled array capable of holding any data type.
# An array of actual data.
# An associated array of indexes or data labels.

# The index is used to access individual data values. You can also get a column of a dataframe as a Series.
#  You can think of a Pandas series as a 1-D dataframe.

# Importing the pandas library
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)

# Coloumn selection using column name
print(df['Name'])  # Selecting the 'Name' column    

# Access multiple columns
print(df[['Name', 'City']])  # Selecting 'Name' and 'City'
print(type(df[['Name', 'City']]))  # DataFrame  
print(type(df['Name']))  # Series   

# Locating data in the DataFrame using loc() and iloc() functions
# loc() is label-based, which means that you have to specify the name of the rows and columns 
# that you want to filter out.
print(df.loc[0, 'Name'])  # Accessing the value at row index 0 and column 'Name'
print(df.loc[1:2, 'Name'])  # Accessing the values from row index 1 to 2 in column 'Name'
print(df.loc[:, 'Name'])  # Accessing all rows in column 'Name'
print(df.loc[:, ['Name', 'City']])  # Accessing all rows in columns 'Name' and 'City' integer position.

#  iloc() is integer index-based, so you have to specify rows and columns by their integer index.
print(df.iloc[0, 0])  # Accessing the value at row index 0 and column index 0
print(df.iloc[1:3, 0])  # Accessing the values from row index 1 to 2 in column index 0
print(df.iloc[:, 0])  # Accessing all rows in column index 0
print(df.iloc[:, [0, 2]])  # Accessing all rows in columns index 0 and 2
print(type(df.iloc[:, [0, 2]]))  # DataFrame
print(type(df.iloc[:, 0]))  # Series

# Slicing
# Slicing in Pandas is similar to slicing in Python lists. You can use the colon (:) operator to specify 
# a range of rows or columns.
print(df[0:2])  # Accessing rows from index 0 to 1  
print(df['Name'][0:2])  # Accessing 'Name' column for rows from index 0 to 1
print(df[['Name', 'City']][0:2])  # Accessing 'Name' and 'City' columns for rows from index 0 to 1
print(type(df[['Name', 'City']][0:2]))  # DataFrame
print(type(df['Name'][0:2]))  # Series