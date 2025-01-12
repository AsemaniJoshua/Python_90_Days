# - Topics:
# - Learn about dictionaries (key-value pairs) and sets (unordered collections).
# - Dictionary methods: get(), keys(), values().
# - Project:
# - Create a program that stores user information (name, age) in a dictionary and allows the user to
# retrieve it by providing the name.

# Asking for the username and Age

name = input("Enter your name: \n")
age = int(input("Enter your age: \n"))

user_details = {
    "name": name,
    "age": age
}

new_name = input("Enter the previous name to retrieve your information: \n")

if new_name in user_details.values():
    print(f"Name: {user_details['name']} \n Age: {user_details['age']}")
else:
    print("Name not found")