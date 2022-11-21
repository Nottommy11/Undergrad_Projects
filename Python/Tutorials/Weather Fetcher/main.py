import requests

# https://youtu.be/Oz3W-LKfafE?t=1829
# https://openweathermap.org/current

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

api_key = input("Enter your key: "
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={api_key}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(((data["main"]["temp"] - 273.15) * (9 / 5) + 32), 2)
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} fahrenheit")
else:
    print("An error occurred.")
