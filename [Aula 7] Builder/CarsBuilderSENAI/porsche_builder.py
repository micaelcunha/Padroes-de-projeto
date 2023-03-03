from body import Body
from builder import Builder
from engine import Engine
from wheel import Wheel


class PorscheBuilder(Builder):
    def get_wheel(self) -> Wheel:
        pass

    def get_engine(self) -> Engine:
        pass

    def get_body(self) -> Body:
        pass