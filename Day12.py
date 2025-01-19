# Day 12: Working with JSON
# - Topics:
# - Learn how to parse and create JSON data using Python’s json library.
# - Understanding JSON format and how it is used in APIs.
# - Project:
# - Create a script that reads a JSON file and prints out specific values based on user input.

# Importing JSON Library
import json
import requests

# people_string = '''
#     {
#         "people":
#             [
#                 {
#                     "name": "Ama",
#                     "age": 12,
#                     "email": "ama@gmail.com",
#                     "has_email": true
#                 },
#                 {
#                     "name": "Kofi",
#                     "age": 15,
#                     "email": "kofi1@gmail.com",
#                     "has_email": false
#                 }
#             ]
#     }
# '''
#
# data = json.loads(people_string)
#
# # print(data)
#
# for person in data['people']:
#     # print(person, "\n")
#     # print(person['name'], person['age'])
#     del person['email']
#
# new_string = json.dumps(data, indent=2)
#
# print(new_string)

# Getting user input
user_input = input("Please enter your name to verify that your information is with us. \n")
user_input = user_input.lower()

# Converting the Json file too Python Object
with open("Information.json","r") as file:
    data = json.load(file)

#  List to store user_names from the JSON file
user_names = []
# Looping through the JSON object to get the name of Users and store the in a list
for info in data['Identification']:
    user_names.append(info['name'])

# Checking if user input is in the list of user_names
if user_input in user_names:
    print("Your information is with us. Here is your details below: \n")

    for user_info in data['Identification']:
        if user_input == user_info['name']:
            print(f"Your name is: {user_info['name']}")
            print(f"You are {user_info['age']} years old")
            print(f"Your email is: {user_info['email']}")

else:
    print("Sorry!. Your information is not with us.")

with open("Information2.json", "w") as file:
    json.dump(data, file, indent=2)



