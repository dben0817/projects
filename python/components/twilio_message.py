# Download the helper library from https://www.twilio.com/docs/python/install
# Can also use 'pip install twilio' in the command line
from twilio.rest import Client

def send_text_message(message):
    # Sign up for a Twilio account and enter in the following information
    twilio_account_sid = ""  
    twilio_account_token = "" # Find your Account SID and Auth Token at twilio.com/console
    twilio_phone_number = ""
    
    personal_cell_number = ""
    
    client = Client(twilio_account_sid, twilio_account_token)
    
    client.message.create(
        to=personal_cell_number,
        from_=twilio_phone_number,
        body=message
    )