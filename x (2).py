import time as t

def display_even():
    print("loading...")
    t.sleep(2)
    print("BLUE")
def display_odd():
    print("loading...")
    t.sleep(2)
    print("RED")
def main(a):
    if ((a==1) or (a==3)):
          display_odd()
    elif ((a==2)or(a==4)):
          display_even()
    else:
        print("wrong input")
