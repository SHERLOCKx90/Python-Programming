def count():
    print("count the no. of special symbols?   press 1")
    print("count the no. of lines started with vowel?   press 2")
    op=int(input("enter the option : :"))
    if op==1:
        f=open("e:/sherlock.txt","r")
        ctr=0
        d=f.read()
        if d.isalnum!=True:
                ctr=ctr+1
        print("the no. of special symbols are : :",ctr)
        f.close()
    elif op==2:
        f=open("e:/sherlock.txt","r")
        xyz=0
        u=["a","e","i","o","u"]
        v=["A","E","I","O","U"]
        d=f.readlines()
        for l in d:
            if l[0] in u or v :
                xyz=xyz+1
        print("the no. of lines started with a vowel : :",xyz)
        f.close()
    else:
        print("err. ivalid option!")
            
def display():
    
    print("display all the words started with 'P' ? press 1")
    #print()
    #print()
    op==int(input("enter your option : :"))
    if op==1:
        f=open("e:/sherlock.txt","r")
        print("the words starting with 'P' or 'p' : :")
        d=f.read()
        w=d.split()
        for i in w:
            if i[0]==("P" or "p"):
                print(i)
            print()
        f.close() 
#main_section
while True:
    print("press 1 to count the content")
    print("press 2 to display the required content")
    op=int(input("enter the option : :"))
    if op==1:
        count()
    elif op==2:
        display()
    else:
        print("err. please enter from the valid options!")
