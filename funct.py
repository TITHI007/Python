class Parent:
    def __init__(self,name):
        print("Parent __init__",name)
class Child(Parent):
    def __init__(self):
        print("Child __init__")
# method 1 to call parent class __init__
        Parent.__init__(self,"Tithi")
# method 2 to call parent class __init__
# here when you use super we don't need to use self
        super().__init__("Tithi")

Child_obj=Child()
#by default it will call __init__ of child

#method resolution order
print(Child.__mro__)
