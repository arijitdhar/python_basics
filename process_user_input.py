__author__ = '220152'

def weather_condition(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"

temperature = float(input("Enter temperature:"))
print(weather_condition(temperature))
