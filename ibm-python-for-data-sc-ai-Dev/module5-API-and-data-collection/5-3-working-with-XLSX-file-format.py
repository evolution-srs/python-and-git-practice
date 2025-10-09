# Use Python to load the xlsx file and define the name
import pandas as pd

# for Web version un comment the following:
# Not needed unless you're running locally
# import urllib.request
# urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")

# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

#async def download(url, filename):
#    response = await pyfetch(url)
#    if response.status == 200:
#       with open(filename, "wb") as f:
#          f.write(await response.bytes())

#await download(filename, "file_example_XLSX_10.xlsx")

#df = pd.read_excel("file_example_XLSX_10.xlsx") 
# print(df)

# for VS
import pandas as pd
import urllib.request
import os

# Define the URL of the Excel file
file_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"
local_filename = "file_example_XLSX_10.xlsx"

print(f"Starting download of '{local_filename}' from URL...")

try:
    # Use urllib.request.urlretrieve to synchronously download the file
    # This is the standard way to download files in a local Python environment.
    urllib.request.urlretrieve(file_url, local_filename)
    print("Download complete. File saved locally.")
    
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(local_filename)
    
    print("\nSuccessfully loaded DataFrame:")
    # Display the first 5 rows to verify the data
    print(df.head())
    
    # Optional: Clean up the downloaded file after reading if desired
    os.remove(local_filename)
    print(f"\nCleaned up local file: {local_filename}")

except Exception as e:
    print(f"An error occurred: {e}")
 
 # Working with xml.etreeElementTree

import xml.etree.ElementTree as ET

# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
import urllib.request
import xml.etree.ElementTree as ET
import os

# Define the URL and the local filename
file_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"
local_filename = "Sample-employee-XML-file.xml"
output_filename = "processed_employee_data.xml"

print(f"Starting download of '{local_filename}'...")

try:
    # Synchronously download the file using the standard Python library
    urllib.request.urlretrieve(file_url, local_filename)
    print("Download complete. File saved locally.")
    
    # --- XML Parsing Example ---
    
    # 1. Parse the XML file
    tree = ET.parse(local_filename)
    root = tree.getroot()
    
    print("\nSuccessfully parsed XML document.")
    print(f"Root tag: {root.tag}")
    print(f"Number of direct children (employees): {len(root)}")
    
    # 2. Iterate through all 'employee' elements and print their first name
    print("\nListing first names of all employees:")
    for employee in root.findall('employee'):
        first_name = employee.find('firstname').text
        print(f" - {first_name}")

    # 3. Corrected way to save the ElementTree object (the whole document)
    print(f"\nSaving the entire parsed tree to '{output_filename}'...")
    
    # The ElementTree object (tree) has a built-in .write() method.
    # It takes the file path or a file handle as an argument.
    with open(output_filename, "wb") as output_file:
        # Use tree.write() to correctly serialize the XML structure to the file
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
        
    print(f"File successfully written: '{output_filename}'")


except Exception as e:
    print(f"An error occurred during download, parsing, or saving: {e}")
    
finally:
    # Optional: Clean up the downloaded file
    # if os.path.exists(local_filename):
    #     os.remove(local_filename)
    #     print(f"\nCleaned up local file: {local_filename}")
    pass


# Reading with xml.etree.Element.tree and Pandas

import urllib.request
import xml.etree.ElementTree as ET
import os
import pandas as pd # <-- Added pandas import

# Define the URL and the local filename
file_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"
local_filename = "Sample-employee-XML-file.xml"
output_filename = "employee_data.csv" # Changed output to CSV, which is typical for DataFrames

print(f"Starting download of '{local_filename}'...")

try:
    # Synchronously download the file using the standard Python library
    urllib.request.urlretrieve(file_url, local_filename)
    print("Download complete. File saved locally.")
    
    # --- XML Parsing and DataFrame Conversion ---
    
    # 1. Parse the XML file and get the root
    tree = ET.parse(local_filename)
    root = tree.getroot()
    
    print("\nSuccessfully parsed XML document.")
    print(f"Root tag: {root.tag}")
    
    # Define the columns and initialize a list to hold the extracted data
    columns = ["firstname", "lastname", "title", "division", "building", "room"]
    employee_data = []

    # 2. Iterate through each 'employee' node and extract data
    print("\nExtracting data and building employee records...")
    # Use root.findall('employee') or just root if 'employee' is the direct child of the root
    for node in root.findall('employee'): 
        record = {
            "firstname": node.find("firstname").text,
            "lastname": node.find("lastname").text,
            "title": node.find("title").text,
            "division": node.find("division").text,
            "building": node.find("building").text,
            "room": node.find("room").text
        }
        employee_data.append(record)
    
    # 3. Create the DataFrame efficiently from the list of dictionaries
    df = pd.DataFrame(employee_data, columns=columns)
    
    print("\nSuccessfully created DataFrame from XML data.")
    print("DataFrame Head:")
    print(df.head())

    # 4. Save the DataFrame to a new file (CSV or Excel)
    print(f"\nSaving DataFrame to '{output_filename}'...")
    df.to_csv(output_filename, index=False)
    print(f"File successfully written: '{output_filename}'")


except Exception as e:
    print(f"An error occurred during download, parsing, or saving: {e}")
    
finally:
    # Optional: Clean up the downloaded file
     if os.path.exists(local_filename):
         os.remove(local_filename)
         print(f"\nCleaned up local file: {local_filename}")
pass

# Reading xml using pandas.read_xml
# Herein xpath we mention the set of xml nodes to be considered for migrating  to the dataframe which in this case is details node under employees.
df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 