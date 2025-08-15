from abc import ABC, abstractmethod

class Relational(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def metaData(self, *args, **kwargs):
        pass
    @abstractmethod
    def cursor(self, *args, **kwargs):
        pass