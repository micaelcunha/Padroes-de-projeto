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

    @staticmethod
    def new_cartesian_point(x: int, y: int):
        return PointIntersect(x, y)

    @staticmethod
    def new_polar_point(rho: int, theta: int):
        return PointIntersect(rho * sin(theta), rho * cos(theta))