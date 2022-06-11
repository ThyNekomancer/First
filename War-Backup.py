#first let's import random procedures since we will be shuffling
import random, os
os.system('cls')
deck=[]
#next, let's start building list holders so we can place our cards in there:
def create_DECK():
    global deck
    numberCards = []
    suits = ["♥️","♦️", "♣️", "♠️"]
    royals = ["J", "Q", "K", "A"]
    

    #now, let's start using loops to add our content:
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the royal faces to the cardbase

    
    for k in range(4):
        for l in range(13):
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make

    #now let's see the cards!
    counter=0
    for row in range(4):
        for col in range(13):
            print(deck[counter], end=" ")
            counter +=1
        print()
    #now let's shuffle our deck!
def playerCards():
    random.shuffle(deck)
    global player1
    global player2
    player1=[]
    player2=[]
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
            player2.append(deck[l])
    print("player1 ",player1)
    print()
    print("player2 ",player2)
    #I also want to see what the deck looks like before shuffling. We should have
        #done that a while ago... oh well!
create_DECK()
playerCards()

def playaturn():
    global player1
    global player2
    global Player1count
    global Player2count
    global turn
    input('hit enter to play a turn' + '\t')
    Card1 = player1[0]
    Card2 = player2[0]
    print('Player 1  '+ Card1 + '\t' + 'Player2  '+ Card2)
    if 'A' in Card1:
        Cardvalue1=14
    elif 'K' in Card1:
        Cardvalue1=13
    elif 'Q' in Card1:
        Cardvalue1=12
    elif 'J'in Card1:
        Cardvalue1=11
    elif '1'in Card1:
        Cardvalue1=10    
    else:
        Cardvalue1=int(Card1[0])

    if 'A' in Card2:
        Cardvalue2=14
    elif 'K' in Card2:
        Cardvalue2=13
    elif 'Q' in Card2:
        Cardvalue2=12
    elif 'J'in Card2:
        Cardvalue2=11
    elif '1'in Card2:
        Cardvalue2=10    
    else:
        Cardvalue2=int(Card2[0])
    
    if Cardvalue1>Cardvalue2:
        print ('Player 1 wins that turn !' + '\n')
        player1.append(player1[0])
        player1.append(player2[0])
        player1.pop(0)
        player2.pop(0)
        Player1count+=1
        Player2count-=1
    #this moves both cards to end of player1 deck and removes the played cards from player1 and player2
       
    elif Cardvalue2>Cardvalue1:
        print ('Player 2 wins that turn !' + '\n')
        player2.append(player1[0])
        player2.append(player2[0])
        player1.pop(0)
        player2.pop(0)
        Player1count-=1
        Player2count+=1
    else:
        print ('That turn was a draw !' + '\n')
        player1.append(player1[0])
        player2.append(player2[0])
        player1.pop(0)
        player2.pop(0)
    #this gives each player back their card and puts it at the end of their deck
                    
    turn+=1
    if Player1count <1 or Player2count<1:
        turn = 51
        #if either player is out of cards, act like 50 turns played and end gane

create_DECK()
playerCards()
              
Player1count=26
Player2count=26
turn=0
while turn<51:
    playaturn()

if Player1count > Player2count:
    print ('Congratulations ! Player 1 wins ')
elif Player2count > Player1count:
    print ('Congratulations ! Player 2 wins')
else:
    print ('that game was a draw')

                    # now add the cards to the winner stack