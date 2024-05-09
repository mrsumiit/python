'''def  add(a,b,c):
    return a+b+c
x=add(1,3,6)
print(x)

def heronce(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**(1/2)

x=heronce(2,5,4)
print(x)
'''
''''
a=int(input("enter your number-->"))
n=int(input("enter the number---"))
for x in range (1,n+1):
    table = x*a
    print(table)

    '''

'''def table(a,n):
    for x in range (1,n+1):
        table=x*a
        print(table)


x=table(2,10)
print(x)
y=table(7,10)
z=table(9,20)
j=table(15,10)'''

#multiply natural numbers
'''n=int(input("enter the value"))
prd=1
for x in range (1,n+1):
    prd=prd*x
print(prd)
if n<0:
    print("negative numbers")
elif n==0:
    print(1)
else:
    print("factorial")'''

'''def factorial(n):
    if n<0:
        print("")
    elif n==0:
        print()
    else:
        prd=1
        for n in range (1,n+1):
            prd=prd*n
    print(prd)
x=factorial(7)'''
'''
def armstrong (n):
    l=len(str(n))
    if (sum==n):
        print(n,"it is an armstrong no ")
    else:
        print(n,"it is not an armstrong no")
        l=len(str(n))
        sum=0
        t=n
    while t>0:
        d=n%10
        sum=sum+(d**l)
x=armstrong(145)'''
'''
def arst(n):

    l=len(str(n))
    sum=0
    t=n
    while t>0:
        d=t%10
        sum=sum+(d**l)
        t=t//10
    if(sum==n):
        print(n,"yes")
    else:
        print(n,"not")

n=arst(153)'''

def palendrome(given_string):
    
    reverse_string=""
    for i in given_string:
        reverse_string=i+reverse_string
    if (given_string==reverse_string):
        print("this string",given_string,"is a palindrome ")
    else :
        print("the string",given_string,"is not a palindrome")
given_string=palendrome("POP")

    


        






