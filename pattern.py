while True:
    q= input("enter the odd/even progression:")
    n=int(input("enter the no. of lines "))
    if q in  ("odd", "ODD"):
        for i in range(n):
            for j in range(i):
                print("*" , end="*")
            print("@")
        

    elif q in ("even","EVEN"):
        for k in range(n):
            for e in range(k):
                print("*", end="**")
            print("@@")
        
