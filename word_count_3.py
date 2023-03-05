f=open("e:/FUN.txt", "r")
c=0
for L in f:
    w= L.split()
    for i in w:
        if len(i)==3:
            c=c+1
print("no. of 3 lettered words:", c)
