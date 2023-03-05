def abc(n):
    a=input("enter subject")
    if a=="maths":
        b=int(input("enter the marks in maths I"))
        c=int(input("enter the marks in maths II"))
        d=b+c
        while True:
            try:
                if d<=80:
                    e=d/80*100
                else:
                    print("invalid marks taken..check it out again.")
            except:
                break
        print("MATHEMATICS MARKS : ",d ,"/ 80", end="")
        print("MATHEMATICS PERCENTAGE:", e, end="")
    else:
        print("out!")
#main section
while True:
    print("press 1 to review score")
    op=int(input("enter 1"))
    if op==1:
        abc(op)
    else:
        print("invalid!")
