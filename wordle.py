from words import words
import random
def wordle():
    print("___WELCOME TO WORDLE___")
    List=[]
    for word in words:
        if len(word)==5:
            List.append(word)

    ComputerWord=random.choice(List).upper()
    Tries=6
    while Tries>0:
        Output=[]
        print(f"You have {Tries} tries")
        UserWord=input("Enter your word:   ")
        try:
            UserWord=(str(UserWord)).upper()
        except:
            print ("Invalid word. Try again!")
            continue

        if len(UserWord)>5 or len(UserWord)<5:
            print ("Invalid word. Try again!")
            continue


        #yellow
        count=0
        for letter in UserWord:
            if letter in ComputerWord:
                Output.append('Y')
                #green
                if (UserWord[count:(count+1)])==(ComputerWord[count:(count+1)]):
                    Output.pop()
                    Output.append(('G'))

            else:
                Output.append('X')
            count=count+1
            ComputerWord=ComputerWord.rstrip(ComputerWord[count:(count+1)])

        print ("                   ", end='')
        for x in Output:
            print (x, end='')
        print (' ')

        Tries=Tries-1
        if UserWord==ComputerWord:
            print ("YOU GOT IT!!!")
            break

    if Tries==0 and UserWord!=ComputerWord:
        print ("You didn't get it, next time, the word was ", ComputerWord)




wordle()
ans='yes'
while ans=='yes':
    ans=input('Do you wanna play again?\n')
    wordle()
quit()



