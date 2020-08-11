from square import Square as s
import tiangle as t
from polygon import Volume as v

v1=v()
v1.set_value(9,10)
print(v1.Volume())

s1=s()
s1.set_value(8,15)
s1.set_valu("Red")
print(s1.area(),s1.get_va())
# s2.set_value(8,15)
# print(s1.area())
t1=t.Triangle()
t1.set_value(8,15)
t1.set_valu("Blue")
print(t1.area(),t1.get_va())

# p1=Polygon()
# p1.set_value(3,5)
# print(p1.disp())
