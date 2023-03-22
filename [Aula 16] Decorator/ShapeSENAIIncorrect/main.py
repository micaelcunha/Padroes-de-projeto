from circle import Circle
from colored_shape import ColoredShape
from square import Square

circle = ColoredShape(Circle(5), 'red')
print(circle)
circle.resize(2)
print(circle)

square = ColoredShape(Square(2), 'blue')
print(square)
square.resize(2)
print(square)