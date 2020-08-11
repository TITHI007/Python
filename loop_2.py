'''n=int(input("number you want to enter:"))
for i in n:
    i=int(input("number"))

for i in n:
    print(i)
'''
#dictionary
E={
     "Riya":"English",
     "Tirt":12
   }

for i in E.items():
  print(i)
#list
A=[3,31,23,34,42,51,56]

for i in range(2,5):
       print(A[i])
#dictionary input
class_list = dict()
data = input('Enter name & score separated by ":" ')
temp = data.split(':')
print(type(temp))
class_list[temp[0]] = temp[1]
# Displaying the dictionary
for key, value in class_list.items():
	print('Name: {}, Score: {}'.format(key, value))

#multiple dictionary input
n = int(input("Number of Items You Want To Add: "))
my_dict =dict()
a=dict()
for i in range(0,n):
  i = input('Enter name & score separated by ":" ')
  temp = i.split(' ')
  my_dict[temp[0]] = temp[1]


print("------------------------------------------")
for key, value in my_dict.items():
	print(' {}:{}'.format(key, value))
#multiple list input
n = int(input("Number of Items You Want To Add: "))
my_list = []

for i in range(0,n):
    i = int(input("Enter input: "))
    my_list.append(i)

print(my_list)
