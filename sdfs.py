'''lst =[2,1,4,6,12]
print(sum(lst))
print(sum(lst[0:3]))
print(sum(lst[1:4]))

data= list(map(int,input().split()))
print(data)'''


def checksum(data):
    s=0
    for i in range(len(data)):
        s=s+data[i]
        checksum=s
    print(checksum)
    
def individualsum(z):
    c=0
    for l in range(len(z)):
        c=c+z[l]
    print(c)

def encrypt(List):
    d=int(input("enter the sum of digits :"))
    for m in range(len(List)):
        List[m]=List[m] + d
    print("partial encrypted list : :",List)
    x=List.append(d)
    print("the complete encrypted data list : :",x)
    #return List
    
#main_section
print("enter data numbers :")
data=list(map(int,input().split()))
while True:
    print("press 2 to checksum :")
    print("press 3 to individualsum :")
    print("press 4 to encrypt data : ")
    op=int(input("enter your option :"))
    if op==1:
        data=list(map(int,input().split()))
    elif op==2:
        checksum(data)
    elif op==3:
        print("enter the checksum_digits separated with space :")
        z=list(map(int,input().split()))
        individualsum(z)
    elif op==4:
        data_list=encrypt(data)
    else:
        print("invalid option!")
