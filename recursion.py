def sum(n):
    if n==1:
        return 1
    else:
        return(n+sum(n-1))
#main section
a=int(input("enter the no. of values:"))
z=sum(a)
print("the sum of the natural numbers upto given limit:", z)