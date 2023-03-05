import pickle as p

def create(an,ano,abl):
    b=open('e:/bank.dat', 'ab+')
    v=['AccNo','Name','Balance']
    a=[]
    if abl>=1000:
        while True:
            try:
                if a[i].get('AccNo.')==ano:
                    v=0
                    print('AccNo. already exists!')
                if v:
                    a.append(dict(zip(['AccNo','Name','Balance'],[an,ano,abl])))
            except:
                print('Account created successfully.')
                break
    else:
        print('Account balance cannot be less than 1000 INR.')
    a=bytes(a)
    p.dump(a,b)
    print("go check out")
    b.close()
    
def display(ano=0):
    if ano:
       b=open('e:/bank.dat', 'rb')
       a=[]
       while True:
        try:
            rec=p.load(b)
            a.append(rec)
        except EOFError:
            break
       v=0
       for i in range(len(a)):
           if a[i].get('AccNo.')==ano:
               print(a[i])
               v=1
               break
           if not v:
               print ('Sorry! Record not found.')
    else:
        print (a)
    b.close()
    
#main section
print('Welcome! Please choose your option.')
while 1:
    c=int(input('1.Create account\n2.Deposit to account\n3.Withdraw from account\n4.View account\n5.Exit\n '))
    if c==1:
        an=input('Enter your account name. ')
        ano=int(input('Enter your account number. '))
        abl=int(input('Enter your account balance. '))
        create(an, ano, abl)
    elif c==2:
        n=int(input('Enter your account number.'))
        d=int(input('Enter your deposit balance'))
        deposit(n, d)
    elif c==3:
        n=int(input('Enter your account number.'))
        w=int(input('Enter your withdrawal balance'))
        withdraw(n, w)
    elif c==4:
        n=int(input('Enter your account number.'))
        if n:
            display(n)
        else:
            display()
    else:
        break
print ('Thank you.')
