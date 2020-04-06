import os # Variables de entorno
import time
import re # Buscar expresiones regulares
import json 
from slackclient import SlackClient # Trabajar con Slack

from commands.ayuda import Ayuda
from commands.hola import Hola
from commands.guarda import Guarda

# Instanciar cliente de slack con nuestra variable de entorno
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
ID_bot = None
data = None

# constants
DELAY_AFTER_READ = 3 
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
def handle_command(msg, channel):

    default_ayuda = "Lo siento, no lo entiendo. \n Para saber las posibles iteraciones que tengo: @mencioname ayuda" 
    response = None

    try:
        command_str = msg.split(" ")[0]
        command = data[command_str]
        obj = None


        if(command.getName() == "guarda"): #TODO estos ifs no me gustan nada
            obj = msg
        elif(command.getName() == "ayuda"):
            obj = data

        response = command.accion(obj)


    except KeyError:
        response = default_ayuda


    # Enviar la respuesta
    slack_client.api_call("chat.postMessage",channel=channel,text=response)

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False): #Conectar cliente con la API Slack RTM
        
        print("SisBot se ha conectado correctamente con API Slack RTM")
        ID_bot = slack_client.api_call("auth.test")["user_id"] # ID para el espacio de trabajo en concreto (Util para las menciones)

        data = {"guarda": Guarda() ,"hola": Hola(), "ayuda": Ayuda()}
        while True: 
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(DELAY_AFTER_READ)
    
    else:
        print("SisBot no se ha podido conectar con API Slack RTM =(")