from abc import ABC, abstractmethod

class shape(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        pass