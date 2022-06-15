#Willow Collins


import pygame, time, os, random, math, sys, datetime
pygame.init()
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
screen = pygame.display.set_mode((WIDTH, HEIGHT))
Markers=[]
MxMy=(0,0)



def zer_grid():
    for x in range(3):
        row=[0]*3
        Markers.append(row)






        
#zer_grid()
#print(Markers)
#Markers[1][1]=-1
#print(Markers)
#print(Markers[1][1])

def draw_grid():
    bgClr=colors.get ('PALE_TURQUOISE_4')
    lineClr= colors.get('pimk')
    screen.fill(bgClr)
    for x in range (1,3):
        pygame.draw.line(screen, lineClr,(0,WIDTH//3*x),(WIDTH,WIDTH//3), lineWidth)
        pygame.draw.line(screen, lineClr,(0,WIDTH//3*x),(WIDTH,WIDTH//3), lineWidth)
        pygame.display.update()
        pygame.time.delay(100)

    pygame.time.delay(1000)
draw_grid
