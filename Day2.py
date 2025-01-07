# Taking user input and calculating them
import string
from xmlrpc.client import Boolean

# To convert a value to string, use str()
# To convert a value to integer, use int()
# To convert a value to float, use float()
# To convert a value to Boolean, use bool()
from datetime import datetime
#Taking User Input
Name = input("Please Enter your Name: ")
#Print User Input
print("Hello " + Name + ".")
#Taking User Input
Age = int(input("Please Enter your Age: "))
#Getting current year
Current_Year = datetime.now().year
#Calculating the year the user was born
Year_born = Current_Year - Age

#Displaying The year the user was born
print("You were born in " + str(Year_born))
