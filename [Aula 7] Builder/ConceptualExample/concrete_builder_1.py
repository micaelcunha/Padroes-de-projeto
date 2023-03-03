from builder import Builder
from product_1 import Product1


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.__product = Product1()

    def product(self) -> Product1:
        product = self.__product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self.__product.add("PartA1")

    def produce_part_b(self) -> None:
        self.__product.add("PartB1")

    def produce_part_c(self) -> None:
        self.__product.add("PartC1")
