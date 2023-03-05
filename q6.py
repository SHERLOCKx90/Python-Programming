import random

PICK = random.randint(0,3)
CITY= ['Durgapur', 'Asansol', 'Bokaro','Dhanbad']
for x in CITY:
    for y in range(1, PICK):
        print (x, end ='')
    print()