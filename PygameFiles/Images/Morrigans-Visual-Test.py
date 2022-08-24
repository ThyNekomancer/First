import pygame, time, os,random, math, datetime, sys

os.system('cls')
pygame.init
WIDTH=700 
HEIGHT=700
bgcolor=('purple')
txtcolor=('blue')
pygame.font.get_fonts
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,0),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()
FPS = 50
MENU_FONT = pygame.font.SysFont('timesnewroman', WIDTH//35)
def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(colors.get(bgcolor))
        text=MENU_FONT.render('hi', 1, colors.get(txtcolor))
        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()


