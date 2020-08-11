import polygon as p
class Triangle(p.Shape,p.Polygon):
    def area(self):
        return self.get_val()*self.get_valh()*1/2
