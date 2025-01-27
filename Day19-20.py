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

# Getting key for encryption from a file
with open("myKey.key", "rb") as read_key:
    key = read_key.read()
    
# Reading from a file to encrypt
with open("Fernet_ENCRYPT.txt", "r") as original_file:
    original = original_file.read()

# Encoding the content of the file
original = original.encode('utf-8')

# Encrypting the file content
encrypted_file = Fernet.encrypt(key, original)

# Writing the encrypted content to a file
with open("Encrypted_File.txt", "wb") as write_encrypted_content:
    write_encrypted_content.write(encrypted_file)
    
print("Done with Encrypting file...... ")



