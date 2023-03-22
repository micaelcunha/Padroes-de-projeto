from shape import Shape


class Circle(Shape):
    def __init__(self, radius: float = 0.0) -> None:
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self) -> str:
        return f"A circle of radius {self.radius}."
