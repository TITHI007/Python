a=(10,15,20,25,30)
print(a[0])
b=(10,20,10,[10,3],0)
print(b.count(10))
print(b[3].count(10))
print(all(b))
print(any(b))
print(len(b))
# print(min(b))#not supported as list is present data type should be same
print(max(a))
print(sum(a))
c=enumerate(a)
d=enumerate(b)
print(list(c))
print(list(d))
print(sorted(a))# cant do with be as no same datatype
n=[1,54,23,2,3,]
print(tuple(n))
