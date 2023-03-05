dict3={}
def add_dict(dict1,dict2):
    global dict3
    dict3=dict1.copy()
    for i in dict2.keys():
        if i not in dict1.keys():
            dict3[i]=dict2[i]
dict1={1:23,2:"abc",3:90,4:45}
dict2={11:"HSMS",2:67, 8:77,4:"durgapur"}
add_dict(dict1,dict2)
print("dictionary 1",dict1)
print("dictionary 2",dict2)
print("dictionary 3",dict3)
