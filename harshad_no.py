def check_harsh(n):
    s=0
    p=n
    while p!=0:
        s=s+p%10
        p=p//10

    if n%s==0:
        return True
    else:
        return False
def remove_harsh(L):
    size=len(L)
    i=0
    while i< size:
        if check_harsh(L[i]):
            L.pop(i)
            i=i-1
            size=size-1
        i=i+1
list=[]
n=int(input("enter the no. of elements:"))
for i in range(n):
    list.append(int(input("enter any integer no::")))
print("\n before deletion elements are::", list)
remove_harsh(list)
print("\n after deletion elements are::", list)

