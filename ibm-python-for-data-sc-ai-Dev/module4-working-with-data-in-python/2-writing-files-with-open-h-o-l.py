
# Writing to a file using 'with' statement

file2='Example2.txt'
with open(file2,'w') as f:
    f.write('Hello World!')
    f.write('\n')
    f.write('This is a test file.')
    f.write('\n')
    f.write('Goodbye!')

with open(file2,'r') as f:
    print(f.read())

# Appending to a file

file1='Example1.txt'
with open(file1,'a') as f:
    f.write('\nAppended line 1.')
    f.write('\nAppended line 2.')

with open(file1,'r') as f:
    print(f.read())
# Writing multiple lines using writelines()

# Additional methods
# It's fairly ineffecient to open the file in a or w and then reopening it in r to read any lines.
#  Luckily we can access the file in the following modes:

# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists. 
# You dont have to dwell on the specifics of each mode for this lab.
with open('Example3.txt','w+') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
    f.write('Line 3\n')
    f.seek(0)  # Move the cursor to the beginning of the file
    print(f.read())
    f.write('Line 4\n')
    f.seek(0)  # Move the cursor to the beginning of the file again
    print(f.read())
    f.write('Line 5\n')
    f.seek(0)  # Move the cursor to the beginning of the file again
    print(f.read())

    # Copy contents of one file to another
with open('Example1.txt','r') as source, open('Example4.txt','w') as dest:
    for line in source:
        dest.write(line)
with open('Example4.txt','r') as f:
    print(f.read())
# Note: Always ensure files are properly closed after operations to prevent data loss or corruption.
# The with statement automatically handles closing the file for you.

# Excercise
# Your local university's Raptors fan club maintains a register of its active members on a .txt document.
# Every month they update the file by removing the members who are not active. You have been tasked with
#  automating this with your Python skills.
# Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each
# of the removed members and append them to the exMem file. Make sure that the format of the original 
# files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
# Run the code block below prior to starting the exercise. The skeleton code has been provided for you.
# Edit only the cleanFiles function

#Run this prior to starting the exercise
from random import randint as rnd

memReg = '/members.txt'
exReg = '/inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)

'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
        #TODO: Open the exMem file in a+ mode

        #TODO: Read each member in the currentMem (1 member per row) file into a list.
        # Hint: Recall that the first line in the file is the header.

        #TODO: iterate through the members and create a new list of the innactive members

        # Go to the beginning of the currentMem file
        # TODO: Iterate through the members list. 
        # If a member is inactive, add them to exMem, otherwise write them into currentMem

        
    
    pass # Remove this line when done implementation


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = '/members.txt'
exReg = '/inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
            
def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

testWrite = "/testWrite.txt"
testAppend = "/testAppend.txt" 
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))
    

