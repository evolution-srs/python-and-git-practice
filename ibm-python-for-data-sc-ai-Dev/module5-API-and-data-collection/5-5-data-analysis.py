# see the scenario in the jupyter file:

# Import pandas library
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

# For local execution, use requests library for synchronous download
import requests
import os

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

download(filename, "diabetes.csv")
df = pd.read_csv("diabetes.csv")

# After reading the dataset, we can use the dataframe.head(n) method to check the top n rows of
#  the dataframe, where n is an integer. Contrary to dataframe.head(n), dataframe.tail(n) will show you the bottom n rows of the dataframe.

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)
print(df)

# To view the dimensions of the dataframe, we use the .shape parameter.
print(df.shape)

# **Statistical Overview of dataset**
# This method prints information about a DataFrame including the index dtype and columns, 
# non-null values and memory usage.

df.info()
df.describe()

# Identify and handle missing values
missing_data = df.isnull()
missing_data.head(5) 
# "True" stands for missing value, while "False" stands for not missing value.

# Count missing value in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    

# Visualization:
# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
labels= 'Not Diabetic','Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()