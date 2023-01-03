import requests
import json

url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Mae%20Chan?unitGroup=metric&include=current&key=ASRQL55QSXYKL63Y2DCEMFUC3&contentType=json'
response = requests.get(url)
text = response.text

with open('json.json', 'w') as f:
    f.write(text)

weather_data = json.loads(text)
#print(weather_data["currentConditions"])

current_conditions = weather_data["currentConditions"]
temperature = current_conditions["temp"]

print(f'\nTemperature: {temperature:.0f}°C')