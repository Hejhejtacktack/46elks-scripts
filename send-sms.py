import requests
import argparse
from utils.converter import csv_to_list


parser = argparse.ArgumentParser(description="Send an SMS using 46elks API.")
parser.add_argument('api_username', type=str, help="Your 46elks API username (provided by 46elks).")
parser.add_argument('api_password', type=str, help="Your 46elks API password (provided by 46elks).")
parser.add_argument('receivers', type=str,
                    help="Receiver phone number in E.164 format (e.g., +46701234567) or a path to a CSV file with phone numbers.")

# Optional argument for custom message
parser.add_argument('-m', '--message', type=str, default="Hej",
                    help="The message to send. Enclose the message in quotes if it contains spaces. Default is 'Hej'.")
parser.add_argument('--sender', type=str, default="Elks",
                    help="The name of sender in a short format. Default is 'Elks'.")

args = parser.parse_args()

api_username = args.api_username
api_password = args.api_password
receivers = args.receivers  # Str containing a phone number or a file path
message = args.message
sender = args.sender

# Makes receivers a list
receivers = [receivers] if receivers.startswith("+") else csv_to_list(receivers)

for phone_number in receivers:
    response = requests.post(
        'https://api.46elks.com/a1/sms',
        auth=(api_username, api_password),
        data={
            'from': sender,
            'to': phone_number,
            'message': message
        }
    )
    print(response.text)