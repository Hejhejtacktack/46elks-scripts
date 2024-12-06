import json
import os
from dotenv import load_dotenv
from flask import Flask, request
from send_message import send_message

app = Flask(__name__)

load_dotenv()

auth = (os.getenv("API_USERNAME"), os.getenv("API_PASSWORD"))

@app.route('/ivr/incoming-calls', methods=['POST'])
def incoming_calls():
    print(request.form)
    response = {
        'ivr': 'https://46elks.com/static/sound/voiceinfo.mp3',
        'digits': '1',
        'next': '{INSERT NGROK HERE}/ivr/choice'
    }
    return json.dumps(response)


@app.route('/ivr/choice', methods=['POST'])
def ivr():
    print(request.form)
    if request.form['result'] == '1':
        response = {
            'play': 'https://www.46elks.com/static/sound/smsinfo.mp3'
        }
        sms_data = {
            'to': request.form['from'],
            'from': 'ErikCo',
            'message': 'Hej, du tryckte in ' + request.form['result']
        }
        send_message(auth, sms_data)
        return json.dumps(response)
    if request.form['result'] == '2':
        response = {
            'connect': os.getenv('PHONE_NUM_JOAKIM'),
            'callerid': request.form['from']
        }
        return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
