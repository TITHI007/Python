def sumf(arg1,arg2):
    print(arg1+arg2)


sumf(2,4)
sumf("1","World")

F=None
print(F)

def sumf(arg1,arg2,arg3):
    if((type(arg1)==type(arg2))and(type(arg1)==type(arg3)) ):
        return(arg1+arg2+arg3)
    else:
        return "INVALID"

print(sumf(5,7,5))
print(sumf("hss",7,5))
# print(sumf(9,7))
# print(sumf("hss",7))


#Positional arguement
def shop(item,price):
    print("Item",item)
    print("Price:",price)
shop("Sugar",40)
#error happens when place is misplaced
shop(40,"Sugar")
#solution
#Keyword arguement
def shop(item,price):
    print("Item",item)
    print("Price:",price)
shop(price=40,item="Sugar")

#Default arguement
def shop(item,price=20):
    print("Item",item)
    print("Price:",price)
shop("Sugar",)
shop("Sugar",90)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    # Variable length arguement
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def std(name,clas,*marks):
    print("Name",name)
    print("class",clas)
    print("Marks",marks)
std("Tithi",12,100,98,99,97)#result of marks is in tuple

#with Keyword
def std(name,clas,**marks):
    print("Name",name)
    print("class",clas)
    print("Marks",marks)
std("Tithi",12,Maths=100,English=98)#result of marks is in dictionary

def std(name,clas,**marks):
    print("Name",name)
    print("class",clas)
    for x in marks:
        print("Marks",x)
std("Tithi",12,Maths=100,English=98)#result of marks is in dictionary

def std(name,clas,**marks):
    print("Name",name)
    print("class",clas)
    for x,y in marks.items():
        print(x,":",y)
std("Tithi",12,Maths=100,English=98)#result of marks is in dictionary


def std(*name,clas,**marks):
    print("Name",name)
    print("class",clas)
    for x,y in marks.items():
        print(x,":",y)
std("Tithi","Riya",clas=12,Maths=100,English=98)#result of marks is in dictionary

def std(name,*clas,**marks):
    print("Name",name)
    print("class",clas)
    for x,y in marks.items():
        print(x,":",y)
std("Tithi",12,3,4,5,Maths=100,English=98)#result of marks is in dictionary


# Variable Global vs local
x=100
y=109

def varia(x,y):
    n=90
    global z
    z=98
    print(x)
    print(y)
    print(z)
    print(n)

varia(x,y)
print("------------------------")
print(x)
print(y)
print(z)#If  varia not called then error as the program doesnt know the z
# print(n)error as it is not global
