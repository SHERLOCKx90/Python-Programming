f=open("e:/movie.txt", "r")
d=f.read()
w=d.split()
for i in w:
    if i[0]=="m":
        print(i)
'''ctr=0
for line in f:
    ctr+=len(line)-1
print(ctr)'''
print()
f.close()
'''
import time as t
import pickle as p
f=open("e:/venomx.dat","ab")
List=[]
for i in range(5):
    a=int(input("enter the number:"))
    List.append(a)
p.dump(List,f)
print("data is being processed...")
t.sleep(3)
print("data is being processed!")
f.close()
'''
