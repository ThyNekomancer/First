from ctypes.wintypes import WORD
from random import random
import random


import os
os.system('cls')
from time import sleep
seconds=.5

def hint1():

    print('|****************************|')
    print('      here is a new hint      ')
    print('|these creatures all have a hard shell')
    print('|only two shells in fact|')
     

def hint2():

    print('|****************************|')
    print('      here is a new hint      ')
    print('|these fruit are all types of berry')
        
           
def hint3():

    print('|****************************|')
    print('      here is a new hint      ')
    print('|these are output systems')
               

list= ('Clam','scallop','sea urchin','oyster''mussel','geoduck','coral','cockle','abelone','ostrea')
list2= ('blueberry','cherry','raspberry','blackberry','grape','strawberry')
list3 = ('headphones','monitor','speakers')
Game=True
cnt=0

print('|********************|')
print('    Guessing Game!!')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('   1. Animals')
print('    2. Fruits')
print('     3. computer parts')
print(' First we will provide you with a hint')
print('|****************************************|')

name=input('What is your name?')
print(name, end=",")
answer=input('would you like to play?')
if 'n' in answer:
    print('okay, your loss')
    Game=False
else:
    choice=input('what game would you like to play, 1, 2, or 3?')
    choice=int(choice)
if Game:
    try:
        choice>0 and choice <4
    except:
        print('sorry')
        print('give me 1,2,3')
    else: 
        if choice==1:
            theword=random.choice(list)
            print(' Your hint is...')
            print(' these animals are big fans of water!')
        else:
            if choice==2:
                theword=random.choice(list2)
                print('your hint is...')
                print('these are fruits are something you can find in your house!')
            
            if choice==3:
                theword=random.choice(list3)
                print('your hint is...')
                print('they are input / output systems!')

check=True
while check and cnt<2 and Game:
    guess=input('please put your guess here ')
    cnt=cnt+1
    print()
    if guess==theword:
        print('Congrats, you got it')
        check=False
    else: 
          print('sorry, try again')
    if choice==1:
        hint1()
    if choice==2:
        hint2()
    if choice==3:
        hint3()
if check and Game:
    print('you are horrible at guessing. Better luck next time')    
