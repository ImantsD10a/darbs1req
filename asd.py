import requests

response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=917f3e81cdc041caaf674930252103&q=Liepāja&days=1&aqi=yes&alerts=yes")
data = response.json() #datu iegūšna
Key = "917f3e81cdc041caaf674930252103"
#for weather in data["current"]:
#    print(weather)
print("Location:")
print(data["location"]["name"]) #pilsēta
print("Temp.C:")
print(data["current"]["temp_c"]) #temperatūra
print("Current Time:")
print(data["location"]["localtime"]) #laiks

