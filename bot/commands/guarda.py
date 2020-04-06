from commands.command import Command

class Guarda(Command):

    def __init__(self):
        Command.__init__(self, 
        "guarda", 
        "\"@mencion guarda msg\" - Guardo el msg en el Readme correspondiente al canal y lo subo GitHub. "
        )

    # Debe subir y cambiar la respuesta en caso de que no salga bien
    def accion(self, obj = None):
        return "Sin implementar todavía"
