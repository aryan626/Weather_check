import requests, json
apikey = "342be8ac66702177b841364e5012a1b6"
baseURL = "https://api.openweathermap.org/data/2.5/weather?q="
CityName = input("Enter your city : ")
completeURL = baseURL + CityName + "&appid=" + apikey
response = requests.get(completeURL)
data = response.json()
print("Current Temperture",data["main"]["temp"])
print("Current Temperture Feels like",data["main"]["feels_like"])
print("Maximum Temperture",data["main"]["temp_max"])
print("Minimum Temperture",data["main"]["temp_min"])

