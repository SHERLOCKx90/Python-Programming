def create_nested(Arr):  #an user defined function, named create_nested, is created.
    x=[]  #empty list is created
    x.append(Arr)  #the user defined array in the main section, has been appended into the variable X.
    for j in range(1,5):  #loop for monitoring the count of core_lists.
        #for k in x:  
        for i in range(5):  #loop for executing user defined operation on each core_list.
            Arr[len(Arr)-(i+1)]=0
            for k in range(4,1,-1):   #the elements of the user-defined array are operated on the basis of their index value.
                if Arr[k]==0:
                    break  
        x[j]=x.append(Arr)  
    print(x)
#main_section
Arr=[2,3,4,5,6]  #user-defined , valued array.
create_nested(Arr) #operation-execution (calling the function)
