import os
f=open("e:/STORY.txt","r")
g=open("e:/temp.txt","w")
z=f.read()
for i in z:
    d=z[::-1]
    g.write(d)
f.close()
g.close()

os.remove("e:/STORY.txt")
os.rename("e:/temp.txt","e:/STORY.txt")
