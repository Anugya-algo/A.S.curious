#dictionary comprehension
#dictionary={key:expression for (key,value) in iterable}

cities_in_F =dict(Kashmir=32,Mumbai=75,Jaipur=100,Vishakapatnam=50)

cities_in_C={key:((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
 
weather=dict(Kashmir='snowing',Mumbai='sunny',Jaipur='sunny',Vishakapatnam='cloudy')

sunny_weather={key for (key,value) in weather.items() if value=='sunny'}
print(sunny_weather)

w_cities={key:('sunny' if value >=45 else "cloudy") for (key,value) in cities_in_F.items()}
print(w_cities)

def check_temp(value):
    if value >= 70:
       return"Hot"
    elif 69 >=value>= 45:
       return "Warm"
    else:
       return "Cold"

w1_cities={key:check_temp(value) for (key,value) in cities_in_F.items()}
print(w1_cities)