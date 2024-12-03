# 46elks scripts
This project contains Python scripts using the [46elks](https://46elks.se/) API.

## Features

### ivr.py

    IVR Handling in Flask: This script manages Interactive Voice Response (IVR) flows using Flask. 

### make_and_forward_call.py

    Initiate and forward calls: This script allows you to make a call from a specified caller to a callee using the 46elks
    API. You can provide the caller and callee phone numbers in E.164 format as command-line arguments.
    
    https://46elks.se/docs/make-call

### receive_sms.py

    SMS Receiver and Responder: This script provides functionality for receiving and responding to SMS messages via 
    the 46elks API. It runs a simple web server, enabling a configured 46elks phone number to handle incoming SMS messages.

### send_message.py

    Message Sending Utility: This script enables sending SMS or MMS messages through the 46elks API. It is designed 
    to support both command-line usage and integration into other modules.

## Required Imports
The script requires the following Python libraries:

requests:For making HTTP requests to the 46elks API.

os: For interacting with the operating system and environment variables.

dotenv: For loading configuration settings from a .env file.

argparse: For handling command-line arguments.