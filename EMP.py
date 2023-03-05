import pickle as p
import time as t

def NewEmp(d):
    f=open("e:/EMP.dat","ab")
    p.dump(d,f)
    print("employee details are being processed , please wait . . . .")
    t.sleep(3)
    print("employee details is being added successfully!")
def SumSalary(p):
    f=open("e:/EMP.dat","rb")
    while True:
        try:
            rec=p.load(f)
            z=rec.values()
            s=0
            for i in range(len(z)):
                if z[2]==p:
                    print("=======EMPLOYEE=======")
                    print("employee no.:",z[0])
                    print("employee name:",z[1])
                    print("employee post:",z[2])
                    print("employee salary:",z[3])
                    print("=====================")
                    s=s+int(z[3])
    print("the sum of the salary:",s)
        except EOFError:
            print("thank you!")
            break
    f.close()
#main_section
data={}
while True:
    print("press 1 to input employee details:")
    print("press 2 to show the sum of the salary")
    op=int(input("enter the option"))
    if op==1:
        data["EmpNo"]=int(input("enter employee number:"))
        data["Ename"]=input("enter employee name")
        data["post"]=input("enter the employee post")
        data["salary"]=input("enter the salary of each employee")
        NewEmp(data)
    elif op==2:
        post=input("enter the post of the employee:")
        SumSalary(post)
    else:
        print("invalid choice ...please chose form the correct options!")
