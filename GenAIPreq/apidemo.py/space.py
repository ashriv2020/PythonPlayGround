import requests
url='http://api.open-notify.org/astros.json'
response = requests.get(url)

resp_json = response.json()

#print(resp_json)
for m in resp_json['people']:
    # print('People found in space ')
    print(m['name'], '--> ', m['craft'])
