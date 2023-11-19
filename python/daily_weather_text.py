import schedule
import time
from components.get_weather import weather_update
from components.twilio_message import send_text_message
    
def send_weather_update():
    weather_info = weather_update()
    send_text_message(weather_info)

def main():
    schedule.every().day.at("8:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()