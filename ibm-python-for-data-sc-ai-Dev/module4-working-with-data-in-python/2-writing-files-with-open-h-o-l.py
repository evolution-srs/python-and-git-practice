
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