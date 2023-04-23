key="<your api key>"
import requests
def get_city_coordinates(city):
    response=requests.get("http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API}".format(API=key,city=city))
    first=0

    lat,long=response.json()[first]['lat'],response.json()[first]['lon']
    return lat,long

def getWeather(city):
    lat,long=get_city_coordinates(city)
    url="https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={key}".format(lat=lat,long=long,key=key)
    response=requests.get(url).json()
    return response["weather"][0]['main']

print(getWeather('Hyderabad'))