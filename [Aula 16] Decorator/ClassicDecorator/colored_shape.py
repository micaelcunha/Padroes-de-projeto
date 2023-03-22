from shape import Shape


# This is a decorator.
class ColoredShape(Shape):
    def __init__(self, shape, color) -> None:
        if isinstance(shape, ColoredShape):
            raise Exception("Cannot apply ColoredDecorator twice.")
        self.shape = shape
        self.color = color

    def __str__(self) -> str:
        return f"{self.shape} has the color {self.color}."
