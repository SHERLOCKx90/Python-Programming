def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
def sum_series(n):
    if n==1:
        return 1
    else:
        return(1/fact(n)+ sum_series(n-1))
n=int(input())
s=sum_series(n)
print("sum=", s)