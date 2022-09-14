from words import words
import random
import string
def get_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=get_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    lives=6
    
    while (len(word_letters))>0 and lives>0:
        print (f"You have {lives} lives, and you have guessed:    ", " ".join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print ("current word:   ",' '.join(word_list))
        user=str(input("type something:    ")).upper()
        if user in alphabet-used_letters:
            used_letters.add(user)
            if user in word_letters:
                word_letters.remove(user)
            else:
                lives=lives-1
        elif user in used_letters:
            print ("already done")
        else:
            print ("invalid character")
            
    if (len(word_letters))==0:
        print ('YAY!!!')
    if lives==0:
        print ("you didnt guess, word was:    ",word) 

hangman()
ans='yes'
while ans=='yes':
    ans=input('do u wanna play again?\n')
    hangman()
quit()
    
