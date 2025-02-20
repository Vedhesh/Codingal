import pygame

pygame.init()

SCREEN_WIDTH,SCREEN_HEIGHT = 500,500
display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

bg_color = [58, 58, 58]
display_surface.fill(bg_color)

image = pygame.image.load("PYGAME\CLASS-1-PYGAME-WINDOW\PROJECT\\fixed_alpha.png")
image_scale = pygame.transform.scale(image.convert_alpha(),(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
image_rect = image_scale.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))

text_my = pygame.font.Font(None, 40).render("My", True, pygame.Color("white"))
text_my_rect = text_my.get_rect(center=(SCREEN_WIDTH//2 - 60, SCREEN_HEIGHT//2 + 140))

text_first = pygame.font.Font(None, 40).render("first", True, pygame.Color("white"))
text_first_rect = text_first.get_rect(center=(SCREEN_WIDTH//2 - 20, SCREEN_HEIGHT//2 + 160))

text_game = pygame.font.Font(None, 40).render("game", True, pygame.Color("white"))
text_game_rect = text_game.get_rect(center=(SCREEN_WIDTH//2 + 20, SCREEN_HEIGHT//2 + 180))

text_screen = pygame.font.Font(None, 40).render("screen.", True, pygame.Color("white"))
text_screen_rect = text_screen.get_rect(center=(SCREEN_WIDTH//2 + 60, SCREEN_HEIGHT//2 + 200))


def render_loop():

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(image_scale,image_rect)
        display_surface.blit(text_my,text_my_rect)
        display_surface.blit(text_first,text_first_rect)
        display_surface.blit(text_game,text_game_rect)
        display_surface.blit(text_screen,text_screen_rect)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    render_loop()
