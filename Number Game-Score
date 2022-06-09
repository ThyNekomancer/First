from operator import truediv
import os
from pdb import Restart
os.system('cls')

import random
import os, datetime
date=datetime.datetime.now()
print(date)
print(date.strftime("%m-%d-%Y"))

name =input('What is your name?')

maxcount=10
cnt=0

print('*********************')
print('GUESS THE NUMBER GAME')

def menu():
    global choice
    global Game
    global cnt
    cnt=0
    print('Choose from the following options')
    print('1: Instructions')
    print('2: Level 1: 1-25 numbers')
    print('3: level 2: 1-50 numbers')
    print('4: level 3: 1-100 numbers')
    print('5: Print top five scores')
    print('6: Exit' + '\n')
    choice=input('What is your choice? ')
    choice=int(choice)
    if choice>5:
        print('alright!  see you later!' +'\n')
        Game=False
    else: Game=True


menu()

while Game==True:
    try:
        choice>1 and choice<5
    except:
        input('sorry, if you want to play, give me 2, 3, or 4')
    if choice==1:
        f=open('Game-Instructions.txt')
        print(f.read())
        cnt=maxcount
    if choice==5:
        myFile = open("topscores.txt", 'r')
        stuff=myFile.readlines()
        stuff.sort(reverse=True)
        myFile.close()
        linecount=0
        print('the top five scores are' + '\n')
        for line in stuff:
            print(line)
            linecount=linecount+1
            if linecount>4:
                break
        cnt=maxcount
    while cnt<maxcount:
        score = (500-cnt*10)
        if choice==2:
            answer=random.randint(1,25)
            guess=input('What is your guess?')
            guess = int(guess)
            cnt=cnt+1
        if choice==3:
            answer=random.randint(1,50)
            guess=input('what is your guess?')
            guess = int(guess)
            cnt=cnt+1
        if choice==4:
            answer=random.randint(1,100)
            guess=input('what is your guess?')
            guess = int(guess)
            cnt=cnt+1
        if guess==answer:
            cnt=maxcount
            print('congratulations! you won!')
            print('your score is   ' +str(score) +'\n')
            scoreline=str(score)+'\t'+name +'\t'+date.strftime('%m-%d-%Y')+'\n'
            Scoreboard= open('topscores.txt', "a")
            Scoreboard.write(scoreline)
            Scoreboard.close()
        else:
            print('sorry! try again')
    menu()
            
