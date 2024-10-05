import requests
city = str(input('please enter city name to check temprature:'))
api_key = 'YOUR_API_KEY'
Url = 'http://api.weatherapi.com/v1/current.json?key='+api_key+city+'&aqi=no'
response = requests.get(Url)
wather_json = response.json()

temp = wather_json.get('current').get('temp_c')
temp_desc = wather_json.get('current').get('condition').get('text')

print("Today's weather in ", city, ' is ', temp_desc, ' and ', temp, ' degree')

