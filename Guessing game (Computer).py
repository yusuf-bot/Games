import random
def comp_guess(low,high):
    feedback=''
    while feedback!='c' :
        if low!=high:
            num=random.randint(low,high)
        else:
            guess=low
        feedback=str(input(f"is the number {num}, if the guess is higher (h), if the guess is lower (l), if its correct (c)"))
        if feedback =='h':
            high=num-1
        elif feedback == 'l':
            low=num+1
    print ('yay')

low=int(input("LOW:"))
high=int(input("HIGH:"))
comp_guess(low,high)