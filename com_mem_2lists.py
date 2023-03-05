def show_common_members(L1,L2):
    flag=0
    for i in L1:
        if i in L2:
            flag=1
            print(i)
    if flag==0:
        print("no common members")
LIST1=[10,34,"HSMS",4.56]
LIST2=["India",4.56,33,111,90,"HSMS"]
show_common_members(LIST1,LIST2)