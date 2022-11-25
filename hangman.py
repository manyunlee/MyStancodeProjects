"""
File: hangman.py
Name:Mandy
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    1. Define a random word. Give hint(based on the length of random word).
    2. Print("You have "+str(hint)+" wrong guesses left.")
    3. Define count function: You have how many chances to guess wrong answer.
    4. Guess->limit guess to A~Z(else:Illegal format). If the guess is lower case, then change to upper case.
    5. If each guess is right: (1)show "You are correct", (2)replace hint(define replace function).
                               (3)count remains the same
    6. If guess is wrong: (1)There is no "input_ch"'s in the word, (2)give the hint(same as previous one)
                          (3)count will minus 1
    7. If all the letters are correct, print "You win"& "The word was:"
    8. If all the letters are incorrect, print "You are completely hung:("& "The word was:"
    """
    # word = "BUNDLE"
    word = random_word()  # define random word
    hint=give_hint(word)
    count=N_TURNS  # count how many turns left
    print("The word looks like ",end="")
    for i in range (len(word)):
        print("-", end="")
    print("")

    print("You have "+str(count)+" wrong guesses left.")

    while count!=0 and hint!=word:  # Ask questions until count =0.
        input_ch=input(("Your guess: "))
        # test:input_ch ="B"
        input_ch=change_upper(input_ch)

        if ALPHABET.find(input_ch)!=-1: #the guess can only be one word
            p=word.find(input_ch)  # find the position of "input_ch" in random word
            if p==-1:
                print("There is no "+input_ch+"'s in the word")
                count = count - 1
                if count!=0:
                    print("You have "+str(count)+" wrong guesses left.")
            else:
                hint=replace(word,input_ch,hint)
                if hint==word:
                    print("You are correct!")
                    print("You win!!")
                    print("The word was: "+word)
                else:
                    print("The words look like "+hint+" in the word")
                    print("You have "+str(count)+" wrong guesses left.")
        else:
            print ("Illegal format")

    if count==0:
        print("You are completely hung:(")
        print("The word was: " + word)


def replace(word,ch,hint):
    search_word=word
    for i in range(len(search_word)):
        s=search_word[i]
        if s!=ch:  # wrong number->print"-"
            p = search_word.find(ch)
            if p!=-1:
                hint=hint[:p]+ch+hint[p+1: ]
                search_word=search_word[:p]+"-"+search_word[p+1: ]  # redefine word, search again

    return hint


def change_upper(ch):
    ans=""
    if ch.islower():
            ans+=ch.upper()# change ch to upper case
    else:ans+=ch
    return ans


def give_hint(random_word):
    ans=""
    for i in range(len(random_word)):
        i=random_word[i]
        ans+="-"
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
