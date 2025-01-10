#Functions and Function arguments, return values, and scope

#Function that takes a number as input and returns the factorial of that number.

# Importing the math class
import math

# Taking user input and convert it to float and then to integer
userNumber = int(float(input("Please enter a number to get the corresponding factorial: ")))

def calculate_factorial(userinput):
    userinput = math.factorial(userinput)
    print("The factorial of the number you entered is:",userinput)

calculate_factorial(userNumber)

