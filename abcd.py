import pickle as p

f=open("e:/abcd.dat", "wb")
n=int(input("please enter the numb er of datas"))
for I in range(n):
    MOB={}
    print("please enter the following details:")
    MOB["modelno"]=input("enter the model number: ")
    MOB["mname"]=input("enter the model name:")
    MOB["price"]=int(input("enter the price of the model"))
    p.dump()
f.close()

#now, if we want to print the contents of the file:

f=open("e:/mobile.dat","rb")
M={}
While True:
    try:
        d=p.load(f)
        print(d)
    except:
        break
f.close()
