# Method 1:- write the data to the file
myfile = open(file='file2.txt', mode='w')
myfile.write("lohith")
myfile.close()

# Method 1:- append the data to file
myfile = open(file='file2.txt', mode='a')
myfile.write("\nlohith")
myfile.close()