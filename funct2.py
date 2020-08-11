class Parent:
    def __init__(self,name):
        print("Parent __init__",name)
class Parent2:
    def __init__(self,name):
        print("Parent2 __init__",name)

class Chil(Parent2,Parent):#super is executed for the 1st parent class mentioned
    def __init__(self):
        print("Child __init__")

        Parent.__init__(self,"Tithi")
        super().__init__("Tithi")
        super().__init__("Tithi")
class Child(Parent,Parent2):
    def __init__(self):
        print("Child __init__")

        Parent2.__init__(self,"Tithi")
        super().__init__("Tithi")
        super().__init__("Tithi")
Child_obj=Child()
print(Child.__mro__)
print("=================================================================================================================")
Child_ob=Chil()
#by default it will call __init__ of child

#method resolution order

print(Chil.__mro__)


# naming convention in python
# can't create constant so for our reference the constant sholud be in capital
