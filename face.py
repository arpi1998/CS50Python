def emj():
    txt=input()
    if txt.find(":)")>-1:
        print(txt.replace(":)","🙂"))
    elif txt.find(":(")>-1:
        print(txt.replace(":(","🙁"))    
emj()        