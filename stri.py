x='                          hello word '
y='HELLO WORLD'

print(x.capitalize())
print(y.capitalize())

print("y="+y.lower())

print(x.upper())
# x[0]='i'TypeError: 'str' object does not support item assignment
# hence need to convert into list
print(x[1:4])#Slicing
print(y[-4:])#https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
print(x[0])#indexing
print(x.strip())#default left strip
print(x.strip())#default left strip
print(x.strip())#default left strip
print(x.strip())#default left strip
print(x.lstrip())
print(x.rstrip())
print(x.islower())# even if one letter in upper then also it will give false
print(y.isupper())#even if one letter in lower then also it will give false
x="Hello"
print(x.isupper())
print(x.replace("H","j"))

print(y.replace("Hello","jello"))
#need to match the whole word
print(y.replace("HELLO","jello"))
print(y)
#replacing single character

text="abcdefg"
new=list(text)
new[6]="w"
text="".join(new)
print(text)
#2nd and OPTIMIZE method
text="abcdefg"
text=text[:1]+'Z'+text[2:]
print(text)

#Split method

#https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/

print(y.split(" "))#result in the form of list
grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 0))
#maxsplit specified then the list will have max of maxsplit+1 items
print(x*100)
#using more than 1 function

x = "hello world example"

# replacing 'example' with 'project'
# after replacing converting all to uppercase characters
print(x.replace('example', 'project').upper())
#refer "https://www.programiz.com/python-programming/methods/string" for more string function
likes = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
print(likes.count("Likes"))
