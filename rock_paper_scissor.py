import random

def game_check(n,u,c):
    List=["R","P","S"]
    j=random.randint(0,2)
    b=List[j]
    if n==b: #DRAW CASES
        if n=="R" and b=="R":
            print(" MOVES DRAW!")
            print("your move :", "ROCK", end="")
            print("computer's move :", "ROCK", end="")
            u+=0
            c+=0
        elif n=="P" and b=="P":
            print(" MOVES DRAW!")
            print("your move :", "PAPER", end="")
            print("computer's move :", "PAPER", end="")
            u+=0
            c+=0
        elif n=="S" and b=="S":
            print(" MOVES DRAW!")
            print("your move :", "SCISSOR", end="")
            print("computer's move :", "SCISSOR", end="")
            u+=0
            c+=0
    elif n!=b: #WIN OR LOSS CASES
        if n=="R" and b=="P":
            print(" COMP'S 1 POINT !")
            print("your move :", "ROCK", end="")
            print("computer's move :", "PAPER", end="")
            u=u+0
            c=c+1
        elif n=="R" and b=="S":
            print(" YOUR'S 1 POINT !")
            print("your move :", "ROCK", end="")
            print("computer's move :", "SCISSOR", end="")
            u=u+1
            c=c+0
        elif n=="P" and b=="R": 
            print(" YOUR'S 1 POINT !")
            print("your move :", "PAPER", end="")
            print("computer's move :", "ROCK", end="")
            u=u+1
            c=c+0
        elif n=="P" and b=="S":
            print(" COMP'S 1 POINT !")
            print("your move :", "PAPER", end="")
            print("computer's move :", "SCISSOR", end="")
            u=u+0
            c=c+1
        elif n=="S" and b=="R":
            print(" COMP'S 1 POINT !")
            print("your move :", "SCISSOR", end="")
            print("computer's move :", "ROCK", end="")
            u=u+0
            c=c+1
        elif n=="S" and b=="P":
            print(" YOUR'S 1 POINT !")
            print("your move :", "SCISSOR", end="")
            print("computer's move :", "PAPER", end="")
            u=u+1
            c=c+0
    print("**----FINAL SCORE----**")
    print("YOUR POINTS : :",u)
    print("COMPUTER'S POINTS : :", c)
    if u>c:
        print("HURRAY !! YOU WIN !!!")
    elif u==c:
        print("MATCH DRAW!")
    elif u<c:
        print("COMPUTER WIN...better luck next time!")
        
            
            
            
            
            
        
        
    
#main section
u=0
c=0
while True:
    print( "------------ROCK , PAPER , SCISSOR-----------")
    print("press R for ROCK")
    print("press P for PAPER")
    print("press S for SCISSOR")
    op1=int(input("For how many points do you want to play?"))
    for i in range(op1):
        op=input("enter your choice: :")
        game_check(op,u,c)
