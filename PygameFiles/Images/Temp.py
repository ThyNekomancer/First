MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//40)
title=MENU_FONT.render('congrats ' +name + ',you got a score of 150!', 1, colors.get(txtcolor))
screen.fill(colors.get(bgcolor))
screen.blit(title, (WIDTH//2, HEIGHT//2))
x=50
y=550
pygame.display.update()
pygame.time.delay(2000)
win = pygame.display.set_mode((700,700))
mainMenu()