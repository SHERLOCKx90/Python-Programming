f=open("e:/movie.txt", "a+")
f.write("\n")
f.write("i go to school by bus.")
f.close()
f=open("e:/movie.txt", "r")
for line in f:
    print(line, end="")
f.close()
