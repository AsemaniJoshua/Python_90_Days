# Day 13: Using External Libraries: Requests
# - Topics:
# - Learn how to make HTTP requests with the requests library.
# - Understanding HTTP methods: GET, POST.
# - Project:
# - Create a Python script that fetches data from a public API (e.g., OpenWeatherMap) and displays the
# weather

# from io import BytesIO

# Import Request Library
import requests
# from pillow import Image

special = "5321eee27d3d32a29f33655bcfcdcbb7"

# Function to get weather
def get_weather_information(city):

#  Getting the weather information using the city
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={special}')
    data = response.json()

    # # Getting the icon
    # icon_code = data['weather'][0]['icon']
    # weather_icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    # r = requests.get(weather_icon_url)
    # img_data = r.content
    # image = Image.open(BytesIO(img_data))
    #
    # # Showing Icon
    # Image.show()

    # Displaying weather Info
    print("\nHere is your weather info: \n")
    print(f"Weather: {data['weather'][0]['main']}")
    print(f"Description: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}")
    print(f"Humidity: {data['main']['humidity']}")
    print(f"Wind Speed: {data['wind']['speed']}")
    print(f"The country of your city is {data['sys']['country']}")

    # print(data)


# Alerting user to enter a city to check it's weather
city = input("Enter a city to get the weather information. \n")

# Calling the function
get_weather_information(city)