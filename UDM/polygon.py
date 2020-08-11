class Polygon:
    __width=None
    __height=None

    def set_value(self,width,height):
        self.__width=width
        self.__height=height
    def get_val(self):
        return self.__width
    def get_valh(self):
        return self.__height
    def disp(self):
        return self.__width

class Volume(Polygon):
    def Volume(self):
        return self.get_val()*self.get_valh()*100

class Shape:
    __color=None

    def set_valu(self,color):
        self.__color=color
    def get_va(self):
        return self.__color
