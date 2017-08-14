# NOTE: This example uses the ALPHA release of the next generation Twilio
# helper library - for more information on how to download and install this
# version, visit
# https://www.twilio.com/docs/libraries/python#accessing-preview-twilio-features
from twilio.rest import Client

# Account SID and Auth Token are found in the console:
# twilio.com/console
account = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
token = "your_auth_token"

client = Client(account, token)

session = client.preview \
    .proxy \
    .services("KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
    .sessions \
    .create(unique_name="MyFirstSession")

print(session.sid)
