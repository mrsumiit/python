print("--------select your option--------")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.floor division")
print("6.modulus opertor")
print("7.** power function")
print("8.percentage")
print("9.percentage amount")
print("10.even")
print("11.(a+b)**2")
print("12.square")
print("13.cube")
print("14.SI")
print("15.cube root")
print("16.area of triangle")
print("17.area of rectangle")
print("18.area of cone")
print("19.area of cylinder")
print("20.area of cube")
print("21.volume of cube")
print("22.volume of cuboid")
print("23.volume of cylinder ")
print("24.volume of cone ")
print("25.(a-b)**2")
print("26.(a+b+c)*2")
print("27.a**2-b**2")
print("28.square root")

x=int(input("enter your number"))
if (x==1): #add
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   print(a+b)
elif (x==2): #subtract
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   print(a-b)
elif (x==3): #multiply
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   print(a*b)
elif (x==4):
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   print(a/b)
elif (x==5): #floor division
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   print(a//b)
elif (x==6): #modulus 
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   print(a%b)
elif (x==7): #power function
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   print(a**b)
elif (x==8): #percentage
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   p=(a/b)*100
   print(p)
elif (x==9): #percentage amount
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   p=(a/100)*b
   print(p)
elif (x==10): #even
   a=int(input("enter the value of a"))
   if(a%2==0):
      print("even")
   else:
      print("odd")
elif (x==11): #(a+b)**2
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   p=a**2+b**2+2*a*b
   print(p)
elif (x==12): #square
   a=int(input("enter the value of a"))
   p=a**2
   print(p)

elif (x==13): #cube
   a=int(input("enter the value of a"))
   p=a**3

elif (x==14): #si
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   c=int(input("enter the value of c"))
   p=(a*b*c)/100
   print(p)

elif (x==15): #cube root
   a=int(input("enter the value of a"))
   b=1/3
   print(a**b)

elif (x==16): #area of triangle 
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   p=(a*b)*1/2
   print(p)

elif (x==17): #area of rectangle
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   p=a*b
   print(p)

elif (x==18): #area of cone 
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   pie=22/7
   p=pie*a*a+pie*a*b
   print(p)

elif (x==19): #area of cylinder
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   pie=22/7
   p=2*pie*a*b+2*pie*a*a
   print(p)

elif (x==20): #area of cube
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   p=6*a*a
   print(p)

elif (x==21): #volume of cube 
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   p=a*a*a
   print(p)

elif (x==22): #volume of cuboid 
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   c=int(input("enter the value of c"))
   p=a*b*c
   print(p)

elif (x==23): #volume of cylinder 
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   pie=22/7
   p=pie*a*a*b
   print(p)

elif (x==24): #volume of cone
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   pie=22/7
   p=pie*a*a*b
   print(p)

elif (x==25): #(a-b)**2
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   p=a**2+b**2-2*a*b
   print(p)

elif (x==26): #(a+b+c)**2
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   c=int(input("enter the value of c"))
   p=a*a+b*b+c*c+2*(a*b+b*c+c*a)
   print(p)

elif (x==27): #a**2-b**2
   a=int(input("enter the value of a"))
   b=int(input("enter the value of b"))
   p=(a+b)*(a-b)
   print(p)

elif (x==28): #square root
   a=int(input("enter the value of a"))
   b=1/2
   print(a**b)



   


