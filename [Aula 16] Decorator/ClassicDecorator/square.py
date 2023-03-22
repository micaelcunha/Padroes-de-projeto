from shape import Shape


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def __str__(self) -> str:
        return f"A square with side {self.side}."
