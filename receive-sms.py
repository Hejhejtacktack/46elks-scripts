from bottle import request, post, run
import json

@post('/sms')
def sms():
  print("You have received an SMS")
  return {
    "reply": "Thank you for your message."}

run(host='0.0.0.0', port=8080)