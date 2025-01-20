# Day 14: Working with APIs
# - Topics:
# - Learn how to send requests and handle JSON responses from APIs.
# - Authentication methods for APIs (e.g., using API keys).
# - Project:
# - Write a program that interacts with the GitHub API to fetch user data (like profile information).


# Importing the request library
import requests


# Taking user input
username = input("Enter your username on github \n")

def get_user_info(username):
    # Getting user info using the github API
    response = requests.get(f'https://api.github.com/users/{username}')
    data = response.json()
    # print(data)

#     Displaying user info
    print("\nHere is your Github Information: \n")

#     Name
    print(f"Name: {data["name"]} ")

    # Created Date
    print(f"The date and time you created your account was: {data["created_at"]}")

    # Number of public repo
    print(f"You have {data["public_repos"]} public repository")

    # Link to your profile
    print(f"The link to your profile is: {data["html_url"]}")

    #     Followers
    print(f"Followers: {data["followers"]}")

 #     Following
    print(f"Following: {data["following"]} \n")


get_user_info(username)