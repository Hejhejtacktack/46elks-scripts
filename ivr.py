import json
import os
import requests
from dotenv import load_dotenv
from flask import Flask, request

app = Flask(__name__)

load_dotenv()

auth = (os.getenv("API_USERNAME"), os.getenv("API_PASSWORD"))

@app.route('/ivr/incoming-calls', methods=['POST'])
def incoming_calls():
    print(request.form)
    response = {
        'ivr': 'https://46elks.com/static/sound/voiceinfo.mp3',
        'digits': '1',
        'next': 'https://63e5-94-234-96-85.ngrok-free.app/ivr/choice'
    }
    return json.dumps(response)


@app.route('/ivr/choice', methods=['POST'])
def ivr():
    print(request.form)
    if request.form['result'] == '1':
        # SPELA LJUDFIL OCH SKICKA SMS
        response = {
            'play': 'https://www.46elks.com/static/sound/smsinfo.mp3'
        }
        return json.dumps(response)
    if request.form['result'] == '2':
        # Calls the specified key in .env
        response = {
            'connect': os.getenv('PHONE_NUM_CAROLINE'),
            'callerid': request.form['from']
        }
        return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
