import pygame
pygame.init()
surface = pygame.display.set_mode((400,400))
BLUE = (0,0,255)
RED = (255,0,0)
pygame.draw.circle(surface,BLUE,(100,100),50)
pygame.draw.circle(surface,RED,(300,300),100,5)
pygame.display.update()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


