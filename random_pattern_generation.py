import pickle as p
import time as t

def xyz(d):
    f=open("f:/venom.dat", "ab")
    p.dump(d,f)
    print("your data is being recorded . . .")
    t.sleep(2)
    print("data successfully recorded!")
    f.close()

#main_section
data={}
while True:
    print(" press 1 to enter the no. of lines to generate : :")
    print(" press 2 to show the output : :")
    op= int(input("enter your option : "))
    if op==1:
        w=int(input("enter the required no. of lines : "))
        q=input("enter odd/even progression : ")
        for  i in range(w):
            for j in range(i):
                print()
            
    
