def fib_series(n):
    if n==0 or n==1:
        return(n)
    else:
        return(fib_series(n-1)+ fib_series(n-2))
n=int(input("enter value:"))
for i in range(n):
    print(fib_series(i))