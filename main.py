import requests
key = '24ad767c093c80435fa04169b7ce7f99'
api_adress = 'http://api.openweathermap.org/data/2.5/weather?q=Sintra&APPID=' + key
json_data = requests.get(api_adress).json()
wind_deg = json_data['wind']['deg']
wind_speed = 1.94384449 * json_data['wind']['speed'] # 1 m/s  = 1.94384449 kts

if (348.75 <= wind_deg < 360 or 0 <= wind_deg < 11.25 ):
    direction = 'N'
elif (11.25 <= wind_deg < 33.75):
    direction = 'NNE'
elif (33.75 <= wind_deg < 56.25):
    direction = 'NE'
elif (56.25 <= wind_deg < 78.75):
    direction = 'ENE'
elif (78.75 <= wind_deg < 101.25):
    direction = 'L'
elif (101.25 <= wind_deg < 123.75):
    direction = 'ESE'
elif (123.75 <= wind_deg < 146.25):
    direction = 'SE'
elif (146.25 <= wind_deg < 168.75):
    direction = 'SSE'
elif (168.75 <= wind_deg < 191.25):
    direction = 'S'
elif (191.25 <= wind_deg < 213.75):
    direction = 'SSO'
elif (213.75 <= wind_deg < 236.25):
    direction = 'SO'
elif (236.25 <= wind_deg < 258.75):
    direction = 'OSO'
elif (258.75 <= wind_deg < 281.25):
    direction = 'O'
elif (281.25 <= wind_deg < 303.75):
    direction = 'ONO'
elif (303.75 <= wind_deg < 326.25):
    direction = 'NO'
elif (326.25 <= wind_deg < 348.75):
    direction = 'NNO'

print(int(wind_speed))
print(wind_deg)
print(direction)