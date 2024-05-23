import os
from dotenv import load_dotenv

load_dotenv()

def envs() -> dict:
  envs = {
    "TWILIO_ACCOUNT_SID": os.getenv("TWILIO_ACCOUNT_SID"),
    "TWILIO_AUTH_TOKEN": os.getenv("TWILIO_AUTH_TOKEN"),
    "TWILIO_FROM_NUMBER": os.getenv("TWILIO_FROM_NUMBER"),
  }

  for k, v in envs.items():
    if v is None:
      raise Exception(f"Missing environment variable: {k}")

  return envs
