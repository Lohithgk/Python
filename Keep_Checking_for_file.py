import os
import time

# Assigning file path to 'path' Variables
path='/home/lohith/Data/Superstore.csv'

# assign a variable to store maximum number of attempts, sleep time in seconds
maximum_attempts: int = 10
sleep_time: int = 1 #seconds

# define a function to check file exists or not
def check_file_exists(path):
    try:
        # loop for maximum number of attempts until file is found
        for attempt in range(maximum_attempts):
            # checking file exists or not, if exists return the path
            if os.path.exists(path):
                return path
            else:
                # Adding a delay between attempts
                time.sleep(sleep_time)  
        # return None if maximum number of attempts are exceeded
        return None 
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
# Call main function.
if __name__ == "__main__":
    # calling check_file_exists function, return value will be stored in file_path    
    file_path = check_file_exists(path)
    # if the return value is not None, then file exists
    if file_path is not None:
        print(f"File exists, it's path is: {file_path}")
        exit()
    else:
        print("File not found")
        exit()