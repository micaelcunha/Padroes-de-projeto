from abc import ABC, abstractmethod


class Creator(ABC):
    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"

    @abstractmethod
    def factory_method(self):
        pass
