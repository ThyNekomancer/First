tkinter import Y


print("*********************************")
print('   Welcome to the age game!')
print('*********************************')
print('i will give you a random birthdate')
print('and you will figure out the age of that person!')



answer = input('Would you like to play? ') #this will close the game if 'n' is the answer
if 'n' in answer:
    print('okay! see you later then')
    Game=False
else:
    Name = input('Okay! put in your initials here') #this will come back later for when your score is printed
    print('******************************************************')
    choice=input('Awesome! you can try 1, 2, or 3. Which one would you like to try? ')
    choice = int(choice) #this will convert the choice to a number, which allows the rest of the code to function,
    #  if we put one, we get easy, 2 we get medium, 3, we get hard
    


    


    if choice==1:
        answer = 15
        print('************************')
        print('Alright! Easy it is!')
        guess =input('if a person was born in 12/18/2006, how old would they be? ') 
        #by putting the input equal to guess, we can have the answer equal to the guess
        
        
    if choice==2:
        answer = 59
        print('***************')
        print('Medium, good choice!')
        guess = input('Okay, if someone was born on 3/7/63, what would their age be? ')
        
        
    if choice==3:
        answer = 355
        print('******************************************************************')
        print("Wow! you're going for hard? good luck!")
        guess = input('Okay, if someone was born on December 31st, 1666, what would their age be? ')
    guess = int(guess) #this converts our guess to an integer so python can see if it is equal to the answer
    if guess==answer:
        print('Congrats! you got a score of 50')
        print(Name)
        print('50')
    else:
        guess = input('Sorry, try again!')
        guess = int(guess)
        if guess==answer:
            print('congrats! you have a score of 40')
            print(Name) #this prints our name, and our score below it
            print('40')
        else:
            guess = input('Sorry, you get one more shot')
             #if you get it wrong, it allows for another chance, but it lowers the score
            guess = int(guess)
            if guess==answer:
                print('Yay! you have a score of 30')
                print(Name)
                print('30')
            else:
                print('sorry, maybe try playing again?') #you get three chances, so you lose, no score.
                

            
        

         
                

