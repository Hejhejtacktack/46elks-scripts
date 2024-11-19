import requests

API_USERNAME = "" # Replace with your 46elks API_USERNAME
API_PASSWORD = "" # Replace with your 46elks API_PASSWORD
receiver = '+46XXXXXXXXX' # Replace with phone number in E.164-format

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