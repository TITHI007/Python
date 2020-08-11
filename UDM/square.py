import polygon as p
from polygon import Shape
class Square(p.Polygon,Shape):
    def area(self):
        return self.get_val()*self.get_valh()
