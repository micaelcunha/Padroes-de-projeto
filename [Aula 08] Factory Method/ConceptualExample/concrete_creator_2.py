from concrete_product_2 import ConcreteProduct2
from creator import Creator
from product import Product


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
