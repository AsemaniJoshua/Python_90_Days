# Day 16: Web Scraping with BeautifulSoup
# - Topics:
# - Introduction to web scraping using BeautifulSoup and requests.
# - Parsing HTML and extracting data.
# - Project:
# - Create a program that scrapes a website (e.g., news headlines from a news site) and displays the
# results.

# Am0241626471

# Importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Link to scrape
url = "https://e-learn-site.vercel.app/"
items = []

def scrape_webpage(url):
    
    # Error Handling
    
    try:
        page = requests.get(url)
        
        # Using Beautiful Soup to parse the HTML
        soup = BeautifulSoup(page.content, "html.parser")
        all_courses = soup.find_all("div", class_="course-card")
        
        
        for course in all_courses:
            item = {}
            item["image"] = course.find("img")
            item["image_source"] = course.find("img")["src"]
            item["title"] = course.find("h3").text
            item["description"] = course.find("p").text
            item["price"] = course.find("p", class_="price").text
            item["link"] = course.find("a")["href"]
            
            items.append(item)
            
        for item in items:
            print("\n")
            print(f"Title: {item['title']}")
            print(f"Description: {item['description']}")
            print(f"Price: {item['price']}")
            print(f"Link: {item['link']}")
            print("\n")
        # print(soup.prettify())
        
    except Exception as e:
        print(f"An error occurred: {e}")

files = pd.DataFrame(items)
files.to_csv("courses.csv")
files.to_excel("courses.xlsx")

        
# Calling the function
scrape_webpage(url)

