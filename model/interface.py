from abc import ABC, abstractmethod

class OA(ABC):
    @abstractmethod
    def buildContext(self, *args, **kwargs):
        pass

    @abstractmethod
    def query(self, *args, **kwargs):
        pass