def compare_last_digit(n1,n2):
    if n1%10 < n2%10:
        return n1
    else:
        return n2
p=int(input("enter first number:"))
q=int(input("enter second number:"))
print("minimum one's digit no.is:", compare_last_digit(p,q))
