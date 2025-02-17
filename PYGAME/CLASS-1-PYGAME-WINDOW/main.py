import pygame

pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT = 500,500
display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

background = pygame.image.load("PYGAME\CLASS-1-PYGAME-WINDOW\\background.png")
background_img = pygame.transform.scale(background.convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))

penguin = pygame.image.load("PYGAME\CLASS-1-PYGAME-WINDOW\\penguin.png")
penguin_img = pygame.transform.scale(penguin.convert_alpha(),(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
penguin_rect = penguin_img.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 - 30))

text = pygame.font.Font(None, 40).render("Welcome", True, pygame.Color("black"))
text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 120))
def gameloop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_img,(0,0))
        display_surface.blit(penguin_img,penguin_rect)
        display_surface.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    gameloop()
