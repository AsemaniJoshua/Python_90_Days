# Regular Expression.

# importing the re module

import re


# Taking user input

userinput = input("Enter your email: \n")

pattern = "\w+@\w+\.com"

if re.search(pattern, userinput):
    print("Valid Email Address ")
else:
    print("Invalid Email Address")