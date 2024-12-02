import argparse
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def call(api_auth, api_data):
    response = requests.post(
        os.getenv("API_URL_CALLS"),
        data=api_data,
        auth=api_auth,
    )
    print(response.text)

parser = argparse.ArgumentParser(description="Make a call and forward it to {who?} using 46elks' API")

# parser.add_argument("API_USERNAME", type=str, help="Your 46elks API username")
# parser.add_argument("API_PASSWORD", type=str, help="Your 46elks API password")
parser.add_argument("caller", type=str, help="Caller's phone number in E.164 format (e.g.+46701234567)."
                                             "This number shows as caller (also when forwarding call)")
parser.add_argument("callee", type=str, help="Callee's phone number in E.164 format (e.g.+46701234567)")

args = parser.parse_args()

auth = (
    os.getenv('API_USERNAME'),
    os.getenv('API_PASSWORD')
    )

action = {
    "connect" : os.getenv('PHONE_NUM_CAROLINE')
}

data = {
    'from': args.caller,
    'to': args.callee
    # 'voice_start': json.dumps(action)
    }

call(auth, data)