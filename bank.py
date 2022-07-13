def greet():
    grt=input("Greeting: ")
    if grt.strip().lower()=="hello":
        print("$0")
    elif grt[0].lower()=="h":
        print("$20")
    else:
        print("$100")        
greet()        