from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass