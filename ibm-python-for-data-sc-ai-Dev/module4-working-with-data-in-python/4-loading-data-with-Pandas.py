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

from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

async def load_data():
    response = await pyfetch(filename)
    if response.status == 200:
        csv_text = await response.text()
        from io import StringIO
        df = pd.read_csv(StringIO(csv_text))
        return df

async def main():
    await download(filename, "Product-sales.csv")
    df = pd.read_csv("Product-sales.csv")
    return df

# To run the async main function and get the dataframe:
# import asyncio
# df = asyncio.run(main())
