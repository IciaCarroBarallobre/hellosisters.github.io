from commands.command import Command

class Hola(Command):

    def __init__(self):
        Command.__init__(self, 
        "hola", 
        "\"@mencion hola\" - Saludo de vuelta. "
        )

    # Debe recoger de cada comando la descripcion y devolverlo
    def accion(self, obj = None):
        return "Hola, ¿Te puedo ayudar en algo?\n Si quieres ver que posibles interaciones tengo escribe: @mecion ayuda"

