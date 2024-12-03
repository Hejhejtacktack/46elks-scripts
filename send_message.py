import requests  # Importerar en extern modul som hanterar HTTP anrop
from utils.utils import csv_to_list  # Importerar funktionen csv_to_list från modulen utils.py i mappen utils
from dotenv import load_dotenv  # Importerar funktionen load_dotenv från den externa modulen dotenv
import os  # Importerar en extern modul för att använda operativsystembundna funktioner

load_dotenv()  # Kallar på funktion som översätter en .env fil och laddar in variabler i den

def send_message(api_auth: tuple, api_data: dict):  # Definierar en funktion med tre parametrar
    """
    Sends an MMS if 'image' element is present in 'api_data', otherwise an SMS, through the 46elks API
    :param api_auth: The 46elks API credentials (found on 46elks.se)
    :param api_data: The 46elks API data
    """
    if 'image' in api_data:
        api_url = os.getenv('API_URL_MMS')
    else:
        api_url = os.getenv('API_URL_SMS')

    response = requests.post(  # Instansierar en variabel till vad requests.post() (som har tre parametrar) returnerar
        api_url,  # En parameter
        auth=api_auth,  # En parameter
        data=api_data
    )  # Slutparentes för post()-metoden
    print(response.text)  # Skriver ut parameter via stream eller stdout


if __name__ == "__main__":
    import argparse  # Importerar en extern modul som hanterar inmatning via CLI

    parser = argparse.ArgumentParser(
        description="Send an message using 46elks API.")  # Instansierar en variabel till en instans av klassen ArgumentParser som finns i modulen argparse

    parser.add_argument('receivers',
                        # Kallar på funktionen add_argument från objektet parser som adderar en parameter för att exekvera modulen
                        type=str,  # Definierar vilken typ av variabel metoden förväntar sig
                        help="Receiver phone number in E.164 format (e.g., +46701234567) or a path to a CSV file with phone numbers.")  # Beskriver vad som händer när användaren matar in -h i CLI

    # Optional arguments
    parser.add_argument('--sender',
                        # Kallar på funktionen add_argument från objektet parser som adderar en parameter för att exekvera modulen
                        type=str,  # Definierar vilken typ av variabel metoden förväntar sig
                        default="noreply",  # Instansierar ett standardvärde till parametern
                        help="The name of sender in a short format. Default is 'noreply'. To send MMS use 'noreply'")  # Beskriver vad som händer när användaren matar in -h i CLI
    parser.add_argument('--message',
                        type=str,
                        default="Hej",
                        help="The message to send. Enclose the message in quotes if it contains spaces. Default is 'Hej'.")
    parser.add_argument('--image',
                        # Kallar på funktionen add_argument från objektet parser som adderar en parameter för att exekvera modulen
                        type=str,  # Definierar vilken typ av variabel metoden förväntar sig
                        default=None,  # Instansierar ett standardvärde till parametern
                        help="A publicly accessible URL pointing to an image file or a Base64/url-encoded string containing representation of an image.")  # Beskriver vad som händer när användaren matar in -h i CLI

    args = parser.parse_args()  # Konverterar strings till object och definierar dem som attribut

    # Makes receivers a list if argument does not start with "+"
    receivers = [args.receivers] if args.receivers.startswith("+") else csv_to_list(args.receivers)  # Instansierar receivers till en lista

    auth = (os.getenv('API_USERNAME'), os.getenv('API_PASSWORD'))  # Instansierar en variabel till en lista innehållandes vad os.getenv returnerar baserat på en key

    if auth.__contains__(None):  # Kör nedanstående kodrad, om kravet att listan auth innehåller None uppfylls
        raise ValueError('No API credentials provided.')  # Genererar ett ValueError och stoppar exekveringen

    data = {  # Definierar och intansierar en variabel innehållandes ett Set
        "from": args.sender,  # Ett element i Setet
        "message": args.message  # Ett element i Setet
    }

    # Setting API url
    if args.image is not None:  # Kör nedanstående kodrader, om kravet att args.image inte innehåller None uppfylls
        url = os.getenv('API_URL_MMS')  # Definierar och intansierar en variabel till vad metoden os.getenv returnerar
        data['image'] = args.image  # Adderar ett element med keyn image och valuet i args.image till setet data
    else:  # Kör nedanstående kodrad om inte kravet i if-statementet uppfylls
        url = os.getenv('API_URL_SMS')  # Instansierar variabeln url till vad os.getenv rerturnerar

    for phone_number in receivers:  # Loopar genom alla element i listan receivers
        data['to'] = phone_number  # Adderar ett element med keyn to och valuet i phone_number till setet data
        send_message(auth, data)  # Kallar på funktionen send_message och skickar in 3 variabler som parametrar
