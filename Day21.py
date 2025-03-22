# Day 21: Automating Tasks with Python
# - Topics:
# - Learn how to automate tasks using Python scripts.
# - Use os and shutil for file manipulation.
# - Project:
# - Write a Python script that automatically organizes files in a folder by extension (e.g., move .txt files to
# a "TextFiles" folder).


# Importing Modules or Libraries
import os
import shutil


# Simple Format

# Creating a directory
# os.makedirs("Destination_Folder", exist_ok=True)

# shutil.copy("Destination_Folder/File_to_Move.txt","File_to_Move.txt")
# shutil.move("Destination_Folder/File_to_Move.txt","File_to_Move.txt")


# Format using Extension

# path = input("Enter path to organize files: ")
# files =  os.listdir(path)

# for file in files:
#     filename, extension = os.path.splitext(file)

#     extension = extension[1:]
    
#     if os.path.exists(f"{path}/{extension}"):
#         shutil.move(f"{path}/{file}", f"{path}/{extension}/{file}")
#     else:
#         os.makedirs(f"{path}/{extension}")
#         shutil.move(f"{path}/{file}", f"{path}/{extension}/{file}")



# Using the dictionary method

directory = input("Enter hte path of the folder you want to organize its files: ")

file_types = {
    "images" : [".jpg", ".jpeg", ".png", ".webp"],
    "documents": [".docx", ".txt", ".ppx", ".pptx", ".pdf"],
    "videos" : [".mp4", ".wav"],
    "audios" : [".mp3"],
    "Spreadsheets" : [".xls", ".xlsx"],
    "archives" : [".zip", ".rar", ".7zip"]
}

# FUnction to create FOlders to store files based on their 
def create_folders(base_dir, folders):
    for folder in folders:
        folder_path = os.path.join(base_dir,folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
            
            
            
# Function to sort the files into the folders based on their file extension
def organize_files(base_dir, file_types):
    for filename in os.listdir(base_dir):
        file_path = os.path.join(base_dir,filename)
        
        if os.path.isdir(file_path):
            continue
        
        name, ext = os.path.splitext(filename)
        
        for folder,extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(base_dir,folder)
                shutil.move(file_path,target_folder)
                break
            
            
            
            
# Calling both the create_folder function and the organize_files function
create_folders(directory,file_types.keys())
organize_files(directory,file_types)
