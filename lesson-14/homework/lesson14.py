#Homework
#1
import json
with open('students.json', 'r') as file:
    data = json.load(file)
    print("Student Details:")
    for key, value in student.items():
        print(f"  {key}: {value}")
    print()  # blank line between students

#2
!pip install requests
import requests

api_key = '33684c78c9ffb7c28de46a8b1a2bc6bc'

city = 'Tashkent'

base_url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    'q': city,
    'appid': api_key,
    'units': 'metric' 
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_desc = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    
    # Print the weather info
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_desc}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error fetching weather data:", response.status_code, response.text)

#3
import json

try:
    with open('books.json', 'r') as f:
        books = json.load(f)
except:
    books = []

title = input("Book title: ")
author = input("Author: ")
year = input("Year published: ")

books.append({"title": title, "author": author, "year": year})

with open('books.json', 'w') as f:
    json.dump(books, f, indent=4)

print("Book added!")

#4
import requests

api_key = 'YOUR_API_KEY' 
movie_title = input("Enter movie title: ")

url = "http://www.omdbapi.com/"
params = {
    'apikey': api_key,
    't': movie_title  
}

response = requests.get(url, params=params)
data = response.json()

if data['Response'] == 'True':
    print(f"Title: {data['Title']}")
    print(f"Year: {data['Year']}")
    print(f"Genre: {data['Genre']}")
    print(f"Director: {data['Director']}")
    print(f"Plot: {data['Plot']}")
    print(f"IMDB Rating: {data['imdbRating']}")
else:
    print("Movie not found!")

#4.2
import requests

api_key = 'YOUR_API_KEY'  

genre_input = input("Enter a movie genre (e.g., Action, Comedy): ").lower()
keyword = "love"  

url = "http://www.omdbapi.com/"
params = {
    'apikey': api_key,
    's': keyword,
    'type': 'movie',
    'page': 1
}

response = requests.get(url, params=params)
data = response.json()

if data.get('Response') == 'True':
    movies = data.get('Search', [])
    for movie in movies:
        details_params = {'apikey': api_key, 'i': movie['imdbID']}
        details_response = requests.get(url, params=details_params)
        details = details_response.json()

        if 'Genre' in details and genre_input in details['Genre'].lower():
            print(f"Recommended movie: {details['Title']} ({details['Year']})")
            print(f"Genre: {details['Genre']}")
            print(f"Plot: {details['Plot']}")
            break
    else:
        print(f"No movies found in genre '{genre_input}'.")
else:
    print("No movies found with that keyword.")
