def Change():
    w=''
    for i in range(len(p)):
        if s[i]>p[i]:
            w=w+s[i]
        elif s[i]<p[i]:
            w=w+p[i-1]
        else:
            w=w+s[i]+p[i]
    print(w)
s='Data-analysis'
i=5
p=s[5:len(s)-(i%3)]
Change()
print(p)