import random
def play():
    while True:
        user=str(input("r,s,p"))
        computer=random.choice(["r", "s", "p"])
        if user==computer:
            print ("tie")
            continue
        if (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
            print (f"user wins, user={user}, computer={computer}")
        else:
            print (f"computer wins, computer={computer}, user={user}")
play()
