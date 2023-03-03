from builder import Builder
from car import Car


class Director:
    def set_builder(self, builder: Builder):
        self.__builder = builder

    def get_car(self) -> Car:
        pass
