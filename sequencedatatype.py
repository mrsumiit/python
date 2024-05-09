a=[1,2,3,4,5]
print(a)
print(type(a))

a=["a","b"]
print(a)
print(type(a))

a=[1,1]
print(a)
print(type(a))


print(a)
print(len(a))

a=[1,2,3,4,5]
print(a)
print(a[-3])
print(a[1:3])


#swipping two number

#before swapping
a=1
b=2
print("before swapping")
print(a,b)

#after swapping
c=a
a=b
b=c
print("after swapping")
print(a,b)


a=[1,2,3]
print(a)

a[2]=4
print(a)

a=[1,3]
print(a[0]*a[1])

#swapping two value using 3 variable
a=1
b=2
print("before swapping",a,b)

c=a
a=b
b=c

print("after swapping",a,b)

#swapping two value using 1 variable

a=[1,2]
print(a)

a[0]=2
a[1]=1
print(a)

print(len(a))


a=[1,2,3,4,5,6,7,8,9]
a[1:5]=[7,7,4,4]
print(a)




a=[2,4,3,5,6,4,7,8,4,1,2,9,0,7,6,5,4,3]
if 66 in a:
    print("yes")

else:
    print("no")


a=["a","b","c"]
a.insert(1,"d")
print(a)

a=[1,2,3,4]
a.insert(1,0)
print(a)

a.append(5)
print(a)


a=[1,2,3]
b=["a","b","c"]

a.extend(b)
b.extend(a)

print(a,b)

a=[1,2,3,4,5,6,7]
a.remove(2)
print(a)

del a[-1]
print(a)

del a
print(a)



a=[1]
a.remove(1)
print(a)
del a
print(a)

a=[]
print(a)


a=[1,2,3,4]

a.clear()

print(a)








