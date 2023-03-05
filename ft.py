def READ():
    f=open("e:/sherlock.txt","r")
    for line in f:
        print(line)
    print()
    f.close()
#reads the file
#line by line
#prints line
#prints line by line
#reads the sherlock file
def WRITE(a):
    f=open("e:/sherlock.txt","a")
    while True:
        print("press 1 to enter text")
        print("press 2 to stop writing")
        op=int(input("enter choice : :"))
        if op==1:
            print("/n/n----TYPE TEXT----/n/n")
            f.write(/n)
            f.write(a)
            f.write(/n)
        elif op==2:
            print("THAT'S ALL!")
            break
        

#MAIN_SECTION
while True:
    q=input("//   want to write(y) or read(n)   // : :")
    if q="y":
        print("----WRITE FILE----")
        a=input("enter the text")
        WRITE(a)
    elif q="n":
        print("----READ FILE----")
        READ()
    else:
        print("invalid option...plz choose correctly!")

