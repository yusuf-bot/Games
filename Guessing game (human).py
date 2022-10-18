import random
def guess(x):
    number=random.randint(0,x)
    guess=-1
    while guess!=number:
        guess=int(input(f"Enter a number between 0 and {x}": ))
        if guess>number:
            print ("Guess is greater")
        elif guess<number:
            print ("Guess is smaller")
    print (f"Yay! The number was {number}")

num=int(input("Enter the upper bound of the number range: "))
guess(num)