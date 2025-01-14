# Day 9: Error Handling
# - Topics:
# - Learn how to use try, except, and finally for error handling.
# - Handling specific exceptions like ValueError, FileNotFoundError.
# - Project:
# - Create a program that takes user input for a number and catches errors if the user inputs something
# invalid (non-integer).

def error_handling():
    try:
        user_input = int(input("Enter a number: \n"))
        print(f"You entered: {user_input}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("This code will run no matter what.")

error_handling()