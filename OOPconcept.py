class Student:
    def __init__(self,name,*age,**marks):
        self.name=name
        self.age=age
        self.marks=marks
    # def __init__(self):
    #     print("Second init")

    # cant use to init in a class
    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)
class Vehicle:
    def __init__(cls,name):
        cls.name=name

    def display(cls):
        print(cls.name)



name=input()
age= int(input())
marks=int(input())

s=Student(name,age,30,40,33,SST=marks,Eng=100,MAth=50,Hind=99,Sci=98)
s.name="TITHI PATEL"
s.display()
c=Vehicle("Mercedes")
c.display()
