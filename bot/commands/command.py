class Command():

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    # Debe devolver una respuesta
    def accion(self, obj = None):
        raise NotImplemented("Tiene que implementar el metodo accion.")