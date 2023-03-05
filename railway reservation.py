import pickle as p
import time as t
import random 

def add_ticket(d):
    f=open("e:/ax90.dat","ab")
    p.dump(d,f)
    print("Your ticket is being processed . . . . . ")
    t.sleep(3)
    print("Ticket has been generated!")
    f.close()
    
def show_ticket():
    file=open("e:/ax90.dat","rb")
    while True:
        try:
            rec=p.load(file)
            print("-----------------------------------------INDIAN RAILWAYS---------------------------------------------")
            print("------------------------------------------RAILWAY TICKET---------------------------------------------")
            print("------------------------------------------TRAIN DETAILS---------------------------------------------")
            print("TRAIN PNR: :", rec["PNR"])
            print("BATH NO.:", rec["B.NO"])
            print("------------------------------------------JOURNEY DETAILS---------------------------------------------")
            print("TRAVELLING FROM::", rec["from"], "TO" , rec["to"])
            print("------------------------------------------PASSENGER DETAILS---------------------------------------------")
            print("no. of passengers::",rec["no"])
            for k in range(rec["no"]):
                print("passenger name: :", rec["name"])
                print("passenger age: :", rec["age"])
                print("passenger sex: : ", rec["sex"])
                print("passenger ph.no", rec["ph.no"])
            print("-----------------------------------------MEAL DETAILS---------------------------------------------")
            print("meal service required ?", rec["ML.serv"])
            print("no. of meals: :", rec["no.ML"])
            print("no. of veg meals: :", rec["no.V"])
            print("no. of non-veg meals: :", rec["no.NV"])
            print("------------------------------------------SEAT DETAILS---------------------------------------------")
            print("searching for available seats . . . .")
            t.sleep(3)
            for m in range(rec["no"]):
                print("seat no.", rec["seat"])
            print("-----------------------------------------BILLING DETAILS---------------------------------------------")
            print("---------------   MEAL BILL   ---------------")
            print("no. of veg meals: :", rec["no.V"])
            print("cost::", rec["V.amt"])
            print("no. of non-veg meals: :", rec["no.NV"])
            print("cost::",rec["NV.amt"])
            print("TOTAL MEAL COST::",rec["ML.amt"])
            print("---------------TRAVELLING BILL---------------")
            print("TRAVELLING FROM::", rec["from"], "TO" , rec["to"])
            print("no. of passengers::",rec["no"])
            print("TRAVELLING COST::",rec["trv.amt"])
            print("**COMFORT FACILITY CHARGE::",rec["COMF.fac"])
            G=(rec["trv.amt"]+rec["COMF.fac"])
            print("TOTAL TRAVEL COST::",G)
            print("---------------   T O T A L   ---------------")
            print("TOTAL COST WO/-(any GST.)::",rec["bill"])
            print("CGST::",rec["CGST"])
            print("SGST::",rec["SGST"])
            print("IGST::",rec["IGST"])
            print("TOTAL(GST.)::",rec["GST"])
            print("TOTAL COST W/-(GST.)::",rec["TOT"])
            print("GST NO.",rec["GSTX"])
        except:
            print("-------------------------THANK YOU--------------------------------")
            break
    file.close()
    
def delete_ticket():
    PNR=int(input("enter the train PNR: :"))
    f=open("e:/ax90.dat","rb")
    l=[]
    while True:
        try:
            rec=p.load(f)
            l.append(rec)
        except EOFError:
            break
    f.close()
    for d in l:
        if (d["PNR"]==PNR):
            l.remove(d)
            print("cancelling ticket . . . .")
            t.sleep(3)
            print("your ticket is successfully cancelled!")
        else:
            print(". . .Ticket not found! . . .")
    f=open("e:/ax90.dat", "wb")
    for d in l:
        p.dump(d,f)
    f.close()

