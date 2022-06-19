



import pygame, time, os,random, math, datetime, sys

date=datetime.datetime.now()
pygame.init()
os.system('cls')
clock = pygame.time.Clock



WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,0),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
message=['Instructions', 'Settings', 'Play', 'Scoreboard', 'Exit']

screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Menu")  

bg=pygame.image.load('bgSmaller.jpg')
char = pygame.image.load('standing.png')
char = pygame.transform.scale(char, (WIDTH//14, HEIGHT//14))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)
#variables for scoreboard starting out
high = 0
two = 0
three = 0
four = 0
five = 0

#square Var
hb=HEIGHT//14
wb=WIDTH//14
xb=WIDTH//7
rad=25
yb=HEIGHT//2

charx = xb
chary = yb
txtcolor="yellow"
bgcolor="limeGreen"
cx=WIDTH//2
cy=HEIGHT//2
speed=2
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)


mx = 0
my = 0

score = 0

name = ''


square=pygame.Rect(xb,yb,wb,hb)
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
mountainSquare=pygame.Rect(250,320,180,250)
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
Game = False

def mainMenu():
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    Bx2=WIDTH//6
    Bx=WIDTH//2-Bx2//2
    Button_menu=pygame.Rect(Bx, 125, Bx2, WIDTH//18)
    Button_instruct=pygame.Rect(Bx, HEIGHT//8, Bx2, WIDTH//18)
    Button_settings=pygame.Rect(Bx, 2*HEIGHT//8, Bx2, WIDTH//18)
    Button_Game2=pygame.Rect(Bx, 4*HEIGHT//8, Bx2, WIDTH//18)
   
    Button_score=pygame.Rect(Bx, 6*HEIGHT//8, Bx2, WIDTH//18)
    Button_exit=pygame.Rect(Bx, 7*HEIGHT//8, Bx2, WIDTH//18)
    #pygame.draw.rect(screen, colors.get('purple'), Button_settings)
    Title = TITLE_FONT.render("Menu", 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(Title, (WIDTH//2 - (Title.get_width()//2), 10))
    yMenu = HEIGHT//8
    
    for item in message:
        Button_menu=pygame.Rect(Bx, yMenu, Bx2, WIDTH//18)
        text=MENU_FONT.render(item, 1, colors.get(txtcolor))
        pygame.draw.rect(screen, colors.get('purple'), Button_menu)
        screen.blit(text, (Bx, yMenu))
        pygame.display.update()
        #pygame.time.delay(50)
        yMenu += HEIGHT//8
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                mainMenu()
                print("You quit")

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    Instructions()
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_score.collidepoint((mx, my)):
                    Play()
                if Button_exit.collidepoint((mx, my)):
                    pygame.quit()
                if Button_Game2.collidepoint((mx, my)):
                    scoreboard()
                
    
def Instructions():
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    Title = TITLE_FONT.render("Instructions", 1, colors.get(txtcolor))

    
    screen.fill(colors.get(bgcolor))

    myFile = open("How-To-Play.txt")
    content = myFile.readlines()

    yinstructions = HEIGHT//4.7
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get(txtcolor))
        screen.blit(Instruc, (WIDTH//14, yinstructions))
        pygame.display.update()
        yinstructions += HEIGHT//18

    myFile.close()

    #renderig fonts to the screen
    screen.blit(Title, (WIDTH//2 - (Title.get_width()//2), 10))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                mainMenu()
                


def settings():
    global txtcolor, bgcolor, screen, WIDTH, HEIGHT, colors, name
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,50),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
    title=TITLE_FONT.render('Settings', 1, colors.get(txtcolor))
    text=MENU_FONT.render('Clr 1', 1, colors.get("yellow"))
    text3=MENU_FONT.render('Clr 2', 1, colors.get("pink"))
    text4=MENU_FONT.render('Random Clr', 1, colors.get("randt"))
    text5=MENU_FONT.render('Smaller Screen', 1, colors.get(txtcolor))
    text6=MENU_FONT.render('Bigger Screen', 1, colors.get(txtcolor))
    text7=MENU_FONT.render('Enter Name: ', 1, colors.get(txtcolor))

    screen.fill(colors.get(bgcolor))

    Button_3 = pygame.Rect(WIDTH//4-WIDTH//12, HEIGHT//4, WIDTH//6, HEIGHT//14)
    Button_4 = pygame.Rect(2*WIDTH//4-WIDTH//12, HEIGHT//4, WIDTH//6, HEIGHT//14)
    Button_5 = pygame.Rect(3*WIDTH//4-WIDTH//12, HEIGHT//4, WIDTH//6, HEIGHT//14)
    Button_6 = pygame.Rect(WIDTH//3-WIDTH//8, 2*HEIGHT//4, WIDTH//4, HEIGHT//14)
    Button_7 = pygame.Rect(2*WIDTH//3-WIDTH//8, 2*HEIGHT//4, WIDTH//4, HEIGHT//14)
    Button_8 = pygame.Rect(WIDTH//4-WIDTH//12, 3*HEIGHT//4, 3*WIDTH//4, HEIGHT//14)
    Button_9 = pygame.Rect(WIDTH//4+WIDTH//12, 3*HEIGHT//4, 3*WIDTH//4, HEIGHT//14)

    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    pygame.draw.rect(screen, colors.get("white"), Button_4)
    pygame.draw.rect(screen, colors.get("randb"), Button_5)
    pygame.draw.rect(screen, colors.get("purple"), Button_6)
    pygame.draw.rect(screen, colors.get("purple"), Button_7)
    pygame.draw.rect(screen, colors.get("purple"), Button_8)
    screen.blit(title, (WIDTH//2-8*WIDTH//18,50))
    screen.blit(text, (WIDTH//4-WIDTH//12, HEIGHT//4))
    screen.blit(text3, (2*WIDTH//4-WIDTH//12, HEIGHT//4))
    screen.blit(text4, (3*WIDTH//4-WIDTH//12, HEIGHT//4))
    screen.blit(text5, (WIDTH//3-WIDTH//8, 2*HEIGHT//4))
    screen.blit(text6, (2*WIDTH//3-WIDTH//8, 2*HEIGHT//4))
    screen.blit(text7, (WIDTH//4-WIDTH//12, 3*HEIGHT//4))

    pygame.display.update()
    setting = True
    while setting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                setting = False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    txtcolor = "yellow"
                    bgcolor = "limeGreen"
                    pygame.display.update()
                    mainMenu()
                if Button_4.collidepoint((mx, my)):
                    txtcolor = "pink"
                    bgcolor = "white"
                    pygame.display.update()
                    mainMenu()
                if Button_5.collidepoint((mx, my)):
                    txtcolor = "randt"
                    bgcolor = "randb"
                    pygame.display.update()
                    mainMenu()
                if Button_6.collidepoint((mx, my)):
                    if WIDTH!=300:
                        WIDTH-=100
                        HEIGHT-=100
                        screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                        pygame.display.update()
                        mainMenu()
                if Button_7.collidepoint((mx, my)):
                    WIDTH+=100
                    HEIGHT+=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                    pygame.display.update()
                    mainMenu()
                if Button_9.collidepoint((mx,my)): 
                    pygame.draw.rect(screen, colors.get("blue"), Button_9)
                    pygame.display.update()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            print(name)
                            pygame.quit()
                            sys.exit()
                        if event.key ==pygame.K_BACKSPACE:
                            name=name[:-1]
                            print('back')
                        else:
                            name += event.unicode
                    pygame.draw.rect(screen, colors.get("purple"), Button_9)
                    textSurface=MENU_FONT.render(name, True, txtcolor)
                    
                    screen.blit(textSurface, (Button_9.x+5, Button_9.y+5))
                    pygame.display.flip()
                 


def exit():
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    title=TITLE_FONT.render('Bye', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(title, (WIDTH//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.quit()
    sys.exit()



def Play():
    global score, hb, wb, xb, rad, yb, charx, chary, cx, cy, speed, ibox, xig, yig, char, bg, mx, my, insSquare, txtcolor, bgcolor
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    title=TITLE_FONT.render('Game Level 2', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    rad = 25
    screen.blit(title, (275,50))
    pygame.display.update()
    pygame.time.delay(1000)
    score=0
    Game=True
    while Game:
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                mainMenu()
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_LEFT] and cx > 0+rad:
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
            cy += speed
            insSquare.y += speed
        if keys[pygame.K_UP] and cy > 0+rad:
            cy -= speed
            insSquare.y -= speed

        if square.colliderect(insSquare): 
            print("BOOM")
            score += 5
            cx = random.randint(rad, WIDTH-rad)
            cy = random.randint(rad, HEIGHT-rad)
            if rad < WIDTH//2:
                rad += 5
            else:
                endtext = TITLE_FONT.render("Game Over", 1, colors.get(txtcolor))
                screen.fill(colors.get(bgcolor))
                screen.blit(endtext, (275, 100))
                leavegametext = MENU_FONT.render("Press x to return to the main menu", 1, colors.get(txtcolor))
                screen.blit(leavegametext, (275, 300))
                pygame.display.update()
                Game = False
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
      
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10
        
       
        if insSquare.colliderect(mountainSquare):
            cx = rad + 10
            cy = rad + 10
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

      
        pygame.draw.rect(screen, colors.get("blue"), square)
        pygame.draw.rect(screen, colors.get("blue"), insSquare)
        screen.blit(char, (charx, chary))

       
        pygame.draw.circle(screen, colors.get("pink"), (cx, cy), rad)
        
        pygame.display.update()
        pygame.time.delay(5)


def scoreboard():
    global score, name, txtcolor, bgcolor, high, two, three, four, five
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    title=TITLE_FONT.render('Scoreboard', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(title, (WIDTH//3,50))
    print(score)
    if score>high:
        five = four
        four = three
        three = two
        two = high
        high = score
    if score>two and score<high:
        five = four
        four = three
        three = two
        two = score
    if score>three and score<two:
        five = four
        four = three
        three = score
    if score>four and score<three:
        five = four
        four = score
    if score>five and score<four:
        five = score
    date=datetime.datetime.now()
    scrLine="1. "+str(high)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    scrLine2="2. "+str(two)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    scrLine3="3. "+str(three)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"       
    scrLine4="4. "+str(four)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    scrLine5="5. "+str(five)+"    "+name + "   "+date.strftime("%m-%d-%Y")+ "\n"
    myFile = open("score.txt", 'a')
    myFile.write(scrLine+scrLine2+scrLine3+scrLine4+scrLine5)
    myFile.close()
    File = open("score.txt", "r")
    yscores=150
    content = File.readlines()
    for line in content[-5:]:
        scr = MENU_FONT.render(line[0:-1], 1, colors.get(txtcolor))
        screen.blit(scr, (WIDTH//18, yscores))
        pygame.display.update()
        yscores += HEIGHT//18
    File.close()
    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]


mainMenu()


