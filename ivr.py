import json
import os
import requests
from dotenv import load_dotenv
from flask import Flask, request

app = Flask(__name__)

load_dotenv()

@app.route('/ivr/incoming-calls', methods=['POST'])
def incoming_calls():
    print(request.form)
    response = {
        'ivr' : 'https://46elks.com/static/sound/voiceinfo.mp3', # TODO
        'digits' : '1',
        'next' : '/ivr/choice' # TODO
    }

    return json.dumps(response)

@app.route('/ivr/choice', methods=['POST'])
def ivr():
    print(request.form)
    if request.form['result'] == '1':
        # SPELA LJUDFIL OCH SKICKA SMS
        # return {'play' : 'https://46elks.com/static/sound/smsinfo.mp3'} # TODO
        # response = requests.post(
        #     'https://api.46elks.com/a1/sms',
        #     auth=(os.getenv('API_USERNAME'), os.getenv('API_PASSWORD')),
        #     data={
        #         'from': 'ErikCo',
        #         'to': request.form.get('from'),
        #         'message': 'Here is a text message after you ended the call.'
        #     }
        # )
        # print(response.text)
    if request.form['result'] == '2':
        # RING JOAKIM


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)