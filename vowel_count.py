f=open("e:/movie.txt", "r")
l=f.readlines()
ctr=0
for k in l:
    q=k.split()
    for w in q:
        if w.isdigit() and w.isalnum:
            break
        else:
            for x in range(len(w)):
                if (w[x] in ["a","e","i","o","u"]):
                    ctr+=1
print(ctr)
f.close()
