from CQs.cq09.point import Point

a1: Point = Point(2.0, 4.0)
a1.scale_by(3)
print(a1.x)
print(a1.y)
a2: Point = a1.scale(3)
print(a2.x)
print(a2.y)
print(a1.x)
print(a1.y)
