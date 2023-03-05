top=-1
STACK=[]
size=50

def PUSH(STACK,top):
    if top==(size-1):
        print("stack overflow")
        return
    N=int(input("enter any number"))
    STACK.append(N)
    top+=1
    return top

def POP(STACK, top):
    if top==-1:
        print("stack is empty")
        return
    print("deleted element is", STACK[top])
    STACK.pop(top)
    top-=1
    return top
def Traverse(STACK, top):
    if top==-1:
        print("stack is empty")
        return
    for I in range(top,-1,-1):
        print(STACK[I])
#main section
while True:
    print("press 1 for push")
    print("press 2 for pop")
    print("press 3 for traverse")
    print("prfess 4 for exit")
    print("enter your option")
    op=int(input())
    if op==1:
        top=PUSH(STACK,top)
    elif op==2:
        top=POP(STACK,top)
    elif  op==3:
        Traverse(STACK,top)
    else:
        break