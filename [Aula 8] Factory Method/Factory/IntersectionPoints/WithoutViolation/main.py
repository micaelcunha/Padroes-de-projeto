from coordinate_system import CoordinateSystem
from point_intersect import PointIntersect
from point_intersect_factory import PointIntersectFactory

p1 = PointIntersectFactory.new_cartesian_point(2, 3)
p2 = PointIntersectFactory.new_polar_point(2, 3)
print(f"Cartesian result: {p1}")
print(f"Polar result: {p2}")
