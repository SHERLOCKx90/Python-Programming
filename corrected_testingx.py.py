def count():   #counts the user required content
    print("count the no. of special symbols?   press 1")
    print("count the no. of lines started with vowel?   press 2")
    op=int(input("enter the option : :"))
    if op==1:
        f=open("sherlock.txt","r")
        ctr=0
        while True:
            try:
            	a=f.readline()
                w=a.split()
                for i in w:
                    for j in i:
                        if j in ('.',',','@','#','!'):
                        	ctr+=1
            except:
                if a=="":
                	break
        print('\n Special Symbols :',ctr)
        f.close()
   
     elif op==2:
        f=open("sherlock.txt","r")
        ctr=0
        v=["A","E","I","O","U"]
        while True:
        	   try:
        	   d=f.readline()
               z=d.split()
        	   for l in z:
        	       if l[0].upper in v :
        	       	ctr+=1
        	   except:
        	   	break
        print("the no. of lines started with a vowel : :",ctr)
        f.close()
    else:
        print("err. ivalid option!")
            
def display():  #disp-lays content acc. to user requirement
    print("display all the words started with 'P' ? press 1")
    op=int(input("enter your option : :"))
    if op==1:
        f=open("sherlock.txt","r")
        while True:
            a=f.readline()
            w=a.split()
            for i in w:
                if i[0].upper()=="P":
                    print("\n Words started with 'P' :",i)
            if a=="":
                break
        f.close()
      
 #------------------------------ M A I N -----------------------------------------
 while True:
        print("1. Count the content")
        print("2. Display the required content")
        op=int(input("Enter option::"))
        if op==1:
            count()
        elif op==2:
            display()
        else:
            print(Err. please choose from the above options!)
