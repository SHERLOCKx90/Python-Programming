'''import cv2
img=cv2.imread("C:/Users/USER/OneDrive/Pictures/Screenshots/subha.png",1) #here, 1 gives the 3d matrix of the colour image
img_1=cv2.imread("C:/Users/USER/OneDrive/Pictures/Screenshots/subha.png",0) #here, 0 gives the 2d matrix of the B/W image


#main_section
while True:
    a=int(input("enter no."))
    if a==1:
        print(type(img)) #type shows the class of the object passed in argument ,here it is a numpy array_3d
    elif a==2:
        print(type(img_1)) #here 2d array
    elif a==3:
        print(img.shape) #(287, 286, 3) gives 3 also because it's a 3d matrix of a colour image
    elif a==4:
        print(img_1.shape) #(287, 286) 2d matrix of a B/W image
    elif a==5:
        cv2.imshow("subhadeep chell",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif a==6:
        resized=cv2.resize(img, (100,100))
        cv2.imshow("subhadeep chell",resized)'''
import cv2
from cv2 import *
img=cv2.imread("E:/wallpapers/rosa.jpg",1)
img_1=cv2.imread("E:/wallpapers/rosa.jpg",0)
cv2.imshow("ROSA",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
                      
