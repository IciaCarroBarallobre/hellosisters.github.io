from abc import ABC, abstractmethod
class Command(ABC):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    @abstractmethod
    def accion(self, obj):
        pass