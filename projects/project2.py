amt=int(input("enter the amount"))
if 10000<=amt<=20000:
    print("no intrest apply")
elif 20000<=amt<40000:
    
    time=int(input("enter the time"))
    rate=5
    SI=(amt*time*rate)/100
    print(SI)
