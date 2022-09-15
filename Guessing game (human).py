import random
def guess(x):
    number=random.randint(0,x)
    guess=-1
    while guess!=number:
        guess=int(input(f"enter a number between 0 and {x}"))
        if guess>number:
            print ("number too high")
        elif guess<number:
            print ("number too small")
    print (f"yay{number}")

num=int(input())
guess(num)