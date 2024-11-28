import argparse
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(description="Make a call and forward it to {who?} using 46elks' API")

parser.add_argument("API_USERNAME", type=str, help="Your 46elks API username")
parser.add_argument("API_PASSWORD", type=str, help="Your 46elks API password")
parser.add_argument("caller", type=str, help="Caller's phone number in E.164 format (e.g.+46701234567)."
                                             "This number shows as caller (also when forwarding call)")
parser.add_argument("callee", type=str, help="Callee's phone number in E.164 format (e.g.+46701234567)")

args = parser.parse_args()

auth = (
    os.getenv('API_USERNAME'),
    os.getenv('API_PASSWORD')
    )

action = {
    "connect" : os.getenv('CAROLINE_PHONE_NUMBER') # Make user choose action?
}

fields = {
    'from': args.caller,
    'to': args.callee,
    'voice_start': json.dumps(action),
    }

response = requests.post(
    "https://api.46elks.com/a1/calls",
    data=fields,
    auth=auth
    )

print(response.text)