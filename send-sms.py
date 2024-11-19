import requests
import argparse

parser = argparse.ArgumentParser(description="Send an SMS containing 'Hej' from 'Elks' using 46elks API.")
parser.add_argument('api_username', type=str, help="Your 46elks API username (provided by 46elks).")
parser.add_argument('api_password', type=str, help="Your 46elks API password (provided by 46elks).")
parser.add_argument('receiver_phone_number', type=str, help="Receiver phone number in E.164 format, e.g., +46701234567.")

args = parser.parse_args()

API_USERNAME = args.api_username
API_PASSWORD = args.api_password
receiver = args.receiver_phone_number

response = requests.post(
  'https://api.46elks.com/a1/sms',
  auth = (API_USERNAME, API_PASSWORD),
  data = {
    'from': 'Elks',
    'to': receiver,
    'message': "Hej"
  }
)
print(response.text)