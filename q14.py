'''f=open("e:/Story (2).txt","r")
def Search_word():
    for L in f:
        w=L.split()
        for i in w:
            for j in i:
                if i[j] and  i[j+1]=="s" and "h":
                    print(i)
Search_word()
f.close()
p=26
for i in range(p):
    if i==25:
        Break
    else:
print(i ,end=" ")
import random as r
City=["DEL","CHN","KOL","BOM","BNG"]
Fly=0
for i in range(0,3):
    Fly=r.randint(0,1) + 1
    print(City[Fly],":",end="")
st="ThIsIsOuT@Put1452"
s=""
q=""
x=st[0:9]
y=st[len(x)::]
s=y+x
s=s[::-1]
for i in s:
    if i.isupper():
        q=q+i.lower()
    elif i.islower():
        q=q+i.upper()
    elif i.isdigit():
        q=q+str(int(i)+2)
    else:
        q=q+"#"
print(q)
print(y)'''
'''p=(1,2,3,4)
print(p[2::])'''
'''a="Hem Sheela Model School"
print(a.find("el",0,len(a)))'''
'''H = (10,23,22,44)
print(sum(H))'''
'''k=("Antidisestablishmentarianism"[5:19])[2:7]
print(k)'''

