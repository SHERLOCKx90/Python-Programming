import pickle as p
f=open("e:/binfile.dat", "ab")
data={}
data["text"]=input("enter text")
p.load(data,f)
f.close()
f=open("e:/binfile.dat","rb")
while True:
    try:
        rec=p.load(f)
        print(rec["text"])
    except EOFError:
        print("that's all?!!")
        break
f.close()
