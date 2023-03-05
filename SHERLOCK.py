import time as t
import random as r
def regis():
    print("--- welcome to S H E R L O C K ---")
    #print("i am student from VIT chennai")
    b=input("enter  your name:")
    print("registering your name, please wait...")
    t.sleep(2)
    print("name registered successfully!")
    print("Hey...",b , end="")
    print("let's have fun!")
    return b

#main
while True:
    print("press 1 to play vs COM /n")
    print("press 2 to play vs user/n")
    print("press 3 to exit game")

    op=int(input("press any key..."))
    if op==1:
        c=regis()
        print("Hey...",c,"let's start the game!",end="")

