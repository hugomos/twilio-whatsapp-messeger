from twilio.rest import Client 
from config.env import envs

_envs = envs()
twilio_rest_client = Client(_envs["TWILIO_ACCOUNT_SID"], _envs["TWILIO_AUTH_TOKEN"])

message = twilio_rest_client.messages.create(
  body = f"Aloy, test from python!",
  from_=_envs["TWILIO_FROM_NUMBER"],
  to=f"whatsapp:+5511999999999",
  media_url="https://github.com/hugomos.png"
)

print("Message SID: " + message.sid)