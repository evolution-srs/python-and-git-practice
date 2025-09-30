import urllib.request

# The URL of the file to download
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'

# The name you want to save the file as locally
filename = 'Example1.txt'

# Download the file
urllib.request.urlretrieve(url, filename)

print(f"File '{filename}' downloaded successfully!")
# Output: File 'Example1.txt' downloaded successfully
# Now you can open and read the file as needed
# For example, to read and print the contents of the file:
with open(filename, 'r') as file:
    contents = file.read()
    print(contents)# Output: (Contents of the file will be printed here)

    # 1. Open the file in read mode ('r')
file1 = open('Example1.txt', 'r')

# 2. Read the entire content of the file
file_content = file1.read()

# 3. Print the content
print(file_content)

# 4. Close the file
file1.close()

# 5.Print the file bath 
print(file1.name) # Output: Example1.txt
# 6. Print the file mode
print(file1.mode) # Output: r   

# 7. Print the file type
print(type(file1)) # Output: <class '_io.TextIOWrapper'>

# 8. check if the file is closed
print(file1.closed) # Output: True

with open('Example1.txt', "r") as file1:
    FileContent = file1.read()
    print(FileContent) #output: (Contents of the file will be printed here)
 
print(file1.closed) # Output: True

# Bad practice: Prone to errors if .close() is forgotten
file1 = open('Example1.txt', 'r')
file_content = file1.read()
print(file_content)

# CRITICAL: If an error happens before this line, the file remains open!
file1.close()

# Good practice: The file is guaranteed to close
with open('Example1.txt', 'r') as file2:
    file_content = file2.read()
    print(file_content)

# File is automatically closed when indentation ends,
# even if an error occurred inside the 'with' block.

# Read first four characters

with open('Example1.txt', "r") as file1:
    print(file1.read(4))

with open('Example1.txt', "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9)) 

with open('Example1.txt', "r") as file1:
    print("first line: " + file1.readline())
    print("second line: " + file1.readline())
    print("third line: " + file1.readline())    

    # Iterate through the lines

with open("Example1.txt", "r")as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Print the first line

with open("Example1.txt", "r") as file1:
    FileasList = file1.readlines()
    print(FileasList[0])

    