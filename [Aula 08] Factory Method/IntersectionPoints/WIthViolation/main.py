from coordinate_system import CoordinateSystem
from point_intersect import PointIntersect

p1 = PointIntersect(2, 3, CoordinateSystem.CARTESIAN)
p2 = PointIntersect(2, 3, CoordinateSystem.POLAR)
print(f"Cartesian result: {p1}")
print(f"Polar result: {p2}")
