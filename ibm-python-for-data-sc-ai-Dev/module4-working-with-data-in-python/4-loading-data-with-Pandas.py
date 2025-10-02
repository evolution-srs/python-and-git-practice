# Loading Data with Pandas

# Use Pandas to access and view data

# The table has one row for each product and several columns.

# OrderID: A unique identifier for each order
# Product: The name of the product purchased
# Category: The category to which the product belongs (e.g., Electronics, Furniture, Stationery)
# Quantity: The number of units purchased for that product
# Price: The price per unit of the product
# Total: The total cost for the product (calculated as Quantity × Price)
# OrderDate: The date when the order was placed
# CustomerCity: The city where the customer resides

# Import the pandas library
import pandas as pd

# Read data from CSV file

# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv'
# df = pd.read_csv(csv_path)

# Read data from Excel file
import pandas as pd

# The URL to the Excel file
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'

try:
    # Read data directly from the URL using pandas.read_excel()
    df = pd.read_excel(xlsx_path)

    print("Excel data loaded successfully!")
    print(df.head()) # Display the first few rows to verify

except ImportError:
    # A common issue with Excel is missing an engine library
    print("Error: The 'openpyxl' or 'xlrd' library is likely missing.")
    print("Please install the required engine by running: pip install openpyxl")
except Exception as e:
    print(f"An error occurred while loading the data: {e}") # Display the first few rows of the DataFrame

# Access the column Quantity and assign it a new dataframe x:
x = df[['Quantity']]

# Viewing Data and Accessing Data:

# 1- Get the column as a series
y = df['Product']

# 2- Get the column as a dataframe
y = df[['Product']]

# 3-Access to multiple columns
y = df[['Product','Category', 'Quantity']]
print(y.head())

# 4- One way to access unique elements is the iloc method, where you can access the 1st row and 
# the 1st column as follows:
# Access the value on the first row and the first column

df.iloc[0, 0]
# Access the value on the second row and the first column
df.iloc[1, 0]

# Access the value on the first row and the third column
df.iloc[0, 2]
# Access the value on the second row and the third column
df.iloc[1, 2]

# 5- You can access the column using the name as well, the following are the same as above:
# Access the column using the name
df.loc[0, 'OrderID']
df.loc[1, 'OrderID']

# 6- You can perform slicing using both the index and the name of the column:
# Access the first 3 rows of the first column the dataframe
df.iloc[0:3, 0]
# Access the first 3 rows of the first column the dataframe
#  Slicing the dataframe using name
df.loc[0:2, 'OrderID':'Category']

# Use a variable q to store the column Price as a dataframe
q=df[['Price']]
print(q.head())

# Assign the variable q to the dataframe that is made up of the column Product and Category:
q = df[['Product', 'Category']]
print(q.head()) 

# Access the 2nd row and the 3rd column of df:
df.iloc[1, 2]

# Use the following list to convert the dataframe index df to characters and assign it to df_new; 
# find the element corresponding to the row index a and column 'CustomerCity'. 
# Then select the rows a through d for the column 'CustomerCity'
new_index = ['a', 'b', 'c', 'd', 'e']
df.index = new_index
df_new = df
print(df_new)
print(df_new.loc['a', 'CustomerCity'])
print(df_new.loc['a':'d', 'CustomerCity'])  
