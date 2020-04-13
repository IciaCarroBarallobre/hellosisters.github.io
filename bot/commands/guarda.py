from commands.command import Command
import re
import os
from datetime import date
from datetime import datetime
import pandas as pd

PATH = "../slack-resources/"

class Guarda(Command):

    def __init__(self):
        Command.__init__(self, 
        "guarda", 
        "\"@mencion guarda msg\" - Guardo el msg en el Readme correspondiente al canal y lo subo GitHub. "
        )
    
    def obtain_df(self, path):
        
        if(os.path.exists(path)):
            df = pd.read_csv(path)
        else:
            df = pd.DataFrame(columns=['Fecha', 'Descripcion', 'Enlace'])
        
        return df
    
    def obtain_path(self, channel):
        return PATH+"/"+channel+".csv"

    

    # Debe subir y cambiar la respuesta en caso de que no salga bien
    def accion(self, obj = None):
        
        text,canal = obj[0], obj[1]
        url_expr='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_expr, text)
        text = re.sub(r'\<.*?\>', '', text)

        try:
            path = self.obtain_path(canal)
            df = self.obtain_df(path)

            fecha = datetime.now().strftime('%Y/%m/%d %H:%M')
            df = df.append({'Fecha': fecha, 'Descripcion': text, 'Enlace': urls}, ignore_index=True)
            df.sort_values(by=['Fecha'], ascending=False, inplace = True)
            df.to_csv(path, index=False)
                
            return "¡Ha sido guardado!"
        except:
            return "Ha ocurrido un error en la accion de guardar"