def modify_ticket():
    x=int(input("enter the train PNR: :"))
    f=open("e:/ax90.dat", "rb")
    l=[]
    while True:
        try:
            rec=p.load(f)
            l.append(rec)
        except EOFError:
            break
    f.close()
    for d in l:
        if (d["PNR"]==x):
            data={}
            print("press 1  to update JOURNEY details: :")
            print("press 2 to update PASSENGER details: :")
            print("press 3 to update MEAL details: :")
            op=int(input("enter your option::"))
            data["PNR"]=d["PNR"]
            data["B.NO"]=d["B.NO"]
            if op==1:
                print("---------UPDATE  J O U R N E Y  DETAILS----------")
                data["from"]=input("travelling from: :")
                data["to"]=input("travelling to: :")
                data["no"]=d["no"]
                for i in range(data["no"]):
                    data["name"]=d["name"]
                    data["age"]=d["age"]
                    data["sex"]=d["sex"]
                    data["ph.no"]=d["ph.no"]
                data["ML.serv"]=d["ML.serv"]
                if data["ML.serv"]==d["ML.serv"]:
                    data["no.ML"]=d["no"]
                    data["no.V"]=d["no.V"]
                    data["no.NV"]=d["no.NV"]
                    if ((data["no.V"]+data["no.NV"])>data["no.ML"]):
                        print("inserted meal details- invalid!Please check")
                    else:
                        data["V.amt"]=150*data["no.V"]
                        data["NV.amt"]=200*data["no.NV"]
                        data["ML.amt"]=(data["V.amt"]+data["NV.amt"])
                elif data["ML.serv"]==("no" or "NO"):
                    data["no.ML"]=0
                    data["no.V"]=0
                    data["no.NV"]=0
                    data["ML.amt"]=0
                    data["V.amt"]=0
                    data["NV.amt"]=0
                data["seat"]=d["seat"]
                data["trv.amt"]=d["trv.amt"]
                data["COMF.fac"]=d["COMF.fac"]
                data["bill"]=d["bill"]
                data["CGST"]=d["CGST"]
                data["SGST"]=d["SGST"]
                data["IGST"]=d["IGST"]
                data["GST"]=d["GST"]
                data["TOT"]=d["TOT"]
                data["GSTX"]=d["GSTX"]
            elif op==2:
                print("---------UPDATE  P A S S E N G E R  DETAILS----------")
                data["from"]=d["from"]
                data["to"]=d["to"]
                data["no"]=int(input("Number of passengers: :"))
                for i in range(data["no"]):
                    data["name"]=input("enter the name of the passenger: :")
                    data["age"]=int(input("enter the age of the passenger: :"))
                    data["sex"]=input("MALE / FEMALE / OTHERS ?")
                    data["ph.no"]=int(input("enter the phone no. of passenger: :"))
                data["ML.serv"]=d["ML.serv"]
                if data["ML.serv"]==d["ML.serv"]:
                    data["no.ML"]=data["no"]
                    data["no.V"]=d["no.V"]
                    data["no.NV"]=d["no.NV"]
                    if ((data["no.V"]+data["no.NV"])>data["no.ML"]):
                        print("inserted meal details- invalid!Please check")
                    else:
                        data["V.amt"]=150*data["no.V"]
                        data["NV.amt"]=200*data["no.NV"]
                        data["ML.amt"]=(data["V.amt"]+data["NV.amt"])
                elif data["ML.serv"]==("no" or "NO"):
                    data["no.ML"]=0
                    data["no.V"]=0
                    data["no.NV"]=0
                    data["ML.amt"]=0
                    data["V.amt"]=0
                    data["NV.amt"]=0
                data["seat"]=d["seat"]
                data["trv.amt"]=500*data["no"]
                data["COMF.fac"]=100*data["no"]
                data["bill"]=data["trv.amt"]+data["COMF.fac"]+data["ML.amt"]
                data["CGST"]=data["bill"]*0.09
                data["SGST"]=data["bill"]*0.09
                data["IGST"]=data["bill"]*0.18
                data["GST"]=(data["CGST"]+data["SGST"]+data["IGST"])
                data["TOT"]=data["GST"]+data["bill"]
                data["GSTX"]=d["GSTX"]
            elif op==3:
                print("---------UPDATE  M E A L  DETAILS----------")
                data["from"]=d["from"]
                data["to"]=d["to"]
                data["no"]=d["no"]
                for i in range(data["no"]):
                    data["name"]=d["name"]
                    data["age"]=d["age"]
                    data["sex"]=d["sex"]
                    data["ph.no"]=d["ph.no"]
                data["ML.serv"]=input("Do you want meal service?")
                if data["ML.serv"]==("yes" or "YES"):
                    data["no.ML"]=data["no"]
                    data["no.V"]=int(input("no. of veg meals ?"))
                    data["no.NV"]=int(input("no. of non-veg meals ?"))
                    if ((data["no.V"]+data["no.NV"])>data["no.ML"]):
                        print("inserted meal details- invalid!Please check")
                    else:
                        data["V.amt"]=150*data["no.V"]
                        data["NV.amt"]=200*data["no.NV"]
                        data["ML.amt"]=(data["V.amt"]+data["NV.amt"])
                elif data["ML.serv"]==("no" or "NO"):
                    data["no.ML"]=0
                    data["no.V"]=0
                    data["no.NV"]=0
                    data["ML.amt"]=0
                    data["V.amt"]=0
                    data["NV.amt"]=0
                data["seat"]=d["seat"]
                data["trv.amt"]=d["trv.amt"]
                data["COMF.fac"]=d["COMF.fac"]
                data["bill"]=data["trv.amt"]+data["COMF.fac"]+data["ML.amt"]
                data["CGST"]=data["bill"]*0.09
                data["SGST"]=data["bill"]*0.09
                data["IGST"]=data["bill"]*0.18
                data["GST"]=(data["CGST"]+data["SGST"]+data["IGST"])
                data["TOT"]=data["GST"]+data["bill"]
                data["GSTX"]=d["GSTX"]
            add_ticket(data)
            l.remove(d)
            l.append(data)
    f=open("e:/ax90.dat", "wb")
    for data in l:
        p.dump(data,f)
        print("updating ticket details . . . .")
        t.sleep(3)
        print("your ticket details has been successfully updated! ")
    f.close()


