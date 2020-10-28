import time

name=input("What is your name")

NFL_Teams = {'Dallas':'Cowboys','Atlanta':'Falcons','Arizona':'Cardinals','Carolina':'Panthers','Chicago':'Bears','Cleveland':'Browns','Denver':'Broncos','Detroit':'Lions','Houston':'Texans','Green Bay':'Packers','Los Angeles':'Rams','Kanas City':'Cheifs'}

def Game():
    score = 0
    rounds = 8
    print('')
    print('Good luck!,'):
    def word_bank():
    for key, value in set.items():
        word = value
        correct = key
        word_bank()
        print('What NFL Team is in,',word,end='?')
        answer=input('\nAnswer: ')
        if answer == correct:
            print('\nGood job!\n')
            score += 1
            rounds -= 1
        else:
            print('\nYou Missed!\n')
            rounds -= 1
        if rounds == 0:
            print('You got',score,'out of 8 questions')
            if score >= 5:
                print('YOU WIN',name,end='!')
        else:
            print("You lost but good try")

    time.sleep(5)
    start=input('Do you want to play again?')



def MENU():
    print("* * * * * * * * * * * * * * *")
    print('*    Guess word meanings    *')
    print('*  Teams is the main topic  *')
    print('*                           *')
    print('*                           *')
    print('*       1. Foods!!!         *')
    print('*       2. Quit!!!           *')
    print('*      Guess 4 to win       *')
    print('*                           *')
    print('* * * * * * * * * * * * * * *')

start=input('Would you like to play? if so (yeah/nah) ')
if start == 'yeah':
    score = 0
    print('')
    MENU()
    set = input('Which catagory do you want to play? only 1 works')
    if set =='1'
        set = NFL_Teams
        print('You chose the NFL Team version')
        Game()
    main_code1()

def main_code1():
    word1=random.choice(list(NFL_Teams))
    turn1=3
    guesses1=""
    print(word1,"means: to ",end='')
    while turn1>0 and not str(NFL_Teams[word1])== str(guesses1):
        guess1=input()
        guesses1=guess1
        turn1=turn1-1
        if not str(NFL_Teams[word1])== str(guesses1) and turn1>0:
            print("\nGuess again!")
            print(word1,"means: to ",end='')
    if str(NFL_Teams[word1]) == str(guess1):
        print("\nYou did it! \""+word1+"\" means to",verbs[word1],end='')
    else:
        print("\nYou ran out. \""+word1+"\" means to", verbs[word1],end='')

def guess_nflteam():
        print("When the city is listed, give the name of the NFL Team!")
        main_code1()

menu()
answer=input()
if answer=="1":
    guess_nflteam()
if answer=="2":
    print("Thank you for playing!")

time sleep(1)
