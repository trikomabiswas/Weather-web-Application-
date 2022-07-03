
import requests 

api_key = '0fdf1a91e65c05796c88a5fc89801c58'
        
user_input = input("Enter city: ")
print(user_input)
#---------------------------------------till step 1
        
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid=0fdf1a91e65c05796c88a5fc89801c58")
#----- step 2 {Prequest}

#---- step-3 reply
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp} ºF")
    print(f"The temperature in {user_input} is: {temp -273.15} ºC")
    #print("%.2f" % x)