#object oriented programming system
#data hiding and encapsulation
class Speed:
    def __init__(self):
        self.speed =10
        self.__new_speed=80#"__" it means private
    # def display():
    #     pri
    def _get_speed(self):
        #using getter
        return self.__new_speed
    def _set_speed(self,n):
        #using setter to set the value
        self.__new_speed=n

car=Speed()
print(car.speed)
car.speed=20
print(car.speed)
print(car._get_speed())
# car.__new_speed=20
# print(car.__new_speed)
car._set_speed(99)
print(car._get_speed())
print("-----------------------------------------------------------------------------------------------------")
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#             private method
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Example:
    def __init__(self):
        self.x=10
        self._y=9
        self.__z=100
    def public_method(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__private_method()

    def __private_method(self):
        print("In private function")

eg=Example()
eg.public_method()
print("-----------------------------------------------------------")
# x=10
# _y=9
# __z=100
# def public_method():
#     print(x)
#     print(_y)
#     print(__z)
#     # __private_method()
#
#
#
#
# public_method()
#
# # def __private_method():
# #     print("In private function")
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                                   Inheritence
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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
class Square(Polygon):
    def area(self):
        return self.get_val()*self.get_valh()
    # def displ(self):
    #     return self.__width here the private member cant acces..
class Triangle(Polygon):
    def area(self):
        return self.get_val()*self.get_valh()*1/2

s1=Square()
s1.set_value(8,15)
print(s1.area())

t1=Triangle()
t1.set_value(8,15)
print(t1.area())

p1=Polygon()
p1.set_value(3,5)
print(p1.disp())
