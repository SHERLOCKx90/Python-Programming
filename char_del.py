import os

f=open("e:/venom.txt", "r")
g=open("e:/temp.txt","w")
k=input("enter the character: :")

for L in f:
    for p in L:
        if p.upper() not in k.upper():
            g.write(p)
f.close()
g.close()

os.remove("e:/venom.txt")
os.rename("e:/temp.txt","e:/venom.txt")
                
                
 
