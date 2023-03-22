from shape import Shape


# This is a decorator.
class TransparentShape(Shape):
    def __init__(self, shape, transparency) -> None:
        self.shape = shape
        self.transparency = transparency

    def __str__(self) -> str:
        return f"{self.shape} has {self.transparency * 100.0}% transparency."
