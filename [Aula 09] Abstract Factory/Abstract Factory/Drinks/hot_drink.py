from abc import ABC, abstractmethod


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass
