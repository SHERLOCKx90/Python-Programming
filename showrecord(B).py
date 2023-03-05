import pickle as p
import time as t

def showrecord(d):
    f=open("e:/emp.dat","rb")
    rec=p.load(f)
    print("showing record...")
    t.sleep(2)
    print("employee ID : :", rec["ID"])
    print("name of the employee  : : ", rec["name"])
    print("salary of the employee : : ", rec["salary"])
    print("ph.no of the employee : : ", rec["ph.no"])
    f.close()
    
def addrecord(d):
    f=open("e:/emp.dat","ab")
    p.dump(d,f)
    print("data is being recorded...")
    t.sleep(2)
    print("adding record--successful")
    f.close()

'''def deleterecord(d):
    ID=int(input("enter the ID of the employee: :"))
    f=open("e:/emp.dat", "rb")
    I=[]
    while True:
        try:
            rec=p.load(f)
            I.append(rec)
        except EOFError:
            break
    f.close()           
    for d in I:
        if (d["ID"]==ID):
            I.remove(d)
            print("cancelling the record...")
            t.sleep(2)
            print("record successfully cancelled!")
        else:
            print("record not found!")
    f=open("e:/emp.dat", "wb")
    for d in I:
        p.dump(d,f)
    f.close()

def modifyrecord(d):
    x=int(input("enter the ID of the employee:"))
    f=open("e:/emp.dat" , "rb")
    L=[]
    while True:
        try:
            rec=p.load(f)
            L.append(rec)
        except EOFError:
            break
    f.close()
    for d in L:
        if (d["ID"]==x):
            data={}
            print("press 1 to update NAME details:")
            print("press 2 to update PH.NO details:")
            op=int(input("enter your option:"))
            data["ID"]=d["ID"]
            data["salary"]=d["salary"]
            if op==1:
                print("--update NAME details--")
                data["name"]=input("enter employee name:")
                data["ph.no"]=d["ph.no"]
            elif op==2:
                print("--update PH.NO details--")
                data["name"]=d["name"]
                data["ph.no"]=int(input("enter the ph.no of the employee:"))
            else:
                print("employee ID invalid!")
            addrecord(data)
            L.remove(d)
            L.append(data)
    f=open("e:/emp.dat", "wb")
    for data in L:
        p.dump(data,f)
        print("updating record details...")
        t.sleep(2)
        print("your record details has been successfully updated!")
    f.close()'''
   
#main section
data={}
while True:
    print("press 1 for adding record:")
    print("press 2 for showing record:")
    print("press 3 for deleting record:")
    print("press 4 for modifying record: ")
    op=int(input("enter your option:"))
    if op==1:
        print("please enter the employee details :")
        data["ID"]=input("enter the ID of the employee :")
        data["name"]=input("enter the name of the employee :")
        data["salary"]=int(input("enter the salary of the employee :"))
        data["ph.no"]=int(input("enter the ph.no. of the employee :"))
        addrecord(data)
    elif op==2:
        showrecord(data)
    elif op==3:
        deleterecord(data)
    elif op==4:
        modifyrecord(data)
    else:
        print("choose  from the specified options")
