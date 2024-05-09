from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    API_KEY = open(".\\API_KEY", "r").read() # Open textfile that has api key & store it in var named API_KEY
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    
    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        # call function fetch_weather and store data in 2 vars
        weather_data1 = fetch_weather(city1, API_KEY, current_weather_url)
        # check if user requested city2, if true then do the same above
        if city2:
           weather_data2 = fetch_weather(city2, API_KEY, current_weather_url)
        else:
            weather_data2 = None

        
        context = {
            "weather_data1": weather_data1,
            "weather_data2": weather_data2,
        }

        return render(request, "C:\\Users\\dell\\Desktop\\EducationNour\\CS\\webDev\\projects\\weatherappDJ\\weather_app\\templates\\index.html", context)
    else:
        return render(request, "C:\\Users\\dell\\Desktop\\EducationNour\\CS\\webDev\\projects\\weatherappDJ\\weather_app\\templates\\index.html")


def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    
    # make a dict to be easily filled in template page
    weather_data = {
        "city": city,
        # get temperature from response then convert it from F to Celsius and round to nearest 2 decimals
        "temperature": round(response["main"]["temp"] - 273.15, 2),
        "description": response["weather"][0]["description"],
        "icon": response["weather"][0]["icon"],
    }

    return weather_data