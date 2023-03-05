#---------------importing modules---------
import time
import sqlite3
import os
import admin_st
import school
import userportal

#------------connection--------------
con=sqlite3.connect("SAMPLE.db")
cur=con.cursor()

#-----------------------functions-------------
def startsession(u):
    #flag=0
    cur.execute("Select * from Admin where ADM_ID=?",(u,))
    if cur.fetchall()!=[]:
        school.sys()
        admin_st.admin(u)
    else:
        cur.execute("Select * from Teacher where THR_ID=?",(u,))
        if cur.fetchall()!=[]:
            school.sys()
            userportal.teacher(u)
        else:
            cur.execute("Select * from Student where STUD_ID=?",(u,))
            if cur.fetchall()!=[]:
                school.sys()
                userportal.student(u)
            else:
                print("\nInvalid User Id")

def endsession(a,f):
    pass
