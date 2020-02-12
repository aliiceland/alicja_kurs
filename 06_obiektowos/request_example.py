import requests 
resp = requests.get("https://www.metaweather.com/api/location/search/?query=warsaw")
print(resp.status_code)
print(resp.content)


id_= resp.json()[0]['woeid']
resp_1 = requests.get(f"https://www.metaweather.com/api/location/{id_}/")
print(resp_1.content)
print(resp_1.json())
zm_1= resp_1.json()["consolidated_weather"][0]
d_temp = zm_1["the_temp"]
d_humid = zm_1["humidity"]
d_wind = zm_1["wind_speed"]

print(f"""
temperatura: {d_temp}
wilgotnosc: {d_humid}
wiatr: {d_wind}
""")


