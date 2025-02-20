import pygame

pygame.init()
surface = pygame.display.set_mode((400,500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    rectangle = pygame.draw.rect(surface, pygame.Color("blue"), pygame.Rect(30,30,60,60))
    pygame.display.flip()