#Importing necessary modules
import os
import time
import datetime
import shutil


#Consts
path = r'Insert directory here'
x = 0 

today = datetime.datetime.now() #Get todays date and convert to string
today_converted = time.strptime(today.strftime("%d-%m-%Y"), "%d-%m-%Y") #Parse string for easier comparison

list_subdirs = [f.path for f in os.scandir(path) if f.is_dir()] #List all directories present in specified path
list_subdir_name = [f.name for f in os.scandir(path) if f.is_dir()]

for x, dir_path in enumerate(list_subdirs):
    try:
        #Get creation time and convert to datetime
        creation_time = os.path.getctime(dir_path)
        converted_date = datetime.datetime.fromtimestamp(creation_time)
        
        #Calculate the difference in days
        days_difference = (today - converted_date).days
        
        if days_difference > 14: #Checks for folders older than the specified integer
            print(f"Folder {list_subdir_name[x]} is older than 14 days")
            
            #Confirmation of the deletion
            try:
                shutil.rmtree(dir_path)  #Deletes the folder
                print(f"Folder {list_subdir_name[x]} has been deleted successfully.")
            except Exception as delete_error:
                print(f"Error deleting folder {list_subdir_name[x]}: {delete_error}")
        else:
            print(f"Folder {list_subdir_name[x]} is not older than 14 days")
        
    except Exception as e:
        print(f"Error processing folder {list_subdir_name[x]}: {e}")
