

import numpy as np
a=np.array([11,22,33])
b=np.array([44,55,66])
print(a,b)
print(a+b)
print(a-b)
print(a*2)

import numpy as np
a=np.array([1,2,3,3.4])
print(a)



list=[11,22,33]
list1=[33,66,88]
print(a,b)
print(list+list1)

import numpy as np
a=np.array([[1,2,3,4,5,6,7,8],[5,6,7,2,2,8,9,10]])
print(type(a))
#slicing
print(a[0:4,0:3]) #because show equal no. of row and column
print(a[0,1:4])
print(np.shape(a))
print(np.size(a))
print(np.ndim(a))
print(a.dtype)
print(type(a))
print(len(a))
print(a.astype(float))
print(a.astype(int))


#concatenate array(numpy)
import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([3,4,5,6,7,8])
print(np.concatenate([a,b]))
print(np.concatenate([a,b]))
print(a+b)


import numpy as np
a=np.array([1,2,3,4,5,6])
print(np.append(a,90))

b=np.array([[1,2,3,4],[1,2,3,4]])
print(np.append(a,[99,77]))

print(np.insert(a,1,6))  #array,index,value
print(np.insert(b,1,[1,2,39,4]))
print(b)

print(a)
print(np.delete(a,1))

print(b)
print(np.delete(b,1,axis=1))
#sort itterate and search
import numpy as np
a=np.array([4,2,6,5,4,7,8,7,5,2])
print(np.sort(a))
print(np.where(a==7))

#all even no in array


import numpy as np 

list1=[10,7,8,9,12]
arr=np.array([10,7,8,9,12])
mean1=np.mean(arr)
print(mean1)


list2=[17,6,11,15,7.9]
arr=np.array([17,6,11,15,7.9])
mean2=np.mean(arr)
print(mean2)

x=max(mean1,mean2)
print(x)
x=min(mean1,mean2)
print(x)

list1=[10,7,8]
arr=np.array([10,7,8])
mean1=np.mean(arr)
print(mean1)

list2=[12,7,9]
arr=np.array([12,7,9])
mean2=np.mean(arr)
print(mean2)

list3=[16,17,1]
arr=np.array([16,17,1])
mean3=np.mean(arr)
print(mean3)

x=max(mean1,mean2,mean3)
print(x)
x=min(mean1,mean2,mean3)
print(x)









