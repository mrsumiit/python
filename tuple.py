a=(1,2,3)
print(a)
print(a[0])
print(type(a))




a=(1,2,3,4,5)
print(a[1:5])

a=(1,2,3,4,5)
if 3 in a:
    print("yes")
else:
    print("no")



a=(2,3,4)
b=("a","b")
c=a+b
print(c)


#type conversion
#int ---> float
a=6
b=float(a)
print(a,b)

#float---> int

a=6.4
b=int(a)
print(a,b)


#how to add element in tuple
a=(1,2,3,4,5,6,7,8)
print(a)
b=list(a)
b.insert(3,"hello")
a=tuple(b)
print(a)

a="1+2"
b=1+2
print(a,b)




a={1,2,3,4,4,5,6,7,8,9}
a.remove(3)
print(a)

b={5,6,7,8,9}

#a.extend(b) not use 
#c=a+b
c=a.union(b)
print(c)

c=a.difference(b)
print(c)






