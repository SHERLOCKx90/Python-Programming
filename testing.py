'''import os
f=open("e:/teacher.txt","r")
g=open("e:/tempx.txt","w")
for L ini f:
    if L[0].upper() not in "AEIOU":
        g.write(L)
f.close()
g.close()
os.remove("e:/teacher.txt")
os.rename("e:/tempx.txt","e:/teacher.txt")
'''
'''f=open("e:/valentine.txt","r")
ctr=0
for L in f:
    ctr+=len(L)-1
print(ctr)
f.close()
'''

'''f=open("e:/valentine.txt","r")
print(f.readlines())
ctr=0
for l in f:
    ctr+=len(l)-1
print(ctr)
f.close()
f.readline()''' #displays the first line of the text file

#.readline() => displays each line of the text file
#.readlines() => displays all the lines of the text file

f=open("e:/valentine.txt","r")
ctr=0
l=f.readlines()
print(l)
f.close()
