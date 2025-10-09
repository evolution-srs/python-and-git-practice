# Read CSV files in Pandas
# For VS version
import pandas as pd
import requests
import os # Used for basic file system operations

# The URL of the file to download
file_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

# The name we want to save the file as locally
LOCAL_FILENAME = "addresses.csv"
local_path = "A:\Coursera\1-computer-science\python-and-git-practice\ibm-python-for-data-sc-ai-Dev\module5-API-and-data-collection"

def download_file_synchronously(url, local_path):
    """
    Downloads a file from a URL using the synchronous 'requests' library.
    This replaces the async 'pyfetch' mechanism used in pyodide environments.
    """
    try:
        # Send a GET request to the URL. We use stream=True for potentially large files.
        print(f"Starting download of {url}...")
        response = requests.get(url, stream=True)

        # Raise an HTTPError if the status code is 4xx or 5xx
        response.raise_for_status()

        # Write the content to the local file
        with open(local_path, "wb") as f:
            # Write content in chunks (8KB at a time) to save memory
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Download successful. File saved as: {LOCAL_FILENAME}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during download: {e}")
        # Exit the script if the download fails
        exit(1)


# 1. Execute the synchronous download
download_file_synchronously( file_url, LOCAL_FILENAME)

# 2. Read the downloaded file into a Pandas DataFrame
# Note: The file is now guaranteed to exist locally, just like in the original code.
try:
    df = pd.read_csv(LOCAL_FILENAME, header=None)
    
    print("\n--- DataFrame Loaded Successfully ---")
    print("First 5 rows of the DataFrame:")
    print(df.head())
    
    # Optional: Clean up the downloaded file after use
    # os.remove(LOCAL_FILENAME)
    # print(f"\nCleaned up local file: {LOCAL_FILENAME}")
    
except FileNotFoundError:
    print(f"Error: Could not find the file {LOCAL_FILENAME}. Check download status.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except Exception as e:
    print(f"An unexpected error occurred during file reading: {e}")

# Adding column name to the DataFrame
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

# Selecting a single column
print(df["First Name"])

#Selecting multiple columns
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
print(df)
# Selecting rows using .iloc and .loc
# loc() : loc() is label based data selecting method which means that we have to pass the name of 
# the row or column which we want to select.
# To select the first row
df.loc[0] 
print(df)
# To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]
print(df)

# iloc() : iloc() is a indexed based selecting method which means that we have to pass integer
#  index in the method to select specific row/column.

# To select the 0th,1st and 2nd row of "First Name" column only
df.iloc[[0,1,2], 0]

# Transform Function in Pandas
#import library
import pandas as pd
import numpy as np

#creating a dataframe
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

# Applying the transform function

df = df.transform(func = lambda x : x + 10)
print(df)

#applying the transform function
df = df.transform(func = lambda x : x + 10)
print(df)

# Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.
result = df.transform(func = ['sqrt'])
print(result)