import mysql.connector as mq


m=mq.connect(host="localhost",user="root", password="subhadeepchell12345", database="students")
mycur=m.cursor()

#sql="insert into student(sid, name, address, marks) values(%s, %s, %s, %s)"
#val=[(102, 'monika','asn',432),(103,'radhika','dgp',560),(104,'kripa', 'ranj',340)]

sql="select * from student where marks>400 ;"   
mycur.execute(sql)

s=mycur.fetchall()
print(s)
  #  if i[3]>400:
       # print("ID: :",i[0],"name: :", i[1]) #",address: :", i[2],",marks: :",i[3])
m.close()

   

'''import mysql.connector as mq

m=mq.connect(host="localhost",user="root", password="subhadeepchell12345",database="students")
mycur=m.cursor()

sql="select * from student where marks>400;"
mycur.execute(sql)
s=mycur.fetchall()
print(s)
m.close()'''
        
        
    
