#import pickle as p
def create():
    f=open("e:/biomutant.txt","w")
    for i in range(2):
        a=input("enter greeting text:")
        f.write(a)
        f.write("  ")
    print("file successfully created!")
    f.close()
def openfile():
    f=open("e:/biomutant.txt","r")
    for line in f:
        print(line)
    print()
    f.close()
#main_section
while True:
    print("press 1 to create greet file:")
    print("press 2 to open greet file:")
    op=int(input("enter option:"))
    if op==1:
        create()
    elif op==2:
        openfile()
    else:
        print("invalid option!")
