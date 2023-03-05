def sum_digits(n):
    if n==0:
        return 0
    else:
        return (n%10 + sum_digits(n//10))
n=int(input("enter any number::"))
print("sum of digits is::", sum_digits(n))