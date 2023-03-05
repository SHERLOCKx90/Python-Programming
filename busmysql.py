import mysql.connector as mq
import random
import time


m=mq.connect(host="localhost",user="root", password="subhadeepchell12345", database="students")
mycur=m.cursor()


def create():
    name=input("Enter name")
    age=int(input("Enter age"))
    dest=input("Enter destination")
    init=input("Enter from:")
    a=input("Enter y or n for ac or nonac respectively")
    if a=="y":
        acnonac="ac"
    elif a=="n":
        acnonac="nac"
    doj=input("Enter date of journey")
    pid=random.randint(1000,9999)
    print("Your ticket id is:",pid)
    print("Your ticket is being processed....")
    if acnonac=="ac":
        price=500
    else:
        price=400
    sql="insert into bus values ('{}',{},'{}','{}','{}','{}',{},{})".format(name,age,dest,init,acnonac,doj,pid,price)
    mycur.execute(sql)
    m.commit()
    time.sleep(2)
    print("Ticket registered successfully")
    print()
    print()

    
def delete():
    pid=int(input("Enter your ticket id"))
    sql="delete from bus where pid={}".format(pid)
    mycur.execute(sql)
    m.commit()
    time.sleep(1)
    print("Your ticket has been deleted")


def modify():
    p=int(input("Enter your pid"))
    print("Press 1 to change name")
    print("Press 2 to change age")
    print("Press 3 to change destination")
    print("Press 4 to change from")
    print("Press 5 to change acnonac")
    print("Press 6 to change date of journey")
    op=int(input("Enter your option"))
    if op==1:
        n=input("Enter name")
        sql="update bus set name='{}' where pid={}".format(n,p)
        mycur.execute(sql)
        m.commit()
    elif op==2:
        a=int(input("Enter age"))
        sql="update bus set age={} where pid={}".format(a,p)
        mycur.execute(sql)
        m.commit()
    elif op==3:
        d=input("Enter destination")
        sql="update bus set destination='{}' where pid={}".format(d,p)
        mycur.execute(sql)
        m.commit()
    elif op==4:
        i=input("Enter from")
        sql="update bus set initial='{}' where pid={}".format(i,p)
        mycur.execute(sql)
        m.commit()
    elif op==5:
        a=input("Enter y or n for ac or nonac respectively")
        if a=="y":
            an="ac"
            price=500
        elif a=="n":
            an="nac"
            price=400
        sql="update bus set acnonac='{}', price={} where pid={}".format(an,price,p)
        mycur.execute(sql)
        m.commit()
    elif op==6:
        doj=input("Enter date of journey")
        sql="update bus set doj='{}' where pid={}".format(doj,p)
        mycur.execute(sql)
        m.commit()
    time.sleep(2)
    print("Your ticket is updated")


def   show():
    p=int(input("Enter ticket id:"))
    sql="select * from bus where pid={}".format(p)
    mycur.execute(sql)
    s=mycur.fetchall()
    for i in s:
        print()
        print("------------TICKET DETAILS----------")
        print("Name:",i[0])
        print("Age:",i[1])
        print("Destination:",i[2])
        print("Initial:",i[3])
        print("AC/NON AC:",i[4])
        print("Date of journey:",i[5])
        print("Price:",i[7])
        print("Ticket id:",i[6])
        print()

#MAIN SECTION
while True:
    print("press 1 to GENERATE ticket::")
    print("press 2 to delete ticket::")
    print("press 3 to modify ticket::")
    print("press 4 to show T    /details::")
    op=int(input("enter your option::"))
    if op==1:
        create()
    elif op==2:
        delete()
    elif op==3:
        modify()
    elif op==4:
        show()
    else:
        print("INVALID OPTION")
