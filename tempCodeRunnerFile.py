def list_permutations(lst):
	if len(lst) == 0: 
		return [] 
	if len(lst) == 1: 
		return lst 
	l = []  
	for i in range(len(lst)): 
        m=lst[i]
        remLst =(lst[:i]+lst[(i+1):]) 
        for p in permutation(remLst): 
            l.append([m] + p) 
	return l 

# Driver program to test above function
List=[]
n=int(input("no. of elements::"))
for i in range(n):
    List.append(int(input("enter any digit:")))
print("----all permutations are----")
list_permutations(List)