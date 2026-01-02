import requests
# library : ->cmd , terminal
# pip install requests
api_key = "eaae20cb832c415f9c8125004260201"
# JSOn -javascript object notation
# key:value
city = input("Enter City : ").replace(" ","+")
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"
response = requests.get(url)
# print(response)
if response.status_code==200:
    data = response.json()
    print("City : ",data["location"]["name"])
    print("Temp : ",data["current"]["temp_c"],"C")
    if data["current"]["air_quality"]["us-epa-index"]>=4:
        print("💀Danger..Dont Go Outside")
    else:
        print("Healthy AQI")
    # US EPA INDEX >=4 ->VERY POOR - 
