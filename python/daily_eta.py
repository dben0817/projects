import datetime
from components.gmaps import get_commute_duration
from components.twilio_message import send_text_message


def main():
    duration = get_commute_duration()
    
    now = datetime.now()
    arrival_time = (now + duration).strftime('%I:%M %p')
    work_start = now.replace(hour=9, minute=00)
    
    message = (
        f"Morning!\n"
        f"If you want to get to work by 9 am, it is suggested that you leave by {(work_start - duration).strftime('%I:%M %p')}"
        f"With traffic, it should take {duration} to get to work"
        f"If you now, you should arrive at approximately {arrival_time}"
    )
    
    send_text_message(message)