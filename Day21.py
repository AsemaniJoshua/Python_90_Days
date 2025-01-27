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

# Creating a directory
# os.makedirs("Destination_Folder", exist_ok=True)

shutil.copy("Destination_Folder/File_to_Move.txt","File_to_Move.txt")



