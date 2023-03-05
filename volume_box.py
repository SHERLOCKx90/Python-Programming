def volume(n):
    V=(20-(2*n))*(10-(2*n))*n
    return V
    
while True:
    print("press 1 to enter value:")
    op=float(input("enter value:"))
    z=volume(op)
    print("the volume:",z)
