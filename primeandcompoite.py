a=int(input("enter any number :"))
if a>1:
    for i in range(2,a):
      if a%i==0:
            print(a,"is not prime number ")
            break
    else:
        print(a,"is a prime number")
elif a==0 or a==1:
    print (a,"is neither prime nor composite")
