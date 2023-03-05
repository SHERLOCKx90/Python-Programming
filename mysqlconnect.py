import mysql

db=mysql.connection('localhost','FaceAdmin','Faceadmin@1234','XYZHOS')
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS Hospital")
sql="""Create Table Hospital('hospital_id' INT NOTNULL,'hospital_name' CHAR(50) NOTNULL,'bed_count' INT, PRIMARY KEY('hospital_id') )"""
cursor.execute(sql)
cursor.close()
db.close()
