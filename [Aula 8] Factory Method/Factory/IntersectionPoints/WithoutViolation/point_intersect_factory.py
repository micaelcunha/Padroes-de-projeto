from math import cos, sin

from point_intersect import PointIntersect


class PointIntersectFactory:
    @staticmethod
    def new_cartesian_point(x: int, y: int) -> PointIntersect:
        return PointIntersect(x, y)

    @staticmethod
    def new_polar_point(rho: int, theta: int) -> PointIntersect:
        return PointIntersect(rho * sin(theta), rho * cos(theta))
