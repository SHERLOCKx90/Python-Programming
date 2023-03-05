1
'''f=open("e:/resources.txt","r")
r=f.readlines()
while True:
    try:
        a=int(input("enter no."))
        for i in range(len(r)):
            if a==1:
                print(r[0])
                print("click the link to get your required pdf file")
                print()
                break
            elif a==2:
                print(r[1])
                print("click the link to get your required pdf file")
                break
            elif a==3:
                print(r[2])
                print("click the link to get your required pdf file")
                break
            else:
                print("invalid")
                break
    except EOFError:
        print("thank you!")
        break
f.close()'''
d={}
list=[]
for i in range(4):
    a=int(input("enter any number"))
    list.append(a)
d["marks"]=list
print(d)1
