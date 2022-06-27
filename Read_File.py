# open() - open a any file using open function in different mode
# r- Read, w-write, a - append, r+ - both read and write

# Method 1:- Read the content of the file.
myfile = open(file='file1.txt', mode='r')
print(myfile.read())
myfile.close()

# Method 2:- Read the content of the file.
with open(file='file1.txt', mode='r') as myfile:
    print(myfile.read())

# Method 1:- Read the content of the file.
myfile = open(file='file1.txt', mode='r')
print(myfile.readline())
myfile.close()