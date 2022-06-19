
import pygame, time,os,random, math
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window

#images
bg=pygame.image.load('bgSmaller.jpg')
char = pygame.image.load('standing.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)


#square Var
hb=50
wb=50
xb=100
yb=300

charx = xb
chary = yb

cx=350
cy=350
rad=25
speed=1
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse varuables
mx = 0
my = 0

square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
Game = False
def settings():
    global title, text, text9,text10,text11,text12,text13
    global  screen, WIDTH, HEIGHT, colors
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//18)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
    colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,50),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
    title=TITLE_FONT.render('Settings', 1, colors.get('white'))
    text=MENU_FONT.render('Clr 1', 1, colors.get("yellow"))
    text9=MENU_FONT.render('Clr 2', 1, colors.get("pink"))
    text10=MENU_FONT.render('Random Clr', 1, colors.get("pink"))
    text11=MENU_FONT.render('Smaller Screen', 1, colors.get('blue'))
    text12=MENU_FONT.render('Bigger Screen', 1, colors.get('limeGreen'))
    text13=MENU_FONT.render('Enter Name: ', 1, colors.get('blue'))

def menu():
    global Title
    Title = TITLE_FONT.render("Circle eats Square", 1, colors.gte("blue"))

def Instructions():
    global Myfile
    global text3 
    global text4
    global text5
    #rendering text objects
    Title = TITLE_FONT.render("Menu", 1, colors.get("blue"))
    text1 = MENU_FONT.render("Begin Game", 1, colors.get("blue"))
    text2 = MENU_FONT.render("Exit program", 1, colors.get("blue"))
    text3 = MENU_FONT.render("scores", 1, colors.get("blue"))
    text4 = MENU_FONT.render("Instructions", 1, colors.get("blue"))
    text5 = MENU_FONT.render("settings", 1, colors.get("blue"))
    
    

    #fills screen with white
    screen.fill(colors.get("white"))

    #creating button options
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    Button_3 = pygame.Rect(200,600,100, 50 )
    Button_4 = pygame.Rect(400, 600, 100, 50)
    Button_5 = pygame.Rect(300, 500, 100, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_4)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_5)

    #Instructions
    myFile = open("instructions.txt")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))
    screen.blit(text3, (225,610))
    screen.blit(text4, (425,610))
    screen.blit(text5,(325,510))


    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    return True
                if Button_2.collidepoint((mx, my)):
                    pygame.quit()
                if Button_4.collidepoint((mx, my)):
                    screen.fill('pink')
                    pygame.display.update()
                    Myfile = open("How-To-Play.txt")
                    screen.fill('pink')
                    
                    Title = MENU_FONT.render("Begin Game", 1, colors.get("blue"))
                if Button_5.collidepoint((mx,my)):
                  
                  
                    title=TITLE_FONT.render('Settings', 1, colors.get('white'))
                    text=MENU_FONT.render('Clr 1', 1, colors.get("pink"))
                    text9=MENU_FONT.render('Clr 2', 1, colors.get("pink"))
                    text10=MENU_FONT.render('Random Clr', 1, colors.get("pink"))
                    text11=MENU_FONT.render('Smaller Screen', 1, colors.get('blue'))
                    text12=MENU_FONT.render('Bigger Screen', 1, colors.get('limeGreen'))
                    text13=MENU_FONT.render('Enter Name: ', 1, colors.get('blue'))




run = Instructions()

while run:
    # screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("Y quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            mx = mousePos[0]
            my = mousePos[1]
    screen.blit(bg, (0,0))
    keys= pygame.key.get_pressed() #this is a list
    #mve square
    if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
        square.x += speed
        charx += speed
    if keys[pygame.K_LEFT] and  square.x > speed:
        square.x -= speed
        charx -= speed
    if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
        square.y -= speed
        chary -= speed
    if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
        square.y += speed
        chary += speed
        #mve Circle
    if keys[pygame.K_d] and cx < WIDTH -(rad):
        cx += speed
        insSquare.x += speed
    if keys[pygame.K_a] and  cx > (speed+rad):
        cx -= speed
        insSquare.x -= speed
    if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
        cy -= speed
        insSquare.y -= speed
    if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
        cy += speed
        insSquare.y += speed

    


    if square.colliderect(insSquare):
        print("BOOM")
        rad+=1
        cx=random.randint(rad, WIDTH-rad)
        cy=random.randint(rad, HEIGHT-rad)
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)
    #rect(surface, color, rect) -> Rect
    pygame.draw.rect(screen, squareClr,square)
    screen.blit(char, (charx, chary))
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, circleClr, (cx,cy), rad)
    pygame.draw.rect(screen, squareClr, insSquare)
    pygame.display.update()