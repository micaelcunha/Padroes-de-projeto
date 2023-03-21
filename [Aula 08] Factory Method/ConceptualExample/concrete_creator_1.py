from concrete_product_1 import ConcreteProduct1
from creator import Creator
from product import Product


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()
