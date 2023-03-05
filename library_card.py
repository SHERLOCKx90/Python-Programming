import random
import time as t
import pickle as p


def small_make(): #GENERATES SMALL LETTER DIGITS
    LIST1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    P=random.randrange(0,len(LIST1))
    v=LIST1[P]
    return v
def CAPS_make(): #GENERATES CAPITAL LETTER DIGITS
    LIST2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    P=random.randrange(0,len(LIST2))
    v=LIST2[P]
    return v
def digits(): #GENERATES DIGITS
    LIST3=[1,2,3,4,5,6,7,8,9,0]
    P=random.randrange(0,len(LIST3))
    v=LIST3[P]
    return v
def symbol(): #GENERATES SYMBOLS
    LIST4=["@","#","$","%","^","&","*","~","-"]
    P=random.randrange(0,len(LIST4))
    v=LIST4[P]
    return v
def pass_gen(list): #GENERATES PASSWORD
    u=""
    for i in range(8):
        g=list[i]
        if g not in(0,1,2,3,4,5,6,7,8,9):
            u=u+g
        else:
            u=u+str(g)
    return u
def check_pass(d,f): #CHECKS THE PASSWORD
    if d[0]==f:
        return False
    elif f in d:
        return True
    else:
        d.append(d)
        return False

def random_pass(list): #RANDOMIZES THE POSITION OF THE CHARACTERS OF DIFFEREENT CLASS
    LS=random.sample(list, len(list))
    return LS
    



#main section
data=[]
while True:
    print("press 1 to generate library card")
    print("press 2 to show the library card")
    print("press 3")
    op=int(input("enter the option:"))
    if op==1:
        LISTM=[]
        for j in range(3):
            Z=small_make()
            LISTM.append(Z)
        for j in range(2):
            d=CAPS_make()
            LISTM.append(d)
        
        for j in range(2):
            c=digits()
            LISTM.append(c)
        
        for j in range(1):
            f=symbol()
            LISTM.append(f)
        LISTMR=random_pass(LISTM)
            
        f=pass_gen(LISTMR)
        data.append(f)
        print("please wait while your card is being generated . . . ")
        t.sleep(2)
        print("your library card is generated!")
        t.sleep(1)
        if check_pass(data, f)==True:
            g=pass_gen(LISTMR)
            print("the LIB_CODE is:", g)
        else:
            print("the LIB_CODE is:", f)
    elif op==2:
        print("done 2")
    elif op==3:
        print("done 3")
    else:
        print("wrong option!")
