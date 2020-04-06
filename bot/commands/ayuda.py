from commands.command import Command

class Ayuda(Command):

    def __init__(self):
        Command.__init__(self, 
        "ayuda", 
        "\"@mencion ayuda\" - Te comento las posibles interaciones que tengo. " 
        )

    # Debe recoger de cada comando la descripcion y devolverlo
    def accion(self, obj = None):
        response = "Mis posibles interaciones actuales son ..."
        for command in obj.values():
            response = response + "\n" + command.getDescription()
        return response
        
