import os, pygame, time, random, math

os.system('cls')
pygame.init
WIDTH=700 
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(0,100,50),"yellow":(255,255,0),"purple":(229,204,255),"randt":(random.randint(0,255), random.randint(0,255), random.randint(0,255)),"randb":(random.randint(0,255), random.randint(0,255), random.randint(0,255))}
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
clock = pygame.time.Clock()
FPS = 50
def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()


