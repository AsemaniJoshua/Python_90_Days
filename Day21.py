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
