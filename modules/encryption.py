from abc import ABC, abstractmethod

class Encryption(ABC):
    @abstractmethod
    def encryption(self, data:str) -> str:
        pass

class Xor(Encryption):
    def encryption(self, data: str):
        return data
