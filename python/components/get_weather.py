import requests

def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relaivehumidity_2m,windspeed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data
    
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
    
def weather_update():
    # Set to latitude and longitude of location you want daily reports.
    # Currently set for Detroit, MI
    latitude = 42.3314
    longitude = -83.0458
    
    weather_data = get_weather(latitude, longitude)
    temperature_celsius = weather_data["hourly"]["temperature_2m"][0]
    relative_humidity = weather_data["hourly"]["relativehumidity_2m"][0]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
    
    weather_info = (
        f"Current Weather in Detroit:\n"
        f"Temperature: {temperature_fahrenheit:.2f}°F\n"
        f"Relative Humidity: {relative_humidity}%\n"
        f"Wind Speed: {wind_speed} m/s"
    )
    
    return weather_info