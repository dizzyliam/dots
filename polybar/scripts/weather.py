#!/bin/python

import requests

icons = {
"01d": "",
"01n": "",
"02d": "",
"02n": "",
"03d": "",
"03n": "",
"04d": "",
"04n": "",
"09d": "",
"09n": "",
"10d": "",
"10n": "",
"11d": "",
"11n": "",
"13d": "",
"13n": "",
"50d": "",
"50n": ""
}

key = "e8e9ce8b749de8fbfbf22fb04b1ca2ad"

desc = "main"

url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=metric&appid={}".format(-45.87416, 170.50361, key)
r = requests.get(url)
data = r.json()

out = ""

out += data["current"]["weather"][0][desc]

for index, i in enumerate(data["hourly"]):
    if i["weather"][0][desc] != out:
        out += ", " + i["weather"][0][desc] + " in " + str(index) + " hours"
        break

if "," not in out:
    for index, i in enumerate(data["daily"]):
        if i["weather"][0][desc] != out:
            out += ", " + i["weather"][0][desc] + " in " + str(index) + " days"
            break

print("  " + out.capitalize() + "  ")
