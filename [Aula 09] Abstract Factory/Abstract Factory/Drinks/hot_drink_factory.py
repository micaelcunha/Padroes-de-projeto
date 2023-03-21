from abc import ABC, abstractmethod


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount):
        pass
