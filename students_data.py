import mysql.connector as mq

m=mq.connect(host="localhost",user="root", password="subhadeepchell12345", database="students")
mycur=m.cursor()


mycur.execute(c)
m.commit()

