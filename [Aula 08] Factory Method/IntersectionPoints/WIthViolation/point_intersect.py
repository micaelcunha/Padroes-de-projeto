from math import *

from coordinate_system import CoordinateSystem


class PointIntersect:
    def __init__(self, a: int, b: int, system=CoordinateSystem.CARTESIAN) -> None:
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)

    def __str__(self) -> str:
        return f"x {self.x}, y: {self.y}"
