import requests
import argparse
from utils.utils import csv_to_list
from dotenv import load_dotenv
import os

load_dotenv()


def send_message(api_url, api_auth, api_data):
    response = requests.post(
        api_url,
        auth=api_auth,
        data=api_data
    )
    print(response.text)


parser = argparse.ArgumentParser(description="Send an message using 46elks API.")

# parser.add_argument('api_username',
#                     type=str,
#                     help="Your 46elks API username (provided by 46elks).")
# parser.add_argument('api_password',
#                     type=str,
#                     help="Your 46elks API password (provided by 46elks).")
parser.add_argument('receivers',
                    type=str,
                    help="Receiver phone number in E.164 format (e.g., +46701234567) or a path to a CSV file with phone numbers.")

# Optional arguments
parser.add_argument('--sender',
                    type=str,
                    default="noreply",
                    help="The name of sender in a short format. Default is 'noreply'. To send MMS use 'noreply'")
parser.add_argument('--message',
                    type=str,
                    default="Hej",
                    help="The message to send. Enclose the message in quotes if it contains spaces. Default is 'Hej'.")
parser.add_argument('--image',
                    type=str,
                    default=None,
                    help="A publicly accessible URL pointing to an image file or a Base64/url-encoded string containing representation of an image.")

args = parser.parse_args()

# Makes receivers a list if argument does not start with "+"
receivers = [args.receivers] if args.receivers.startswith("+") else csv_to_list(args.receivers)

auth = (os.getenv('API_USERwNAME'), os.getenv('API_PASSeWORD'))

if auth.__contains__(None):
    raise ValueError('No API credentials provided.')

data = {
    "from": args.sender,
    "to": args.receivers,
    "message": args.message
}

# Setting API url
if args.image is not None:  # If image is present in data
    url = os.getenv('API_URL_MMS')
    data['image'] = args.image
else:  # If image is not present in data
    url = os.getenv('API_URL_SMS')

send_message(url, auth, data)
