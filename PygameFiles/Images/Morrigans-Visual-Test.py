import pygame, time, os,random, math, datetime, sys



pygame.init()
os.system('cls')
clock = pygame.time.Clock
date=datetime.datetime.now()



WIDTH=700 
HEIGHT=700
colors={"white":(255,255,255), "black":(0,0,0),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,0),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
message=['Instructions', 'Settings', 'Chapter 1', 'Exit']

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
txtcolor="purple"
bgcolor="black"
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
    TITLE_FONT = pygame.font.SysFont('timesnewroman', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('timesnewroman', WIDTH//35)
    Bx2=WIDTH//6
    Bx=WIDTH//2-Bx2//2
    Button_menu=pygame.Rect(Bx, 125, Bx2, WIDTH//18)
    Button_instruct=pygame.Rect(Bx, HEIGHT//8, Bx2, WIDTH//18)
    Button_settings=pygame.Rect(Bx, 2*HEIGHT//8, Bx2, WIDTH//18)
    
    Button_exit=pygame.Rect(Bx, 4*HEIGHT//8, Bx2, WIDTH//18)
    
    
    
    Title = TITLE_FONT.render("Morrigans Beta Test", 1, colors.get(txtcolor))
    hdng = MENU_FONT.render(name,1,colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(Title, (WIDTH//2 - (Title.get_width()//2), 10))
    screen.blit(hdng, (WIDTH//1.2 - (Title.get_width()//1.5), 10))
    yMenu = HEIGHT//8
    
    for item in message:
        Button_menu=pygame.Rect(Bx, yMenu, Bx2, WIDTH//18)
        text=MENU_FONT.render(item, 1, colors.get(txtcolor))
        pygame.draw.rect(screen, colors.get('black'), Button_menu)
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
                if Button_exit.collidepoint((mx,my)):
                    exit()



    
    

    
                
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
    colors={"white":(255,255,255),"black":(0,0,0),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,50),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
    title=TITLE_FONT.render('Settings', 1, colors.get(txtcolor))
    text5=MENU_FONT.render('Smaller Screen', 1, colors.get(txtcolor))
    text6=MENU_FONT.render('Bigger Screen', 1, colors.get(txtcolor))
    

    screen.fill(colors.get(bgcolor))

    
    Button_6 = pygame.Rect(WIDTH//3-WIDTH//8, 2*HEIGHT//4, WIDTH//4, HEIGHT//14)
    Button_7 = pygame.Rect(2*WIDTH//3-WIDTH//8, 2*HEIGHT//4, WIDTH//4, HEIGHT//14)
    Button_8 = pygame.Rect(WIDTH//4-WIDTH//12, 3*HEIGHT//4, 3*WIDTH//4, HEIGHT//14)
    Button_9 = pygame.Rect(WIDTH//4+WIDTH//12, 3*HEIGHT//4, 3*WIDTH//4, HEIGHT//14)

   
    pygame.draw.rect(screen, colors.get("black"), Button_6)
    pygame.draw.rect(screen, colors.get("black"), Button_7)
    pygame.draw.rect(screen, colors.get("black"), Button_8)
    screen.blit(title, (WIDTH//2-8*WIDTH//18,50))
    screen.blit(text5, (WIDTH//3-WIDTH//8, 2*HEIGHT//4))
    screen.blit(text6, (2*WIDTH//3-WIDTH//8, 2*HEIGHT//4))
    

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
                    pygame.draw.rect(screen, colors.get("black"), Button_9)
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

    




    



    


mainMenu()



