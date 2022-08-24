
import pygame, time, os,random, math, datetime, sys



pygame.init()
os.system('cls')
clock = pygame.time.Clock
date=datetime.datetime.now()



WIDTH=700 
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,0),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
message=['Instructions', 'Settings', 'Easy',  "Medium", 'Hard', 'Scoreboard', 'Exit']

screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Morrigans")  

bg=pygame.image.load('bgSmaller.jpg')
char = pygame.image.load('standing.png')
char = pygame.transform.scale(char, (WIDTH//14, HEIGHT//14))

#variables for scoreboard starting out
high = 0
two = 0
three = 0
four = 0
five = 0


hb=HEIGHT//14
wb=WIDTH//14
xb=WIDTH//7
rad=25
yb=HEIGHT//2

charx = xb
chary = yb
txtcolor="blue"
bgcolor="purple"
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
    global menu
    global Button_Game3
    menu = True
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    Bx2=WIDTH//6
    Bx=WIDTH//2-Bx2//2
    Button_menu=pygame.Rect(Bx, 125, Bx2, WIDTH//18)
    Button_instruct=pygame.Rect(Bx, HEIGHT//8, Bx2, WIDTH//18)
    Button_settings=pygame.Rect(Bx, 2*HEIGHT//8, Bx2, WIDTH//18)
    Button_Game1=pygame.Rect(Bx,3*HEIGHT//8, Bx2,WIDTH//18)
    Button_Game2=pygame.Rect(Bx, 4*HEIGHT//8, Bx2, WIDTH//18)
    
    Button_Game3=pygame.Rect(Bx, 5*HEIGHT//8, Bx2, WIDTH//18)
    Button_score=pygame.Rect(Bx, 6*HEIGHT//8, Bx2, WIDTH//18)
    Button_exit=pygame.Rect(Bx, 7*HEIGHT//8, Bx2, WIDTH//18)
    
    Title = TITLE_FONT.render("Menu", 1, colors.get(txtcolor))
    hdng = MENU_FONT.render(name,1,colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(Title, (WIDTH//2 - (Title.get_width()//2), 10))
    screen.blit(hdng, (WIDTH//1.2 - (Title.get_width()//1.5), 10))
    yMenu = HEIGHT//8
    
    for item in message:
        Button_menu=pygame.Rect(Bx, yMenu, Bx2, WIDTH//18)
        text=MENU_FONT.render(item, 1, colors.get(txtcolor))
        pygame.draw.rect(screen, colors.get('purple'), Button_menu)
        screen.blit(text, (Bx, yMenu))
        pygame.display.update()
   
        yMenu += HEIGHT//8
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                mainMenu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
    
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    Instructions()
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx,my)):
                    test()
                if Button_Game2.collidepoint((mx, my)):
                    Medium()
                if Button_Game3.collidepoint((mx,my)):
                    Hard()
                if Button_score.collidepoint((mx,my)):
                    scoreboard()
                if Button_exit.collidepoint((mx,my)):
                    exit()
x = 50
y = 550

def test():
    global score
    global bg, walkLeft, walkRight, height, walkCount, rect, isJump, plattopleftx, plattoprightx, plattopy, jumpCount, x, y, hbh, hbw
    global left2x, right2x, plat2y
    global left3x, right3x, plat3y
    win = pygame.display.set_mode((700,700))
    bg = pygame.image.load('bgSmaller.jpg')
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
    char = pygame.image.load('standing.png')
    hitbox=char.get_rect()
    hbh=hitbox.h
    hbw=hitbox.w
    screen.blit(bg, (0,0))
    pygame.display.flip()
    run = True
    plattopleftx = WIDTH//4-WIDTH//12
    plattoprightx= WIDTH//4-WIDTH//12+WIDTH//6
    plattopy = HEIGHT-200
    left2x = WIDTH//4+WIDTH//4
    right2x = WIDTH//4+WIDTH//4+WIDTH//6
    plat2y = HEIGHT-350
    left3x = WIDTH//4 + WIDTH//2
    right3x = WIDTH//4 +WIDTH//2+WIDTH//6
    plat3y = HEIGHT - 500
    platform3 = pygame.Rect(left3x, plat3y, (right3x-left3x), HEIGHT//14)
    platform2 = pygame.Rect(left2x, plat2y, (right2x-left2x), HEIGHT//14)
   
    platform = pygame.Rect(plattopleftx, plattopy, (plattoprightx-plattopleftx), HEIGHT//14)
    pygame.draw.rect(screen, 1, platform)
    pygame.draw.rect(screen,1, platform2)
    pygame.draw.rect(screen,1, platform3)
    pygame.display.update()
    
    vel = 7
   
   
    clock = pygame.time.Clock()

    isJump = False
    jumpCount = 10
    left = False
    right = False
    walkCount = 0
    landed = False
    

    


    def Play():
        global hitbox
        global my
        global walkCount
        
        screen.blit(bg, (0,0))
        if walkCount + 1 >= 27:
            walkCount = 0
            hitbox = pygame.Rect(x,y,hbw,hbh)
        if left:  
            screen.blit(walkLeft[walkCount//3], (x,y))
            hitbox = pygame.Rect(x,y,hbw,hbh)
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            hitbox = pygame.Rect(x,y,hbw,hbh)
            walkCount += 1
        else:
            hitbox = pygame.Rect(x,y,hbw,hbh)
            win.blit(char, (x, y))
            walkCount = 0
        pygame.draw.rect(screen, colors.get("blue"), platform)
        pygame.draw.rect(screen, colors.get('blue'), platform2)
        pygame.draw.rect(screen, colors.get('blue'), platform3)
        pygame.display.update() 

    def Checklanding():
        global score
        global x, y, plattopleftx, plattoprightx, plattopy, isJump, hbh, landed, isJump
        global jumpCount
        score = 0
        if isJump and jumpCount < -1:
            if y+hbh<plattopy:
                if x>plattopleftx and x<plattoprightx:
                    landed = True
                    score+=50
                    print(score)
                    y=plattopy-hbh
                    jumpCount=10
                    isJump=False
                elif x+hbw>plattopleftx and x+hbw<plattoprightx:
                    landed = True
                    score+=50
                    print(score)
                    y=plattopy-hbh
                    jumpCount=10
                    isJump=False
              

    def checklanding2():
        global x, y, left2x, right2x, plat2y, isJump, hbh, hbw, landed, isJump
        global jumpCount, score
        if isJump and jumpCount < -1:
            if y+hbh<plat2y:
                if x>left2x and x<right2x:
                    landed = True
                    score+=100
                    print(score)
                    y=plat2y-hbh
                    jumpCount=10
                    isJump=False
                elif x+hbw>left2x and x+hbw<right2x:
                    landed = True
                    score+=100
                    print(score)
                    y=plat2y-hbh
                    jumpCount=10
                    isJump=False
             



    def checklanding3():
        global x, y, left3x, right3x, plat3y, isJump, hbh, hbw, landed, isJump
        global jumpCount, score
        if isJump and jumpCount < -1:
            if y+hbh<plat3y:
                if x>left3x and x<right3x:
                    landed = True
                    score+=150
                    print('score')
                    y=plat3y-hbh
                    jumpCount=10
                    isJump=False
                    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//40)
                    title=MENU_FONT.render('congrats ' +name + ',you got a score of 150!', 1, colors.get(txtcolor))
                    screen.fill(colors.get(bgcolor))
                    screen.blit(title, (WIDTH//2, HEIGHT//2))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    x = 50
                    y=550
                    mainMenu()
                elif x+hbw>left3x and x+hbw<right3x:
                    landed = True
                    score+=150
                    print(score)
                    y=plat3y-hbh
                    jumpCount=10
                    isJump=False
                    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//40)
                    title=MENU_FONT.render('congrats ' +name + ',you got a score of 150!', 1, colors.get(txtcolor))
                    screen.fill(colors.get(bgcolor))
                    screen.blit(title, (WIDTH//2, HEIGHT//2))
                    x=50
                    y=550
                    pygame.display.update()
                    pygame.time.delay(2000)
                    mainMenu()
          


    run = True

    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0: 
            x -= vel
            left = True
            right = False
            Play()

        elif keys[pygame.K_RIGHT] and x < 585:  
            x += vel
            left = False
            right = True
            Play()
        else: 
            left = False
            right = False
            walkCount = 0
            Play()

        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
                Play()
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
                Checklanding()
                checklanding2()
                checklanding3()
                if landed==False and jumpCount==-10:
                    y=550
                    isJump=False
                    jumpCount=10
                    score = 0
                    print(score)
                Play()
            else: 
                jumpCount = 10
                isJump = False
                Play()
        

def Medium():
    global score
    global bg, walkLeft, walkRight, height, walkCount, rect, isJump, plattopleftx, plattoprightx, plattopy, jumpCount, x, y, hbh, hbw
    global left2x, right2x, plat2y
    global left3x, right3x, plat3y
    global left4x, right4x, plat4y, platform4
    win = pygame.display.set_mode((1000,800))
    bg = pygame.image.load('Background2.png')
    bg = pygame.transform.scale(bg, (1000,800))
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
    char = pygame.image.load('standing.png')
    hitbox=char.get_rect()
    hbh=hitbox.h
    hbw=hitbox.w
    screen.blit(bg, (0,0))
    pygame.display.flip()
    run = True
    plattopleftx = WIDTH//4-WIDTH//4
    plattoprightx= WIDTH//4-WIDTH//4+WIDTH//6
    plattopy = HEIGHT-200
    left2x = WIDTH//4+WIDTH//4
    right2x = WIDTH//4+WIDTH//4+WIDTH//6
    plat2y = HEIGHT-350
    left3x = WIDTH//4 + WIDTH//2
    right3x = WIDTH//4 +WIDTH//2+WIDTH//6
    plat3y = HEIGHT - 500
    platform3 = pygame.Rect(left3x, plat3y, (right3x-left3x), HEIGHT//14)
    left4x =  WIDTH//3
    right4x = WIDTH//3+WIDTH//6
    plat4y = HEIGHT - 600
    platform4 = pygame.Rect(left4x, plat4y, (right4x-left4x), HEIGHT//14)
    platform3 = pygame.Rect(left3x, plat3y, (right3x-left3x), HEIGHT//14)
    platform2 = pygame.Rect(left2x, plat2y, (right2x-left2x), HEIGHT//14)
  
    platform = pygame.Rect(plattopleftx, plattopy, (plattoprightx-plattopleftx), HEIGHT//14)
    pygame.draw.rect(screen, 1, platform)
    pygame.draw.rect(screen,1, platform2)
    pygame.draw.rect(screen,1, platform3)
    pygame.draw.rect(screen,1,platform4)
    pygame.display.update()

    vel = 7


    clock = pygame.time.Clock()

    isJump = False
    jumpCount = 10
    left = False
    right = False
    walkCount = 0
    landed = False


        


    def Play():
        global hitbox
        global my
        global walkCount
        
        screen.blit(bg, (0,0))
        if walkCount + 1 >= 27:
            walkCount = 0
            hitbox = pygame.Rect(x,y,hbw,hbh)
        if left:  
            screen.blit(walkLeft[walkCount//3], (x,y))
            hitbox = pygame.Rect(x,y,hbw,hbh)
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            hitbox = pygame.Rect(x,y,hbw,hbh)
            walkCount += 1
        else:
            hitbox = pygame.Rect(x,y,hbw,hbh)
            win.blit(char, (x, y))
            walkCount = 0
        pygame.draw.rect(screen, colors.get("blue"), platform)
        pygame.draw.rect(screen, colors.get('blue'), platform2)
        pygame.draw.rect(screen, colors.get('blue'), platform3)
        pygame.draw.rect(screen, colors.get('blue'), platform4)
        pygame.display.update() 

    def Checklanding():
        global score
        global x, y, plattopleftx, plattoprightx, plattopy, isJump, hbh, landed, isJump
        global jumpCount
        score = 0
        if isJump and jumpCount < -1:
            if y+hbh<plattopy:
                if x>plattopleftx and x<plattoprightx:
                    landed = True
                    score+=50
                    print(score)
                    y=plattopy-hbh
                    jumpCount=10
                    isJump=False
                elif x+hbw>plattopleftx and x+hbw<plattoprightx:
                    landed = True
                    score+=50
                    print(score)
                    y=plattopy-hbh
                    jumpCount=10
                    isJump=False
            

    def checklanding2():
        global x, y, left2x, right2x, plat2y, isJump, hbh, hbw, landed, isJump, score
        global jumpCount, score
        
        if isJump and jumpCount < -1:
            if y+hbh<plat2y:
                if x>left2x and x<right2x:
                    landed = True
                    score+=150
                    print(score)
                    y=plat2y-hbh
                    jumpCount=10
                    isJump=False
                elif x+hbw>left2x and x+hbw<right2x:
                    landed = True
                    score+=150
                    print(score)
                    y=plat2y-hbh
                    jumpCount=10
                    isJump=False
  
    def checklanding4():
        global x, y, left4x, right4x, plat4y, isJump, hbh, hbw, landed, isJump, score 
        global jumpCount, win
        if isJump and jumpCount < -1:
            if y+hbh<plat4y:
                if x>left4x and x<right4x:
                    landed = True
                    score+=450
                    print(score)
                    y=plat4y-hbh
                    jumpCount=10
                    isJump=False
              
                    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//40)
                    title=MENU_FONT.render('congrats ' +name + ',you got a score of 450!', 1, colors.get(txtcolor))
                    screen.fill(colors.get(bgcolor))
                    screen.blit(title, (WIDTH//2, HEIGHT//2))
                    x=50
                    y=550
                    pygame.display.update()
                    pygame.time.delay(2000)
                    win = pygame.display.set_mode((700,700))
                    mainMenu()
                elif x+hbw>left4x and x+hbw<right4x:
                    landed = True
                    score+=450
                    print(score)
                    y=plat4y-hbh
                    jumpCount=10
                    isJump=False
               
                    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//40)
                    title=MENU_FONT.render('congrats ' +name + ',you got a score of 450!', 1, colors.get(txtcolor))
                    screen.fill(colors.get(bgcolor))
                    screen.blit(title, (WIDTH//2, HEIGHT//2))
                    x=50
                    y=550
                    pygame.display.update()
                    pygame.time.delay(2000)
                    win = pygame.display.set_mode((700,700))
                    mainMenu()



    def checklanding3():
        global x, y, left3x, right3x, plat3y, isJump, hbh, hbw, landed, isJump, score
        global jumpCount, win
        if isJump and jumpCount < -1:
            if y+hbh<plat3y:
                if x>left3x and x<right3x:
                    landed = True
                    score+=200
                    print(score)
                    y=plat3y-hbh
                    jumpCount=10
                    isJump=False
                    
                elif x+hbw>left3x and x+hbw<right3x:
                    landed = True
                    score+=200
                    print(score)
                    y=plat3y-hbh
                    jumpCount=10
                    isJump=False
       


    run = True

    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0: 
            x -= vel
            left = True
            right = False
            Play()

        elif keys[pygame.K_RIGHT] and x < 985:  
            x += vel
            left = False
            right = True
            Play()
        else: 
            left = False
            right = False
            walkCount = 0
            Play()

        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
                Play()
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
                checklanding4()
                checklanding3()
                checklanding2()
                Checklanding()
                if landed==False and jumpCount==-10:
                    y=550
                    isJump=False
                    jumpCount=10
                    score = 0
                    print(score)
                Play()
            else: 
                jumpCount = 10
                isJump = False
                Play()
    

def Hard():
    global score
    global bg, walkLeft, walkRight, height, walkCount, rect, isJump, plattopleftx, plattoprightx, plattopy, jumpCount, x, y, hbh, hbw
    global left2x, right2x, plat2y
    global left3x, right3x, plat3y
    global left4x, right4x, plat4y, platform4
    global left5x, right5x, plat5y, platform5
    win = pygame.display.set_mode((1000,800))
    bg = pygame.image.load('Background5.gif')
    bg = pygame.transform.scale(bg, (1000,800))
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
    char = pygame.image.load('standing.png')
    hitbox=char.get_rect()
    hbh=hitbox.h
    hbw=hitbox.w
    screen.blit(bg, (0,0))
    pygame.display.flip()
    run = True
    plattopleftx = WIDTH//4-WIDTH//4
    plattoprightx= WIDTH//4-WIDTH//4+WIDTH//6
    plattopy = HEIGHT-200
    left2x = WIDTH//12+WIDTH//4
    right2x = WIDTH//12+WIDTH//4+WIDTH//6
    plat2y = HEIGHT-390
    left3x = WIDTH//5 + WIDTH//2
    right3x = WIDTH//5 +WIDTH//2+WIDTH//6
    plat3y = HEIGHT - 550
    platform3 = pygame.Rect(left3x, plat3y, (right3x-left3x), HEIGHT//14)
    left4x =  WIDTH//1.0
    right4x = WIDTH//1.0+WIDTH//6
    plat4y = HEIGHT - 300
    left5x = WIDTH +WIDTH//6 + WIDTH//12
    right5x = WIDTH + WIDTH//6 + WIDTH//6 + WIDTH//12
    plat5y = HEIGHT - 490
    platform5 = pygame.Rect(left5x, plat5y, (right5x-left5x), HEIGHT//14)
    platform4 = pygame.Rect(left4x, plat4y, (right4x-left4x), HEIGHT//14)
    platform3 = pygame.Rect(left3x, plat3y, (right3x-left3x), HEIGHT//14)
    platform2 = pygame.Rect(left2x, plat2y, (right2x-left2x), HEIGHT//14)
    platform = pygame.Rect(plattopleftx, plattopy, (plattoprightx-plattopleftx), HEIGHT//14)
    pygame.draw.rect(screen, 1, platform)
    pygame.draw.rect(screen,1, platform2)
    pygame.draw.rect(screen,1, platform3)
    pygame.draw.rect(screen,1,platform4)
    pygame.draw.rect(screen,1,platform5)
    pygame.display.update()

    vel = 7


    clock = pygame.time.Clock()

    isJump = False
    jumpCount = 10
    left = False
    right = False
    walkCount = 0
    landed = False


        


    def Play():
        global hitbox
        global my
        global walkCount
        
        screen.blit(bg, (0,0))
        if walkCount + 1 >= 27:
            walkCount = 0
            hitbox = pygame.Rect(x,y,hbw,hbh)
        if left:  
            screen.blit(walkLeft[walkCount//3], (x,y))
            hitbox = pygame.Rect(x,y,hbw,hbh)
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            hitbox = pygame.Rect(x,y,hbw,hbh)
            walkCount += 1
        else:
            hitbox = pygame.Rect(x,y,hbw,hbh)
            win.blit(char, (x, y))
            walkCount = 0
        pygame.draw.rect(screen, colors.get("blue"), platform)
        pygame.draw.rect(screen, colors.get('blue'), platform2)
        pygame.draw.rect(screen, colors.get('blue'), platform3)
        pygame.draw.rect(screen, colors.get('blue'), platform4)
        pygame.draw.rect(screen,colors.get('blue'), platform5)
        pygame.display.update() 

    def Checklanding():
        global score
        global x, y, plattopleftx, plattoprightx, plattopy, isJump, hbh, landed, isJump
        global jumpCount
        score = 0
        if isJump and jumpCount < -1:
            if y+hbh<plattopy:
                if x>plattopleftx and x<plattoprightx:
                    landed = True
                    score+=50
                    print(score)
                    y=plattopy-hbh
                    jumpCount=10
                    isJump=False
                elif x+hbw>plattopleftx and x+hbw<plattoprightx:
                    landed = True
                    score=50
                    print(score)
                    y=plattopy-hbh
                    jumpCount=10
                    isJump=False
       
    def checklanding2():
        global x, y, left2x, right2x, plat2y, isJump, hbh, hbw, landed, isJump
        global jumpCount, score
        if isJump and jumpCount < -1:
            if y+hbh<plat2y:
                if x>left2x and x<right2x:
                    landed = True
                    score+=150
                    print(score)
                    y=plat2y-hbh
                    jumpCount=10
                    isJump=False
                elif x+hbw>left2x and x+hbw<right2x:
                    landed = True
                    score+=150
                    print(score)
                    y=plat2y-hbh
                    jumpCount=10
                    isJump=False
         
    def checklanding4():
        global x, y, left4x, right4x, plat4y, isJump, hbh, hbw, landed, isJump
        global jumpCount, win, score
        if isJump and jumpCount < -1:
            if y+hbh<plat4y:
                if x>left4x and x<right4x:
                    landed = True
                    score+=450
                    print(score)
                    y=plat4y-hbh
                    jumpCount=10
                    isJump=False
              
                    
                elif x+hbw>left4x and x+hbw<right4x:
                    landed = True
                    score+=450
                    print(score)
                    y=plat4y-hbh
                    jumpCount=10
                    isJump=False
               
                   
    def checklanding5():
        global x, y, left5x, right5x, plat5y, isJump, hbh, hbw, landed, isJump
        global jumpCount, win, score
        if isJump and jumpCount < -1:
            if y+hbh<plat5y:
                if x>left5x and x<right5x:
                    landed = True
                    score+=600
                    print(score)
                    y=plat5y-hbh
                    jumpCount=10
                    isJump=False
              
                    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//40)
                    title=MENU_FONT.render('congrats ' +name + ',you got a score of 600!', 1, colors.get(txtcolor))
                    screen.fill(colors.get(bgcolor))
                    screen.blit(title, (WIDTH//2, HEIGHT//2))
                    x=50
                    y=550
                    pygame.display.update()
                    pygame.time.delay(2000)
                    win = pygame.display.set_mode((700,700))
                    mainMenu()
                elif x+hbw>left5x and x+hbw<right5x:
                    landed = True
                    score=600
                    print(score)
                    y=plat5y-hbh
                    jumpCount=10
                    isJump=False
               
                    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//40)
                    title=MENU_FONT.render('congrats ' +name + ',you got a score of 600!', 1, colors.get(txtcolor))
                    screen.fill(colors.get(bgcolor))
                    screen.blit(title, (WIDTH//2, HEIGHT//2))
                    x=50
                    y=550
                    pygame.display.update()
                    pygame.time.delay(2000)
                    win = pygame.display.set_mode((700,700))
                    mainMenu()



    def checklanding3():
        global x, y, left3x, right3x, plat3y, isJump, hbh, hbw, landed, isJump
        global jumpCount, win, score
        if isJump and jumpCount < -1:
            if y+hbh<plat3y:
                if x>left3x and x<right3x:
                    landed = True
                    score+=200
                    print(score)
                    y=plat3y-hbh
                    jumpCount=10
                    isJump=False
                    
                elif x+hbw>left3x and x+hbw<right3x:
                    landed = True
                    score+=200
                    print(score)
                    y=plat3y-hbh
                    jumpCount=10
                    isJump=False
                    
          


    run = True

    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0: 
            x -= vel
            left = True
            right = False
            Play()

        elif keys[pygame.K_RIGHT] and x < 985:  
            x += vel
            left = False
            right = True
            Play()
        else: 
            left = False
            right = False
            walkCount = 0
            Play()

        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
                Play()
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
                checklanding5()
                checklanding4()
                checklanding3()
                checklanding2()
                Checklanding()
                if landed==False and jumpCount==-10:
                    y=550
                    isJump=False
                    jumpCount=10
                    score = 0
                    print(score)
                Play()
            else: 
                jumpCount = 10
                isJump = False
                Play()
    
    

    
                
def Instructions():
    global mx, my, Button_back_to_menu
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    Title = TITLE_FONT.render("Instructions", 1, colors.get(txtcolor))
    Button_back_to_menu=pygame.Rect(600, 7*HEIGHT//8, 600, WIDTH//18)
    

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
            for item in message:
                Button_menu=pygame.Rect(400, HEIGHT//8, 400, WIDTH//18)
                text=MENU_FONT.render(item, 1, colors.get(txtcolor))
                pygame.draw.rect(screen, colors.get('purple'), Button_menu)
                
                pygame.display.update()
            
            if event.type==pygame.QUIT:
                Instructions=False
                mainMenu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
    
                mx = mousePos[0]
                my = mousePos[1]
                


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
    active = False
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
                if Button_8.collidepoint((mx,my)): 
                    pygame.draw.rect(screen, colors.get("blue"), Button_9)
                    pygame.display.update()
                    active = not active 
                else: 
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(name)
                        mainMenu()
                    
                    elif event.key ==pygame.K_BACKSPACE:
                            name=name[:-1]
                            print('back')
                    else:
                        name += event.unicode
                        print(name)
                    
                    pygame.draw.rect(screen, colors.get("purple"), Button_9)
                    textSurface=MENU_FONT.render(name, True, 'yellow')
                   
                    screen.blit(textSurface, Button_9)
                    pygame.display.flip()
                    
                 


def exit():
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    title=MENU_FONT.render('byeeeeeeeee B)', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(title, (WIDTH//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

    




    


def scoreboard():
    global score, name, txtcolor, bgcolor, high, two, three, four, five
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    title=TITLE_FONT.render('Scoreboard', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(title, (WIDTH//3,50))
    myFile=open("scoreboard.txt")
    line1=myFile.readline()
    line2=myFile.readline()
    line3=myFile.readline()
    line4=myFile.readline()
    line5=myFile.readline()
    high=int(line1[3:6])
    print(high)
    two=int(line2[3:6])
    three=int(line3[3:6])
    four=int(line4[3:6])
    five=int(line5[3:6])
    print(five)
    
    
    name1 = line1[10:-14]
    print(name1)
    name2 = line2[10:-14]
    print(name2)
    name3 = line3[10:-14]
    print(name3)
    name4 = line4[10:-14]
    print(name4)
    name5 = line5[10:-14]
    print(name5)


    if score>high:
        five = four
        four = three
        three = two
        two = high
        high = score
        name5=name4
        name4=name3
        name3=name2
        name2=name1
        name1=name

        
    if score>=two and score<high:
        five = four
        four = three
        three = two
        two = score
        name5=name4
        name4=name3
        name3=name2
        name2=name
  
    if score>=three and score<two:
        five = four
        four = three
        three = score
        name5=name4
        name4=name3
        name3=name

    if score>=four and score<three:
        five = four
        four = score
        name5=name4
        name4=name
   
    if score>=five and score<four:
        five = score
        name5=name

    myFile.close()

    date=datetime.datetime.now()
    scrLine="1. "+str(high)+"    "+name1 + "   "+date.strftime("%m-%d-%Y")+ "\n"
    scrLine2="2. "+str(two)+"    "+name2 + "   "+date.strftime("%m-%d-%Y")+ "\n"
    scrLine3="3. "+str(three)+"    "+name3 + "   "+date.strftime("%m-%d-%Y")+ "\n"       
    scrLine4="4. "+str(four)+"    "+name4 + "   "+date.strftime("%m-%d-%Y")+ "\n"
    scrLine5="5. "+str(five)+"    "+name5 + "   "+date.strftime("%m-%d-%Y")+ "\n"
    myFile = open("scoreboard.txt", "w")
    myFile.write(scrLine+scrLine2+scrLine3+scrLine4+scrLine5)
    myFile.close()
    File = open("scoreboard.txt", "r")
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