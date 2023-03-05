from datetime import datetime
def pnr():
    t=str(datetime.now())
    s=t[10::]
    c=""
    for i in s:
        if i!=":":
            c=c+i
    return(c)
