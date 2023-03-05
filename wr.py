f = open("e:/resources.txt", "a")
while True:
    try:
        print("press 1 to upload subject link")
        print("press 2 to update subject link")
        if op==1:
            subj=input("enter subject:")
            if subj == "physics":
                print("++++++ PHYSICS ++++++")
                up = input("upload physics link:")
                f.write(\n)
                f.write(up)
                break
            elif subj == "chemistry":
                print("++++++ CHEMISTRY ++++++")
                up = input("upload chemistry link:")
                f.write(\n)
                f.write(up)
                        break
                    elif subj == "mathematics":
                        print("++++++ MATHEMATICS ++++++")
                        up = input("upload mathematics link:")
                        f.write(\n)
                        f.write(up)
                        break
                    else:
                        print("invalid")
                        break
                #elif op==2:
            except EOFError:
                print("thank you!")
                break
        f.close()
