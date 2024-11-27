# 46elks SMS Handler

This project contains a collection of Python scripts for interacting with the [46elks](https://46elks.se/) API.

## Features
All the scripts are developed for CLI.

### send-sms.py
    Send SMS to one or more recipients: This script allows you to send a simple SMS message to a recipientdefined by
    either a phone number in E.164 format or a CSV file containing a list of phone numbers.
    
    https://46elks.se/docs/send-sms

### send-mms.py
    Send MMS to one or more recipients: This script allows you to send a multimedia message (MMS) to a 
    single recipient or multiple recipients listed in a CSV file. The script accepts optional parameters 
    to specify the sender name, message text, and an image URL or Base64 representation to include in the MMS.
    
    https://46elks.se/docs/send-mms

### send-message.py
    Send SMS or MMS to one or more recipients: This script allows you to send either an SMS or 
    an MMS message to a single recipient or multiple recipients listed in a CSV file. You can customize 
    the sender name, message text, and optionally include an image URL or Base64 representation to send 
    an MMS. The script automatically determines whether to send an SMS or MMS based on the provided arguments.

### receive-sms.py
    Receive and respond to SMS messages: This script sets up a simple web server using the Bottle framework 
    (I also use NGROK) to receive incoming SMS messages through the 46elks API. Depending on the specified action, 
    the script can either reply with a predefined message or forward the received SMS to another phone number.
    
    https://46elks.se/docs/receive-sms