import csv
# Line 1
def Addproduct(pid,pname,price): # to write / add data into the CSV file
    f=open('e:/Product.csv','a') # Line 2
    newFileWriter = csv.writer(f)
    newFileWriter.writerow([pid,pname,price])
    f.close()
#csv file reading code
def Readproduct(): # to read data from CSV file with
    newFile = open('e:/Product.csv','r')
    newFileReader = csv.reader(newFile) # Line 3 for row in newFileReader:
    print (“product id::”,row[0])
    print(“product name::”,row[1])
    print(“product price::”,row[2])
    newFile.close()
     # Line 4
Addproduct(“M104”,”Mouse”,550)
Addproduct(“P102”,”Pen Drive”,660)
Addproduct(“M456”,”Mobile”,12000)
Readproduct()