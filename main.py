#Your new Phone Number is +18647778894

import requests
TWILIO_SID = "your twilio sid"
TWILIO_AUTHTOKEN = "2d6e9a5fcb8f7e1646903fed614b9211"
TWILIO_MESSAGE_ENDPOINT = "https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json".format(TWILIO_SID=TWILIO_SID)
TWILIO_NUMBER = "whatsapp:+14155238886"
def send_whatsapp_message(to, message):
    message_data = {
        "To": to,
        "From": TWILIO_NUMBER,
        "Body": message,
    }
    response = requests.post(TWILIO_MESSAGE_ENDPOINT, data=message_data, auth=(TWILIO_SID, TWILIO_AUTHTOKEN))
    
    response_json = response.json()
    
    
    return response_json
to_number = "whatsapp:+38269152741"
appointment_msg = "Test porukica."
msg = send_whatsapp_message(to_number, appointment_msg)
print(msg['sid']) # SM5xxxafa561e34b1e84c9d22351ae08a0
print(msg['status']) # queued