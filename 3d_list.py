def create_3d_list(l):
    for i in range(2):
        l.append([])
        for j in range(3):
            l[i].append([])
            for k in range(4):
                l[i][j].append("$")
#main_section
list=[]
create_3d_list(list)
print(list)