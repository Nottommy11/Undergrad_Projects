import requests

# https://youtu.be/Oz3W-LKfafE?t=1829
# https://openweathermap.org/current
# My API Key: 12f82b9548263b20374446fcb4c4d1dc

API_KEY = "12f82b9548263b20374446fcb4c4d1dc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(((data["main"]["temp"] - 273.15) * (9 / 5) + 32), 2)
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} fahrenheit")
else:
    print("An error occurred.")
