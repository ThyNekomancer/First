#Maria Suarez
#6/9/2022
#We are learning pygame basic functins, 
# creating screens, clrs, shape

import pygame, time,os
pygame.init()#initialize the pygame package
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors= {'white':(255,255,255,),'blue':(0,0,255),'Green':(0,255,0)}
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
greenClr=(0,255,0)
# screen.fill(greenClr)
# pygame.display.update()
# pygame.time.delay(2000)
redClr=(255,0,0)
purpleClr=(125,0,125)
# screen.fill(redClr)
# pygame.display.update()
# pygame.time.delay(2000)
hb=50
wb=50
xb=100
yb=300
square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
#keep running create a lp
circleClr=colors.get('blue')
backgrnd=colors.get('Green')
run = True
speed = 5
cx=350
cy=350
rad=25
while run:
    screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("Y quit")

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb+speed):
        square.x += speed
    if keys[pygame.K_LEFT] and square.x > speed:
        square.x -= speed
    if keys[pygame.K_DOWN] and square.y <HEIGHT-(hb+speed):
        square.y += speed
    if keys[pygame.K_UP] and square.y > speed:
        square.y -= speed 
    if keys[pygame.K_d] and cx <WIDTH -(rad):
        cx += speed
    if keys[pygame.K_a] and cx> (speed+rad):
        cx -= speed
    if keys[pygame.K_w] and cy> (speed+rad):
        cy -= speed
    if keys[pygame.K_s] and cy <HEIGHT -(rad):
        cy += speed



    #rect(surface, color, rect) -> Rect
    pygame.draw.rect(screen, redClr,square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, circleClr, (cx,cy), rad)
    pygame.display.update()
