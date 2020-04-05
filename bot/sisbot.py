
import os
import time
import re
from slackclient import SlackClient


# Instanciar cliente de slack con nuestra variable de entorno
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
ID_bot = None

# constants
DELAY_AFTER_READ = 3 
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

# Determina si el evento contiene un comando para el bot
# Devuelve una tupla Comando, canal si determina que si
# Devuelve None, Nonde si determina que no

def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"]) # Mira si le hablan al bot
            if user_id == ID_bot:
                return message, event["channel"]
    return None, None

# Mencion directa @bot separandolo en grupo nombre de usuario y mensaje
# Si no encuentra devuelve None, None

def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

# Si el bot conoce el comando se ejecuta
def handle_command(command, channel):

    default_ayuda = "Lo siento no lo entiendo. \n Escribelo con este formato  *{}*.".format(EXAMPLE_COMMAND)
    response = None

    if command.startswith(EXAMPLE_COMMAND): # Si si que coincide con el formato
        response = "Lo tengo :) pero aun no esta implentado"

    # Enviar la respuesta
    slack_client.api_call("chat.postMessage",channel=channel,text=response or default_ayuda)

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False): #Conectar cliente con la API Slack RTM
        print("SisBot se ha conectado correctamente con API Slack RTM")
        ID_bot = slack_client.api_call("auth.test")["user_id"] # ID para el espacio de trabajo en concreto (Util para las menciones)
        
        while True: #Loop para que este recibiendo comandos
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(DELAY_AFTER_READ) #Sleep para dejar descansar a la CPU
    
    else:
        print("SisBot no se ha podido conectar con API Slack RTM =(")