# Day 19-20: Introduction to Encryption
# - Topics:
# - Learn basic encryption concepts using the cryptography library.
# - Symmetric vs. asymmetric encryption.
# - Project:
# - Create a simple encryption/decryption tool using the cryptography library (e.g., AES encryption)

# Encryption using Fernet
from cryptography.fernet import Fernet

# # Generating a key
# keys = Fernet.generate_key()

# # Writing the key to a file
# with open("myKey.key", "wb") as write_key:
#     write_key.write(keys)

# *************************************** Encrypting a File *********************************************

# # Getting key for encryption from a file
# with open("myKey.key", "rb") as read_key:
#     key = read_key.read()
    
# # Reading from a file to encrypt
# with open("Fernet_ENCRYPT.txt", "r") as original_file:
#     original = original_file.read()

# # Encoding the content of the file
# original = original.encode('utf-8')

# # Creating instance of Fernet with our key
# f = Fernet(key)

# # Encrypting the file content
# encrypted_file = f.encrypt(original)

# # Writing the encrypted content to a file
# with open("Encrypted_File.txt", "wb") as write_encrypted_content:
#     write_encrypted_content.write(encrypted_file)
    
# print("Done with Encrypting file...... ")


# ***************************** Decrypting a File ****************************************

# # Reading the key from the file
# with open("myKey.key", "rb") as read_key:
#     key = read_key.read()

# # Reading the encrypted file
# with open("Encrypted_File.txt", "rb") as encrypted_file:
#     encrypted = encrypted_file.read()

# # Creating instance of Fernet with our key
# f = Fernet(key)

# # Decrypting the file content
# decrypted_file = f.decrypt(encrypted)

# # Writing the decrypted content to a file
# with open("Decrypted_File.txt", "w") as write_decrypted_content:
#     write_decrypted_content.write(decrypted_file.decode('utf-8'))




# ************************************** Encryption with AES *************************************
# Importing the required libraries
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# Generating a random key
key = get_random_bytes(16)

# Creating a function for encryption
def encrypt(message, key):
    # Creating an instance of AES
    cipher = AES.new(key, AES.MODE_EAX)
    
    # Encrypting the message
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message)
    
    # Writing the encrypted message to a file
    with open("Encrypted_AES.txt", "wb") as write_encrypted_content:
        write_encrypted_content.write(ciphertext)
    return nonce, ciphertext, tag


# Function to decrypt the message
def decrypt(nounce, ciphertext, tag, key):
    # Creating an instance of AES
    cipher = AES.new(key, AES.MODE_EAX, nounce)
    
    # Decrypting the message
    decrypted = cipher.decrypt(ciphertext)
    
    # Verifying the tag
    try:
        cipher.verify(tag)
        # Writing the decrypted message to a file
        with open("Decrypted_AES.txt", "w") as write_decrypted_content:
            write_decrypted_content.write(decrypted.decode('utf-8'))
        return decrypted.decode('utf-8')
        
    except:
        # If the tag is not verified
        print("The tag is not verified")
        return False



# Calling the encryption function
nonce, ciphertext, tag = encrypt(b"This is a secret message", key)

# Calling the decryption function
decrypted_message = decrypt(nonce, ciphertext, tag, key)

# Printing the encrypted message
print(f"Encrypted message: {ciphertext}")

# Printing the decrypted message
print(f"Decrypted message: {decrypted_message}")

print("Done with Encryption and Decryption......")