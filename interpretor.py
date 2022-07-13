def calc():
    user=input("Expression: ")
    if user.strip().split(" ",3)[1]!="/" and user.strip().split(" ",3)[2]!="0":
        print(float(eval(user)))
    else:
        print("No division by 0!")    
calc()    