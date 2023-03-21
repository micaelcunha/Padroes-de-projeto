from abc import ABC, abstractmethod

from body import Body
from engine import Engine
from wheel import Wheel


class Builder(ABC):
    @abstractmethod
    def get_wheel(self) -> Wheel: pass

    @abstractmethod
    def get_engine(self) -> Engine: pass

    @abstractmethod
    def get_body(self) -> Body: pass