#main section
data={}
while True:
    print("press 1 to GENERATE ticket::")
    print("press 2 to show ticket::")
    print("press 3 to cancel ticket::")
    print("press 4 to update T/details::")
    op=int(input("enter your option::"))
    if op==1:
        data["PNR"]=random.randint(10000,99999)
        data["B.NO"]=random.randint(1,10)
        data["from"]=input("travelling from: :")
        data["to"]=input("travelling to: :")
        data["no"]=int(input("Number of passengers: :"))
        for i in range(data["no"]):
            data["name"]=input("enter the name of the passenger: :")
            data["age"]=int(input("enter the age of the passenger: :"))
            data["sex"]=input("MALE / FEMALE / OTHERS ?")
            data["ph.no"]=int(input("enter the phone no. of passenger: :"))
        data["ML.serv"]=input("Do you want meal service?")
        if data["ML.serv"]==("yes" or "YES"):
            data["no.ML"]=data["no"]
            data["no.V"]=int(input("no. of veg meals ?"))
            data["no.NV"]=int(input("no. of non-veg meals ?"))
            if ((data["no.V"]+data["no.NV"])>data["no.ML"]):
                print("inserted meal details- invalid!Please check")
            else:
                data["V.amt"]=150*data["no.V"]
                data["NV.amt"]=200*data["no.NV"]
                data["ML.amt"]=(data["V.amt"]+data["NV.amt"])
        elif data["ML.serv"]==("no" or "NO"):
            data["no.ML"]=0
            data["no.V"]=0
            data["no.NV"]=0
            data["ML.amt"]=0
            data["V.amt"]=0
            data["NV.amt"]=0
        data["seat"]=random.randint(1,1000)
        data["trv.amt"]=500*data["no"]
        data["COMF.fac"]=100*data["no"]
        data["bill"]=data["trv.amt"]+data["COMF.fac"]+data["ML.amt"]
        data["CGST"]=data["bill"]*0.09
        data["SGST"]=data["bill"]*0.09
        data["IGST"]=data["bill"]*0.18
        data["GST"]=(data["CGST"]+data["SGST"]+data["IGST"])
        data["TOT"]=data["GST"]+data["bill"]
        data["GSTX"]=random.randint(100000,999999)
        add_ticket(data)
    elif op==2:
        show_ticket()
    elif op==3:
        delete_ticket()
    elif op==4:
        modify_ticket()
    else :
            print("Err : Please choose from the specified options!")
        

        
    
