import random

#l = list(range(5))
#print(l)
# [0, 1, 2, 3, 4]

#lr = random.sample(l, len(l))
#print(lr)
# [3, 2, 4, 1, 0]

#print(l)
# [0, 1, 2, 3, 4]

def pass_gen(list): #GENERATES PASSWORD
    u=""
    for i in range(8):
        g=list[i]
        if g not in(0,1,2,3,4,5,6,7,8,9):
            u=u+g
        else:
            u=u+str(g)
    return u
while True:
    print("press 1")
    op=int(input("enter ur option:"))
    if op==1:
        LISTM=list(range(8))
        LISTMR=random.sample(LISTM,len(LISTM))
        g=pass_gen(LISTMR)
        print("password:",g)
