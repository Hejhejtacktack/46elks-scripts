from bottle import request, post, run
import json
import argparse


parser = argparse.ArgumentParser(description='Receive SMS messages through 46elks API. '
                                             'This script is supposed to run a simple web server so your 46elks phone number can receive sms. '
                                             'This may be a weird script, I know')

parser.add_argument("actions",
                    nargs=2,
                    type=str,
                    default='send',
                    help="Action the script takes when received a sms, "
                         "'reply' or 'forward' "
                         "followed by either the reply message or forward phone number in E.164 format (e.g., +46701234567)")

args = parser.parse_args()

@post('/sms')
def sms():
    print("You have received an SMS")
    return {
        args.actions[0] : args.actions[1]
    }


run(host='0.0.0.0', port=8080)
