import random
import time

name=input("What is your name? ")
print("Good Luck !", name)
gameWords = ['pizza','pasta','hamburger','hotdog','chicken','steak','sushi','cook','fork','knife','spoon','cake','soup','salad']
answer=input('do you want to guess a word')

while answer == 'yes':
    word= random.choice(gameWords)
    guesses =''
    final =''
    turns=8
    while turns>0:
        for char in word:
            if char in guesses:
                print(char,end ='')
                final= final+char
            else:
                print('_', end =' ')
        print(' ')
        if word in final:
            print('you win')
            print("the word is: "+ word)
            break
        guess= input("give me a letter: ")
        guesses += guess
        if guess not in word:
            turns -=1
            print("you have ",end= '')
            print(turns)
        if turns == 0:
            print('GAME OVER!')
            break
        answer= input('do you want to play again')
    time.sleep(5)
