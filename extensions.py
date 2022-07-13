def file():
    chk=["gif","jpg","jpeg","png"]
    answ=input("File name: ")
    x=answ.strip().split(".",2)[1]
    if x in chk:
        print("image/"+x)
    else:
        print("application/"+x)    
file()      