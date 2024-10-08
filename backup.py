import schedule
import time
import os
import shutil
import datetime

source_dir = r"C:\Users\zaboc\OneDrive\Pictures\Screenshots"
destination_dir = "C:/Users/zaboc/Desktop/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")
        
copy_folder_to_directory(source_dir, destination_dir)

#schedule.every().day.at("5:00").do(copy_folder_to_directory)
