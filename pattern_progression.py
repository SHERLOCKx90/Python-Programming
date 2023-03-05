while True:
    q= input("enter the odd/even progression:")
    n=int(input("enter the no. of lines "))
    if q in  ("odd", "ODD"):
        for i in range(1,n+1):
            for j in range(1,i+2):
                print("*" , end="")
            print("@")
        

    elif q in ("even","EVEN"):
        for k in range(1,n+1):
            for e in range(1,k+1):
                print("*", end="*")
            print("@@")

