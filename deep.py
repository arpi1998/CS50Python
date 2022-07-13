def answ():
    import random
    quest=["What is the Answer to the Great Question of Life?","What is the Answer to the Great Question of Universe?","What is the Answer to the Great Question of Everything?"]
    print(random.choice(quest))
    answer=input()
    chk="FORTY TWO"
    if answer=="42" or answer.lower()==chk.lower() or answer.replace("-"," ")==chk.lower():
        print("Yes")
    else:
        print("No")
answ()          