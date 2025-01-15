# Day 10: Introduction to Libraries
# - Topics:
# - Introduction to Python libraries: how to install and use them (using pip).
# - Using built-in libraries like os, sys, math.
# - Project:
# - Write a Python script that calculates the square root of a number using the math library.

# Importing the math library
import math

# Getting a number from the user
number = float(input("Enter a number (it can be either whole numbers or decimal point number): \n"))

sqrt_of_number = math.sqrt(number)

print(f"The square root of the number you entered is {sqrt_of_number}")
