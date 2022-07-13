def meals():
    from datetime import datetime
    qs=input("What time is it?")
    chg=float(qs.replace(":","."))
    if 7<=chg<=8:
        print("Breakfast time")
    elif 12<=chg<=13:
        print("Lunch time")
    elif 18<=chg<=19:
        print("Dinner time")
meals()           