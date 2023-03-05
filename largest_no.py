def largest(a,b):
    if a>b:
        return a
    else:
        return b
def max_list(L,n):
    if n==0:
        return L[0]
    else:
        return(largest(L[n], max_list(L,n-1)))
List=[11,2,93,4,15,6]
z=max_list(List,5)
print("largest element=",z) 