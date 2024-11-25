import requests
import argparse
from utils.utils import csv_to_list

API_URLS = ('https://api.46elks.com/a1/sms', "https://api.46elks.com/a1/MMS")

def send():
    response = requests.post(
        url,
        auth=auth,
        data=data
    )
    print(response.text)

parser = argparse.ArgumentParser(description="Send an message using 46elks API.")

parser.add_argument('api_username',
                    type=str,
                    help="Your 46elks API username (provided by 46elks).")
parser.add_argument('api_password',
                    type=str,
                    help="Your 46elks API password (provided by 46elks).")
parser.add_argument('receivers',
                    type=str,
                    help="Receiver phone number in E.164 format (e.g., +46701234567) or a path to a CSV file with phone numbers.")

# Optional arguments
parser.add_argument('--sender',
                    type=str,
                    default="ELks",
                    help="The name of sender in a short format. Default is 'Elks'. To send MMS use 'noreply'")
parser.add_argument('--message',
                    type=str,
                    default="Hej",
                    help="The message to send. Enclose the message in quotes if it contains spaces. Default is 'Hej'.")
parser.add_argument('--image',
                    type=str,
                    default=None,
                    help= "A publicly accessible URL pointing to an image file or a Base64/url-encoded string containing representation of an image.")

args = parser.parse_args()

# Makes receivers a list
receivers = [args.receivers] if args.receivers.startswith("+") else csv_to_list(args.receivers)

url = API_URLS[0]
auth = (args.api_username, args.api_password)
data = {
    "from": args.sender,
    "to": args.receivers,
    "message": args.message
}

if args.image is not None:
    url = API_URLS[1]
    data['image'] = args.image

send()