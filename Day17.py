# Day 17: HTML and HTTP Basics
# - Topics:
# - Understanding HTML structure and HTTP request/response cycle.
# - Inspecting web traffic using browser dev tools.
# - Project:
# - Build a simple HTTP request handler in Python to fetch and display the content of a webpage

# importing the requests library
import requests

# Function to get the HTML content of a webpage
def get_html(url):
    # Error handling using try
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        

# Printing the HTML content
print(get_html("https://e-learn-site.vercel.app/"))
    
    
    
