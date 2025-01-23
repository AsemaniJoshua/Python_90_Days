# Day 18: Introduction to Cryptography
# - Topics:
# - Introduction to hashing with the hashlib library.
# - Hashing algorithms: MD5, SHA1, SHA256.
# - Project:
# - Write a Python script that hashes a user’s password and compares it to a known hash.


# Importing the hashlib library
import hashlib

# defining a default password
default_password = "amazingGRACE"

# Taking user input to compare with the hash of the default password.
user_input = input("Enter a password to check the validity : \n")

# Function to hash the default password
def hash_default(default_password):
    h = hashlib.new("SHA256")
    h.update(default_password.encode())
    return h.hexdigest()


# Function to hash the user input
def hash_user_input(user_input):
    h = hashlib.sha256()
    h.update(user_input.encode())
    return h.hexdigest()

# A variable to store the hash value of the default password
hashed_default_password = hash_default(default_password)

# A variable to store the hash of the user input
hashed_user_input = hash_user_input(user_input)

# Comparing if the hashes are the same or not.
if hashed_default_password == hashed_user_input :
    print("\nThe hash of the default password is equal to the hash of the user input.")
    print("Congratulation !!! 🎉🎉🎉\n")
    
else:
    print("\nThe hash of the default password is not equal to the hash of the user input.")
    print("Sorry !!! 😭😭😭\n")
 