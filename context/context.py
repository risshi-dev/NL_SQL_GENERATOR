from abc import ABC, abstractmethod

class Context(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_schema_information(self, *args, **kwargs):
        pass