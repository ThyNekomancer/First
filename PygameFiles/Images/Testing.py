from platform import platform
from tkinter import Menu
from turtle import title
from unittest import main
import pygame, time, os,random, math, datetime, sys


date=datetime.datetime.now()
pygame.init()
os.system('cls')
clock = pygame.time.Clock



WIDTH=700 
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,0),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
message=['Instructions', 'Settings', 'Easy',  "Medium", 'Hard', 'Scoreboard', 'Exit']

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
    
    #pygame.draw.rect(screen, colors.get('purple'), Button_settings)
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
        #pygame.time.delay(50)
        yMenu += HEIGHT//8
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
               pygame.quit()
               sys.exit 

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
                    Easy()
                if Button_Game3.collidepoint((mx,my)):
                    Easy()
                if Button_score.collidepoint((mx,my)):
                    scoreboard()
                if Button_exit.collidepoint((mx,my)):
                    exit()

def test():
    global bg
    screen.blit(bg, (0,0))
    pygame.display.update
    platform = pygame.Rect(WIDTH//4-WIDTH//12, HEIGHT//4, WIDTH//6, HEIGHT//14)
    pygame.draw.rect(screen, colors.get("blue"), platform)

def Easy():
    global height, walkCount
    import pygame
    pygame.init()

    win = pygame.display.set_mode((500,480))
    pygame.image.load('bgSmaller.jpg')

    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
    bg = pygame.image.load('bgSmaller.jpg')
    char = pygame.image.load('standing.png')

    x = 50
    y = 400
    width = 40
    height = 60
    vel = 5

    clock = pygame.time.Clock()

    isJump = False
    jumpCount = 10

    left = False
    right = False
    walkCount = 0

    def Play():
        global walkCount
        
        win.blit(bg, (0,0))  
        if walkCount + 1 >= 27:
            walkCount = 0
            
        if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0
            
        pygame.display.update() 
        


    run = True

    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and x > vel: 
            x -= vel
            left = True
            right = False

        elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
            x += vel
            left = False
            right = True
            
        else: 
            left = False
            right = False
            walkCount = 0
            
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False

    
    
    


    

    
                
    
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
                #pygame.time.delay(50)
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
                   # screen.blit(textSurface, name(Button_9,mx+5, Button_9,my+5))
                    screen.blit(textSurface, Button_9)
                    pygame.display.flip()
                    #screen.blit(name, Button_9)
                 


def exit():
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    title=MENU_FONT.render('byeeeeeeeee B)', 1, colors.get(txtcolor))
    screen.fill(colors.get(bgcolor))
    screen.blit(title, (WIDTH//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

    



def Play():
    global score, hb, wb, xb, rad, yb, charx, chary, cx, cy, speed, ibox, xig, yig, char, bg, mx, my, insSquare, txtcolor, bgcolor
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    title=TITLE_FONT.render('Circle Eats Square', 1, colors.get(txtcolor))
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
def GameThree():
    # TICTACTOE  
    # zero_Array() 
    # draw_grid() 
    # draw_markers() 
    # checkWinner() 
    # Game_end()

    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    clock = pygame.time.Clock
    scoreo = 0
    scorex = 0
    colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 0,255),
    # SHADES,
    "BLACK" : (0, 0, 0),
    "DARK_GREY" : (60, 60, 60),
    "DARK_SLATE_GREY" : (47, 79, 79),
    "DIM_GREY" : (105, 105, 105),
    "FREE_SPEECH_GREY" : (99, 86, 136),
    "GREY" : (190, 190, 190),
    "GREY0" : (0, 0, 0),
    "GREY1" : (3, 3, 3),
    "GREY2" : (5, 5, 5),
    "GREY3" : (8, 8, 8),
    "GREY4" : (10, 10, 10),
    "GREY5" : (13, 13, 13),
    "GREY6" : (15, 15, 15),
    "GREY7" : (18, 18, 18),
    "GREY8" : (20, 20, 20),
    "GREY9" : (23, 23, 23),
    "GREY10" : (26, 26, 26),
    "GREY11" : (28, 28, 28),
    "GREY12" : (31, 31, 31),
    "GREY13" : (33, 33, 33),
    "GREY14" : (36, 36, 36),
    "GREY15" : (38, 38, 38),
    "GREY16" : (41, 41, 41),
    "GREY17" : (43, 43, 43),
    "GREY18" : (46, 46, 46),
    "GREY19" : (48, 48, 48),
    "GREY20" : (51, 51, 51),
    "GREY21" : (54, 54, 54),
    "GREY22" : (56, 56, 56),
    "GREY23" : (59, 59, 59),
    "GREY24" : (61, 61, 61),
    "GREY25" : (64, 64, 64),
    "GREY26" : (66, 66, 66),
    "GREY27" : (69, 69, 69),
    "GREY28" : (71, 71, 71),
    "GREY29" : (74, 74, 74),
    "GREY30" : (77, 77, 77),
    "GREY31" : (79, 79, 79),
    "GREY32" : (82, 82, 82),
    "GREY33" : (84, 84, 84),
    "GREY34" : (87, 87, 87),
    "GREY35" : (89, 89, 89),
    "GREY36" : (92, 92, 92),
    "GREY37" : (94, 94, 94),
    "GREY38" : (97, 97, 97),
    "GREY39" : (99, 99, 99),
    "GREY40" : (102, 102, 102),
    "GREY41" : (105, 105, 105),
    "GREY42" : (107, 107, 107),
    "GREY43" : (110, 110, 110),
    "GREY44" : (112, 112, 112),
    "GREY45" : (115, 115, 115),
    "GREY46" : (117, 117, 117),
    "GREY47" : (120, 120, 120),
    "GREY48" : (122, 122, 122),
    "GREY49" : (125, 125, 125),
    "GREY50" : (127, 127, 127),
    "GREY51" : (130, 130, 130),
    "GREY52" : (133, 133, 133),
    "GREY53" : (135, 135, 135),
    "GREY54" : (138, 138, 138),
    "GREY55" : (140, 140, 140),
    "GREY56" : (143, 143, 143),
    "GREY57" : (145, 145, 145),
    "GREY58" : (148, 148, 148),
    "GREY59" : (150, 150, 150),
    "GREY60" : (153, 153, 153),
    "GREY61" : (156, 156, 156),
    "GREY62" : (158, 158, 158),
    "GREY63" : (161, 161, 161),
    "GREY64" : (163, 163, 163),
    "GREY65" : (166, 166, 166),
    "GREY66" : (168, 168, 168),
    "GREY67" : (171, 171, 171),
    "GREY68" : (173, 173, 173),
    "GREY69" : (176, 176, 176),
    "GREY70" : (179, 179, 179),
    "GREY71" : (181, 181, 181),
    "GREY72" : (184, 184, 184),
    "GREY73" : (186, 186, 186),
    "GREY74" : (189, 189, 189),
    "GREY75" : (191, 191, 191),
    "GREY76" : (194, 194, 194),
    "GREY77" : (196, 196, 196),
    "GREY78" : (199, 199, 199),
    "GREY79" : (201, 201, 201),
    "GREY80" : (204, 204, 204),
    "GREY81" : (207, 207, 207),
    "GREY82" : (209, 209, 209),
    "GREY83" : (212, 212, 212),
    "GREY84" : (214, 214, 214),
    "GREY85" : (217, 217, 217),
    "GREY86" : (219, 219, 219),
    "GREY87" : (222, 222, 222),
    "GREY88" : (224, 224, 224),
    "GREY89" : (227, 227, 227),
    "GREY90" : (229, 229, 229),
    "GREY91" : (232, 232, 232),
    "GREY92" : (235, 235, 235),
    "GREY93" : (237, 237, 237),
    "GREY94" : (240, 240, 240),
    "GREY95" : (242, 242, 242),
    "GREY96" : (245, 245, 245),
    "GREY97" : (247, 247, 247),
    "GREY98" : (250, 250, 250),
    "GREY99" : (252, 252, 252),
    "LIGHT_GREY" : (211, 211, 211),
    "SLATE_GREY" : (112, 128, 144),
    "SLATE_GREY_1" : (198, 226, 255),
    "SLATE_GREY_2" : (185, 211, 238),
    "SLATE_GREY_3" : (159, 182, 205),
    "SLATE_GREY_4" : (108, 123, 139),
    "VERY_LIGHT_GREY" : (205, 205, 205),
    "WHITE" : (255, 255,255),
    
    
    "ALICE_BLUE" : (240, 248, 255),
    "AQUA" : (0, 255, 255),
    "AQUAMARINE" : (127, 255, 212),
    "AQUAMARINE_1" : (127, 255, 212),
    "AQUAMARINE_2" : (118, 238, 198),
    "AQUAMARINE_3" : (102, 205, 170),
    "AQUAMARINE_4" : (69, 139, 116),
    "AZURE" : (240, 255, 255),
    "AZURE_1" : (240, 255, 255),
    "AZURE_2" : (224, 238, 238),
    "AZURE_3" : (193, 205, 205),
    "AZURE_4" : (131, 139, 139),
    "BLUE_1" : (0, 0, 255),
    "BLUE_2" : (0, 0, 238),
    "BLUE_3" : (0, 0, 205),
    "BLUE_4" : (0, 0, 139),
    "BLUE_VIOLET" : (138, 43, 226),
    "CADET_BLUE" : (95, 159, 159),
    "CADET_BLUE_1" : (1152, 245, 255),
    "CADET_BLUE_2" : (142, 229, 238),
    "CADET_BLUE_3" : (122, 197, 205),
    "CADET_BLUE_4" : (83, 134, 139),
    "CORN_FLOWER_BLUE" : (66, 66, 111),
    "CYAN" : (0, 255, 255),
    "CYAN_1" : (0, 255, 255),
    "CYAN_2" : (0, 238, 238),
    "CYAN_3" : (0, 205, 205),
    "CYAN_4" : (0, 139, 139),
    "DARK_SLATE_BLUE" : (36, 24, 130),
    "DARK_TURQUOISE" : (112, 147, 219),
    "DEEP_SKY_BLUE" : (0, 191, 255),
    "DEEP_SKY_BLUE_1" : (0, 191, 255),
    "DEEP_SKY_BLUE_2" : (0, 178, 238),
    "DEEP_SKY_BLUE_3" : (0, 154, 205),
    "DEEP_SKY_BLUE_4" : (0, 104, 139),
    "DODGER_BLUE" : (30, 144, 255),
    "DODGER_BLUE_1" : (30, 144, 255),
    "DODGER_BLUE_2" : (28, 134, 238),
    "DODGER_BLUE_3" : (24, 116, 205),
    "DODGER_BLUE_4" : (16, 78, 139),
    "FREE_SPEECH_BLUE" : (65, 86, 197),
    "LIGHT_BLUE" : (173, 216, 230),
    "LIGHT_BLUE_1" : (191, 239, 255),
    "LIGHT_BLUE_2" : (178, 223, 238),
    "LIGHT_BLUE_3" : (154, 192, 205),
    "LIGHT_BLUE_4" : (104, 131, 139),
    "LIGHT_CYAN" : (224, 255, 255),
    "LIGHT_CYAN_1" : (224, 255, 255),
    "LIGHT_CYAN_2" : (209, 238, 238),
    "LIGHT_CYAN_3" : (180, 205, 205),
    "LIGHT_CYAN_4" : (122, 139, 139),
    "LIGHT_SKY_BLUE" : (135, 206, 250),
    "LIGHT_SKY_BLUE_1" : (176, 226, 255),
    "LIGHT_SKY_BLUE_2" : (164, 211, 238),
    "LIGHT_SKY_BLUE_3" : (141, 182, 205),
    "LIGHT_SKY_BLUE_4" : (96, 123, 139),
    "LIGHT_SLATE_BLUE" : (132, 112, 255),
    "LIGHT_STEEL_BLUE" : (176, 196, 222),
    "LIGHT_STEEL_BLUE_1" : (202, 225, 255),
    "LIGHT_STEEL_BLUE_2" : (188, 210, 238),
    "LIGHT_STEEL_BLUE_3" : (162, 181, 205),
    "LIGHT_STEEL_BLUE_4" : (110, 123, 139),
    "MEDIUM_BLUE" : (0, 0, 205),
    "MEDIUM_SLATE_BLUE" : (123, 104, 238),
    "MEDIUM_TURQUOISE" : (72, 209, 204),
    "MIDNIGHT_BLUE" : (25, 25, 112),
    "NAVY" : (0, 0, 128),
    "NAVY_BLUE" : (0, 0, 128),
    "NEON_BLUE" : (77, 77, 255),
    "NEW_MIDNIGHT_BLUE" : (0, 0, 156),
    "PALE_TURQUOISE" : (187, 255, 255),
    "PALE_TURQUOISE_1" : (187, 255, 255),
    "PALE_TURQUOISE_2" : (174, 238, 238),
    "PALE_TURQUOISE_3" : (150, 205, 205),
    "PALE_TURQUOISE_4" : (102, 139, 139),
    "POWDER_BLUE" : (176, 224, 230),
    "RICH_BLUE" : (89, 89, 171),
    "ROYAL_BLUE" : (65, 105, 225),
    "ROYAL_BLUE_1" : (72, 118, 255),
    "ROYAL_BLUE_2" : (67, 110, 238),
    "ROYAL_BLUE_3" : (58, 95, 205),
    "ROYAL_BLUE_4" : (39, 64, 139),
    "ROYAL_BLUE_5" : (0, 34, 102),
    "SKY_BLUE" : (135, 206, 235),
    "SKY_BLUE_1" : (135, 206, 255),
    "SKY_BLUE_2" : (126, 192, 238),
    "SKY_BLUE_3" : (108, 166, 205),
    "SKY_BLUE_4" : (74, 112, 139),
    "SLATE_BLUE" : (131, 111, 255),
    "SLATE_BLUE_1" : (122, 103, 238),
    "SLATE_BLUE_2" : (122, 103, 238),
    "SLATE_BLUE_3" : (105, 89, 205),
    "SLATE_BLUE_4" : (71, 60, 139),
    "STEEL_BLUE" : (70, 130, 180),
    "STEEL_BLUE_1" : (99, 184, 255),
    "STEEL_BLUE_2" : (92, 172, 238),
    "STEEL_BLUE_3" : (79, 148, 205),
    "STEEL_BLUE_4" : (54, 100, 139),
    "SUMMER_SKY" : (56, 176, 222),
    "TEAL" : (0, 128, 128),
    "TRUE_IRIS_BLUE" : (3, 180, 204),
    "TURQUOISE" : (64, 224, 208),
    "TURQUOISE_1" : (0, 245, 255),
    "TURQUOISE_2" : (0, 229, 238),
    "TURQUOISE_3" : (0, 197, 205),
    "TURQUOISE_4" : (0, 134,139),
    
    
    "BAKERS_CHOCOLATE" : (92, 51, 23),
    "BEIGE" : (245, 245, 220),
    "BROWN" : (166, 42, 42),
    "BROWN_1" : (255, 64, 64),
    "BROWN_2" : (238, 59, 59),
    "BROWN_3" : (205, 51, 51),
    "BROWN_4" : (139, 35, 35),
    "BURLYWOOD" : (222, 184, 135),
    "BURLYWOOD_1" : (255, 211, 155),
    "BURLYWOOD_2" : (238, 197, 145),
    "BURLYWOOD_3" : (205, 170, 125),
    "BURLYWOOD_4" : (139, 115, 85),
    "CHOCOLATE" : (210, 105, 30),
    "CHOCOLATE_1" : (255, 127, 36),
    "CHOCOLATE_2" : (238, 118, 33),
    "CHOCOLATE_3" : (205, 102, 29),
    "CHOCOLATE_4" : (139, 69, 19),
    "DARK_BROWN" : (92, 64, 51),
    "DARK_TAN" : (151, 105, 79),
    "DARK_WOOD" : (133, 94, 66),
    "LIGHT_WOOD" : (133, 99, 99),
    "MEDIUM_WOOD" : (166, 128, 100),
    "NEW_TAN" : (235, 199, 158),
    "PERU" : (205, 133, 63),
    "ROSY_BROWN" : (188, 143, 143),
    "ROSY_BROWN_1" : (255, 193, 193),
    "ROSY_BROWN_2" : (238, 180, 180),
    "ROSY_BROWN_3" : (205, 155, 155),
    "ROSY_BROWN_4" : (139, 105, 105),
    "SADDLE_BROWN" : (139, 69, 19),
    "SANDY_BROWN" : (244, 164, 96),
    "SEMI_SWEET_CHOCOLATE" : (107, 66, 38),
    "SIENNA" : (142, 107, 35),
    "TAN" : (219, 147, 112),
    "TAN_1" : (255, 165, 79),
    "TAN_2" : (238, 154, 73),
    "TAN_3" : (205, 133, 63),
    "TAN_4" : (139, 90, 43),
    "VERY_DARK_BROWN" : (92, 64,51),
    
    "CHARTREUSE" : (127, 255, 0),
    "CHARTREUSE_1" : (127, 255, 0),
    "CHARTREUSE_2" : (118, 238, 0),
    "CHARTREUSE_3" : (102, 205, 0),
    "CHARTREUSE_4" : (69, 139, 0),
    "DARK_GREEN" : (47, 79, 47),
    "DARK_GREEN_COPPER" : (74, 118, 110),
    "DARK_KHAKI" : (189, 183, 107),
    "DARK_OLIVE_GREEN" : (85, 107, 47),
    "DARK_OLIVE_GREEN_1" : (202, 255, 112),
    "DARK_OLIVE_GREEN_2" : (188, 238, 104),
    "DARK_OLIVE_GREEN_3" : (162, 205, 90),
    "DARK_OLIVE_GREEN_4" : (110, 139, 61),
    "DARK_SEA_GREEN" : (143, 188, 143),
    "DARK_SEA_GREEN_1" : (193, 255, 193),
    "DARK_SEA_GREEN_2" : (180, 238, 180),
    "DARK_SEA_GREEN_3" : (155, 205, 155),
    "DARK_SEA_GREEN_4" : (105, 139, 105),
    "FOREST_GREEN" : (34, 139, 34),
    "FREE_SPEECH_GREEN" : (9, 249, 17),
    "GREEN_1" : (0, 255, 0),
    "GREEN_2" : (0, 238, 0),
    "GREEN_3" : (0, 205, 0),
    "GREEN_4" : (0, 139, 0),
    "GREEN_YELLOW" : (173, 255, 47),
    "KHAKI" : (240, 230, 140),
    "KHAKI_1" : (255, 246, 143),
    "KHAKI_2" : (238, 230, 133),
    "KHAKI_3" : (205, 198, 115),
    "KHAKI_4" : (139, 134, 78),
    "LAWN_GREEN" : (124, 252, 0),
    "LIGHT_SEA_GREEN" : (32, 178, 170),
    "LIME" : (0, 255, 0),
    "MEDIUM_SEA_GREEN" : (60, 179, 113),
    "MEDIUM_SPRING_GREEN" : (0, 250, 154),
    "MINT_CREAM" : (245, 255, 250),
    "OLIVE" : (128, 128, 0),
    "OLIVE_DRAB" : (107, 142, 35),
    "OLIVE_DRAB_1" : (192, 255, 62),
    "OLIVE_DRAB_2" : (179, 238, 58),
    "OLIVE_DRAB_3" : (154, 205, 50),
    "OLIVE_DRAB_4" : (105, 139, 34),
    "PALE_GREEN" : (152, 251, 152),
    "PALE_GREEN_1" : (154, 255, 154),
    "PALE_GREEN_2" : (144, 238, 144),
    "PALE_GREEN_3" : (124, 205, 124),
    "PALE_GREEN_4" : (84, 139, 84),
    "SEA_GREEN" : (46, 139, 87),
    "SEA_GREEN_1" : (84, 255, 159),
    "SEA_GREEN_2" : (78, 238, 148),
    "SEA_GREEN_3" : (67, 205, 128),
    "SEA_GREEN_4" : (46, 139, 87),
    "SPRING_GREEN" : (0, 255, 127),
    "SPRING_GREEN_1" : (0, 255, 127),
    "SPRING_GREEN_2" : (0, 238, 118),
    "SPRING_GREEN_3" : (0, 205, 102),
    "SPRING_GREEN_4" : (0, 139, 69),
    "YELLOW_GREEN" : (154, 205,50),
    "BISQUE" : (255, 228, 196),
    "BISQUE_1" : (255, 228, 196),
    "BISQUE_2" : (238, 213, 183),
    "BISQUE_3" : (205, 183, 158),
    "BISQUE_4" : (139, 125, 107),
    "CORAL" : (255, 127, 0),
    "CORAL_1" : (255, 114, 86),
    "CORAL_2" : (238, 106, 80),
    "CORAL_3" : (205, 91, 69),
    "CORAL_4" : (139, 62, 47),
    "DARK_ORANGE" : (255, 140, 0),
    "DARK_ORANGE_1" : (255, 127, 0),
    "DARK_ORANGE_2" : (238, 118, 0),
    "DARK_ORANGE_3" : (205, 102, 0),
    "DARK_ORANGE_4" : (139, 69, 0),
    "DARK_SALMON" : (233, 150, 122),
    "HONEYDEW" : (240, 255, 240),
    "HONEYDEW_1" : (240, 255, 240),
    "HONEYDEW_2" : (224, 238, 224),
    "HONEYDEW_3" : (193, 205, 193),
    "HONEYDEW_4" : (131, 139, 131),
    "LIGHT_CORAL" : (240, 128, 128),
    "LIGHT_SALMON" : (255, 160, 122),
    "LIGHT_SALMON_1" : (255, 160, 122),
    "LIGHT_SALMON_2" : (238, 149, 114),
    "LIGHT_SALMON_3" : (205, 129, 98),
    "LIGHT_SALMON_4" : (139, 87, 66),
    "MANDARIN_ORANGE" : (142, 35, 35),
    "ORANGE" : (255, 165, 0),
    "ORANGE_1" : (255, 165, 0),
    "ORANGE_2" : (238, 154, 0),
    "ORANGE_3" : (205, 133, 0),
    "ORANGE_4" : (139, 90, 0),
    "ORANGE_RED" : (255, 36, 0),
    "PEACH_PUFF" : (255, 218, 185),
    "PEACH_PUFF_1" : (255, 218, 185),
    "PEACH_PUFF_2" : (238, 203, 173),
    "PEACH_PUFF_3" : (205, 175, 149),
    "PEACH_PUFF_4" : (139, 119, 101),
    "SALMON" : (250, 128, 114),
    "SALMON_1" : (255, 140, 105),
    "SALMON_2" : (238, 130, 98),
    "SALMON_3" : (205, 112, 84),
    "SALMON_4" : (139, 76, 57),
    "SIENNA_1" : (255, 130, 71),
    "SIENNA_2" : (238, 121, 66),
    "SIENNA_3" : (205, 104, 57),
    "SIENNA_4" : (139, 71, 38),
    "DEEP_PINK," : (255, 20, 147),
    "DEEP_PINK_1" : (255, 20, 147),
    "DEEP_PINK_2" : (238, 18, 137),
    "DEEP_PINK_3" : (205, 16, 118),
    "DEEP_PINK_4" : (139, 10, 80),
    "DUSTY_ROSE" : (133, 99, 99),
    "FIREBRICK" : (178, 34, 34),
    "FIREBRICK_1" : (255, 48, 48),
    "FIREBRICK_2" : (238, 44, 44),
    "FIREBRICK_3" : (205, 38, 38),
    "FIREBRICK_4" : (139, 26, 26),
    "FELDSPAR" : (209, 146, 117),
    "FLESH" : (245, 204, 176),
    "FREE_SPEECH_MAGENTA" : (227, 91, 216),
    "FREE_SPEECH_RED" : (192, 0, 0),
    "HOT_PINK" : (255, 105, 180),
    "HOT_PINK_1" : (255, 110, 180),
    "HOT_PINK_2" : (238, 106, 167),
    "HOT_PINK_3" : (205, 96, 144),
    "HOT_PINK_4" : (139, 58, 98),
    "INDIAN_RED" : (205, 92, 92),
    "INDIAN_RED_1" : (255, 106, 106),
    "INDIAN_RED_2" : (238, 99, 99),
    "INDIAN_RED_3" : (205, 85, 85),
    "INDIAN_RED_4" : (139, 58, 58),
    "LIGHT_PINK" : (255, 182, 193),
    "LIGHT_PINK_1" : (255, 174, 185),
    "LIGHT_PINK_2" : (238, 162, 173),
    "LIGHT_PINK_3" : (205, 140, 149),
    "LIGHT_PINK_4" : (139, 95, 101),
    "MEDIUM_VIOLET_RED" : (199, 21, 133),
    "MISTY_ROSE" : (255, 228, 225),
    "MISTY_ROSE_1" : (255, 228, 225),
    "MISTY_ROSE_2" : (238, 213, 210),
    "MISTY_ROSE_3" : (205, 183, 181),
    "MISTY_ROSE_4" : (139, 125, 123),
    "ORANGE_RED_1" : (255, 69, 0),
    "ORANGE_RED_2" : (238, 64, 0),
    "ORANGE_RED_3" : (205, 55, 0),
    "ORANGE_RED_4" : (139, 37, 0),
    "PALE_VIOLET_RED" : (219, 112, 147),
    "PALE_VIOLET_RED_1" : (255, 130, 171),
    "PALE_VIOLET_RED_2" : (238, 121, 159),
    "PALE_VIOLET_RED_3" : (205, 104, 137),
    "PALE_VIOLET_RED_4" : (139, 71, 93),
    "PINK" : (255, 192, 203),
    "PINK_1" : (255, 181, 197),
    "PINK_2" : (238, 169, 184),
    "PINK_3" : (205, 145, 158),
    "PINK_4" : (139, 99, 108),
    "RED_1" : (255, 0, 0),
    "RED_2" : (238, 0, 0),
    "RED_3" : (205, 0, 0),
    "RED_4" : (139, 0, 0),
    "SCARLET" : (140, 23, 23),
    "SPICY_PINK" : (255, 28, 174),
    "TOMATO" : (255, 99, 71),
    "TOMATO_1" : (255, 99, 71),
    "TOMATO_2" : (238, 92, 66),
    "TOMATO_3" : (205, 79, 57),
    "TOMATO_4" : (139, 54, 38),
    "VIOLET_RED" : (208, 32, 144),
    "VIOLET_RED_1" : (255, 62, 150),
    "VIOLET_RED_2" : (238, 58, 140),
    "VIOLET_RED_3" : (205, 50, 120),
    "VIOLET_RED_4" : (139, 34, 82),
    
    "DARK_ORCHID," : (153, 50, 204),
    "DARK_ORCHID_1" : (191, 62, 255),
    "DARK_ORCHID_2" : (178, 58, 238),
    "DARK_ORCHID_3" : (154, 50, 205),
    "DARK_ORCHID_4" : (104, 34, 139),
    "DARK_PURPLE" : (135, 31, 120),
    "DARK_VIOLET" : (148, 0, 211),
    "FUCHSIA" : (255, 0, 255),
    "LAVENDER" : (230, 230, 250),
    "LAVENDER_BLUSH" : (255, 240, 245),
    "LAVENDER_BLUSH_1" : (255, 240, 245),
    "LAVENDER_BLUSH_2" : (238, 224, 229),
    "LAVENDER_BLUSH_3" : (205, 193, 197),
    "LAVENDER_BLUSH_4" : (139, 131, 134),
    "MAGENTA" : (255, 0, 255),
    "MAGENTA_1" : (255, 0, 255),
    "MAGENTA_2" : (238, 0, 238),
    "MAGENTA_3" : (205, 0, 205),
    "MAGENTA_4" : (139, 0, 139),
    "MAROON" : (176, 48, 96),
    "MAROON_1" : (255, 52, 179),
    "MAROON_2" : (238, 48, 167),
    "MAROON_3" : (205, 41, 144),
    "MAROON_4" : (139, 28, 98),
    "MEDIUM_ORCHID" : (186, 85, 211),
    "MEDIUM_ORCHID_1" : (224, 102, 255),
    "MEDIUM_ORCHID_2" : (209, 95, 238),
    "MEDIUM_ORCHID_3" : (180, 82, 205),
    "MEDIUM_ORCHID_4" : (122, 55, 139),
    "MEDIUM_PURPLE" : (147, 112, 219),
    "MEDIUM_PURPLE_1" : (171, 130, 255),
    "MEDIUM_PURPLE_2" : (159, 121, 238),
    "MEDIUM_PURPLE_3" : (137, 104, 205),
    "MEDIUM_PURPLE_4" : (93, 71, 139),
    "NEON_PINK" : (255, 110, 199),
    "ORCHID" : (218, 112, 214),
    "ORCHID_1" : (219, 112, 219),
    "ORCHID_2" : (238, 122, 233),
    "ORCHID_3" : (205, 105, 201),
    "ORCHID_4" : (139, 71, 137),
    "PLUM" : (221, 160, 221),
    "PLUM_1" : (255, 187, 255),
    "PLUM_2" : (238, 174, 238),
    "PLUM_3" : (205, 150, 205),
    "PLUM_4" : (139, 102, 139),
    "PURPLE" : (160, 32, 240),
    "PURPLE_1" : (155, 48, 255),
    "PURPLE_2" : (145, 44, 238),
    "PURPLE_3" : (125, 38, 205),
    "PURPLE_4" : (85, 26, 139),
    "THISTLE" : (216, 191, 216),
    "THISTLE_1" : (255, 225, 255),
    "THISTLE_2" : (238, 210, 238),
    "THISTLE_3" : (205, 181, 205),
    "THISTLE_4" : (139, 123, 139),
    "VIOLET" : (238, 130, 238),
    "VIOLET_BLUE" : (159, 95, 159),
    
    "BLANCHED_ALMOND," : (255, 235, 205),
    "DARK_GOLDENROD" : (184, 134, 11),
    "DARK_GOLDENROD_1" : (255, 185, 15),
    "DARK_GOLDENROD_2" : (238, 173, 14),
    "DARK_GOLDENROD_3" : (205, 149, 12),
    "DARK_GOLDENROD_4" : (139, 101, 8),
    "LEMON_CHIFFON" : (255, 250, 205),
    "LEMON_CHIFFON_1" : (255, 250, 205),
    "LEMON_CHIFFON_2" : (238, 233, 191),
    "LEMON_CHIFFON_3" : (205, 201, 165),
    "LEMON_CHIFFON_4" : (139, 137, 112),
    "LIGHT_GOLDENROD" : (238, 221, 130),
    "LIGHT_GOLDENROD_1" : (255, 236, 139),
    "LIGHT_GOLDENROD_2" : (238, 220, 130),
    "LIGHT_GOLDENROD_3" : (205, 190, 112),
    "LIGHT_GOLDENROD_4" : (139, 129, 76),
    "LIGHT_GOLDENROD_YELLOW" : (250, 250, 210),
    "LIGHT_YELLOW" : (255, 255, 224),
    "LIGHT_YELLOW_1" : (255, 255, 224),
    "LIGHT_YELLOW_2" : (238, 238, 209),
    "LIGHT_YELLOW_3" : (205, 205, 180),
    "LIGHT_YELLOW_4" : (139, 139, 122),
    "PALE_GOLDENROD" : (238, 232, 170),
    "PAPAYA_WHIP" : (255, 239, 213),
    "CORNSILK" : (255, 248, 220),
    "CORNSILK_1" : (255, 248, 220),
    "CORNSILK_2" : (238, 232, 205),
    "CORNSILK_3" : (205, 200, 177),
    "CORNSILK_4" : (139, 236, 120),
    "GOLDENROD" : (218, 165, 32),
    "GOLDENROD_1" : (255, 193, 37),
    "GOLDENROD_2" : (238, 180, 34),
    "GOLDENROD_3" : (205, 155, 29),
    "GOLDENROD_4" : (139, 105, 20),
    "MOCCASIN" : (255, 228, 181),
    "YELLOW" : (255, 255, 0),
    "YELLOW_1" : (255, 255, 0),
    "YELLOW_2" : (238, 238, 0),
    "YELLOW_3" : (205, 205, 0),
    "YELLOW_4" : (139, 139, 0),
    "GOLD" : (255, 215, 0),
    "GOLD_1" : (255, 215, 0),
    "GOLD_2" : (238, 201, 0),
    "GOLD_3" : (205, 173, 0),
    "GOLD_4" : (139, 117, 0),
    "MEDIUM_GOLDENROD" : (234, 234, 174),
    "ANTIQUE_WHITE" : (250, 235, 215),
    "ANTIQUE_WHITE_1" : (255, 239, 219),
    "ANTIQUE_WHITE_2" : (238, 223, 204),
    "ANTIQUE_WHITE_3" : (205, 192, 176),
    "ANTIQUE_WHITE_4" : (139, 131, 120),
    "FLORAL_WHITE" : (255, 250, 240),
    "GHOST_WHITE" : (248, 248, 255),
    "NAVAJO_WHITE" : (255, 222, 173),
    "NAVAJO_WHITE_1" : (255, 222, 173),
    "NAVAJO_WHITE_2" : (238, 207, 161),
    "NAVAJO_WHITE_3" : (205, 179, 139),
    "NAVAJO_WHITE_4" : (139, 121, 94),
    "OLD_LACE" : (253, 245, 230),
    "WHITE_SMOKE" : (245, 245, 245),
    "GAINSBORO" : (220, 220, 220),
    "IVORY" : (255, 255, 240),
    "IVORY_1" : (255, 255, 240),
    "IVORY_2" : (238, 238, 224),
    "IVORY_3" : (205, 205, 193),
    "IVORY_4" : (139, 139, 131),
    "LINEN" : (250, 240, 230),
    "SEASHELL" : (255, 245, 238),
    "SEASHELL_1" : (255, 245, 238),
    "SEASHELL_2" : (238, 229, 222),
    "SEASHELL_3" : (205, 197, 191),
    "SEASHELL_4" : (139, 134, 130),
    "SNOW" : (255, 250, 250),
    "SNOW_1" : (255, 250, 250),
    "SNOW_2" : (238, 233, 233),
    "SNOW_3" : (205, 201, 201),
    "SNOW_4" : (139, 137, 137),
    "WHEAT" : (245, 222, 179),
    "WHEAT_1" : (255, 231, 186),
    "WHEAT_2" : (238, 216, 174),
    "WHEAT_3" : (205, 186, 150),
    "WHEAT_4" : (139, 126, 102),
    "QUARTZ" : (217, 217, 243),
    }
    clr=colors.get("limeGreen")
    #create dispay wind with any name y like
    pygame.display.set_caption("Tic Tac Toe")  #change the title of my window
    backgrnd=colors.get("pink")

    #game Variable
    player=1        #Change players 1 and -1
    gameOver=False#check is game is Over
    winner=0        #save winner either 1 OR -1 ZERO means tie
    markers=[]      #CONTROL cells
    lineWidth=10    #thickness  drawing
    Game=True       #CONTROL game
    MxMy=(0,0)      #Clicks
    print(markers)  
    cirClr=colors.get("blue")     #circle COLOR
    xClr=colors.get("BLACK")      #X COLOR

    #FunctiOn TO ZERO OUR ARRAY
    def zero_Array(): 
        for x in range(3):
            row = [0] *3
            markers.append(row) #write was append, change back if it doesnt work

    def draw_grid():
        lineClr=colors.get("white")
        for x in range(1,3):
            pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #Hztal line
            pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth)  #Vert line
        pygame.time.delay(100)

    def draw_Markers():
        xValue=0
        for x in markers:   # getting a rw
            yValue=0
            for y in x:  #each elem fthe rw
                if y ==1:
                    
                    pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                    pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
                if y==-1:
                    
                    pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
                yValue +=1
            xValue +=1
        pygame.display.update()
    def checkWinner():
        nonlocal gameOver,winner#nonlocal instead of global
        x_pOs=0
        for x in markers:
            #check COL
            if sum(x) ==3:
                print("sum")
                winner = 1
                gameOver=True
            if sum(x) ==-3:
                winner = -1
                gameOver=True
            #Check ROWS
            if markers[0][x_pOs] +markers[1][x_pOs]+markers[2][x_pOs] == 3:
                winner = 1
                gameOver=True

            if markers[0][x_pOs] +markers[1][x_pOs]+markers[2][x_pOs] == -3:
                winner = -1
                gameOver=True
            x_pOs +=1
        # #Check DiagOnals 
        if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[2][0]+markers[1][1]+markers[0][2] == 3:
            winner = 1
            gameOver=True
        if markers[0][0]+markers[1][1]+markers[2][2] == -3 or markers[2][0]+markers[1][1]+markers[0][2] == -3:
            winner = -1
            gameOver=True
        #Check FOR a tie
        if gameOver ==False:
            tie=True
            for ROW in markers:
                for COL in ROW:
                    if COL ==0:
                        tie=False
            #LEts make winner =0 if it is tie
            if tie:   #in a bOOlean variable dOnt need ==  if tie == True
                gameOver=True
                winner=0
    def gameEnd():
        nonlocal Game, scoreo, scorex, markers, gameOver, clock
        Game = False
        if winner == 1:
            scorex+=1
        if winner == -1:
            scoreo+=1
        scro = str(scoreo)
        scrx = str(scorex)
        txtcolor = colors.get("IVORY") #i changed colors
        textxscore=MENU_FONT.render("X's score is "+scrx, 1, (txtcolor))
        textoscore=MENU_FONT.render("O's score is "+scro, 1, (txtcolor))
        textagn=MENU_FONT.render('Want to play again?', 1, (txtcolor))
        textyes=MENU_FONT.render('Yes', 1, (txtcolor))
        textno=MENU_FONT.render('No', 1, (txtcolor))
        aw = WIDTH//2 - (textagn.get_width()//2)
        yw = WIDTH//2 - (textyes.get_width()//2)
        nw = WIDTH//2 - (textno.get_width()//2)
        xw = WIDTH//2 - (textxscore.get_width()//2)
        ow = WIDTH//2 - (textoscore.get_width()//2)
        Buttony=pygame.Rect(yw, 4*HEIGHT//6, 35, 25)
        Button_n=pygame.Rect(nw, 5*HEIGHT//6, 30, 25)
        screen.fill(backgrnd)
        pygame.draw.rect(screen, colors.get('BLUE'), Buttony)
        pygame.draw.rect(screen, colors.get('BLUE'), Button_n)
        screen.blit(textxscore, (xw, HEIGHT//6))
        screen.blit(textoscore, (ow, 2*HEIGHT//6))
        screen.blit(textno, (nw, 5*HEIGHT//6))
        screen.blit(textyes, (yw, 4*HEIGHT//6))
        screen.blit(textagn, (aw, 3*HEIGHT//6))
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    print("Bye")
                    mainMenu()
                    #add menu if normal game
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    if Button_n.collidepoint((mx, my)):
                        pygame.event.get()
                        run = False
                        screen.fill(backgrnd)
                        if scorex>scoreo:
                            win = MENU_FONT.render("X won with an overall score of "+scrx, 1, (txtcolor))
                        if scoreo>scorex:
                            win = MENU_FONT.render("O won with an overall score of "+scro, 1, (txtcolor))
                        if scoreo == scorex:
                            win = MENU_FONT.render("It was a tie, each person with an overall score of "+scro, 1, (txtcolor))
                        dw = WIDTH//2 - (win.get_width()//2)
                        textbye=MENU_FONT.render('Bye!', 1, (txtcolor))
                        screen.blit(win, (dw, HEIGHT//4))
                        screen.blit(textbye, (WIDTH//2, HEIGHT//2))
                        pygame.display.update()
                        pygame.time.delay(3000)
                        mainMenu()


                    if Buttony.collidepoint((mx, my)):
                        markers.clear()
                        zero_Array()
                        gameOver = False
                        Gamef()
    zero_Array()
    def Gamef():
        nonlocal Game, player, markers, MxMy, gameOver# cellx, celly,#nonlocal instead of global bc in outer function?
        Game = True
        while Game:
            screen.fill(backgrnd)
            draw_grid()
            draw_Markers()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    #Menu(mainTitle,messageMenu)
                    mainMenu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    MxMy = pygame.mouse.get_pos()
                    cellx=MxMy[0]//(WIDTH//3)
                    celly=MxMy[1]//(HEIGHT//3)
                    # print(cellx, celly)
                    if markers[cellx][celly]==0:
                        markers[cellx][celly]=player
                        player *=-1
                        checkWinner()
                        print(winner)
                        if gameOver:
                            draw_Markers()
                            pygame.time.delay(60)
                            gameEnd()
                            gameOver = False
    Gamef()


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