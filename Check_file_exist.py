# importing os module
import os

# Assigning file path to 'path' Variables
path='/home/lohith/Data/Superstore.csv'

# define a function to check file exists or not
def check_file_exists(path):
    try:
        if os.path.exists(path):            
            return path                      
        else:
            return None
    except:
        return None
    
# Call main function.
if __name__ == "__main__":
    # calling check_file_exists function, return value will be stored in file_path    
    file_path = check_file_exists(path)
    # if the return value is not None, then file exists
    if file_path is not None:
        print(f"File exists, it's path is: {file_path}")
    else:
        print("File not found")