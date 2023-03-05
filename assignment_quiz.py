import time 

def qs():
    question=[]
    qsn=int(input("Question Number:"))
    qs=input("Question :")+"?"
    options=[]
    i=1
    while True:
        a=input("Option %d: "%i)
        if a=="":
            break
        options.append(a)
        i+=1
    qsc=int(input("Correct Option :")) 
    question=[qsn,qs,options,qsc]
    return question
    
def create(x):
    r=int(input("\nEnter no. of questions:"))
    print("----------------")
    for i in range(r):
        print("---------------------------")
        print("\nQuestion ",(i+1))
        print("---------------------------")
        L=qs()
        x.append(L)
    print("\nQuestions Created")

def display(x):
    score=0
    for i in x:
        print(str(i[0])+"》",end="")
        print(i[1])
        for j in i[2]:
            k=1
            print(k,". ",j)
            k+=1
        ans=input("\nEnter Answer: ")
        time.sleep(1)
        if ans==i[3]:
            score+=1
    time.sleep(1.5)
    print("Your Total Score :",score)

# M A I N S ....

L=[]
create(L)
ch=input("\nReady For Test ?")
if ch.upper()=="YES":
    display()