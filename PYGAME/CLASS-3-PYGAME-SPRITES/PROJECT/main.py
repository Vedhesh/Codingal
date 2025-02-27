import pygame
import math
def main():
    pygame.init()
    screen_width,screen_height = 600,600
    surface = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Mirror Test | FPS Benchmark")
    current_color2 = pygame.Color("black")
    current_color = pygame.Color("grey")
    x,y = 270,200
    x2,y2 = 270,340
    spos = (0,300)
    epos = (600,300)
    sprite_width,sprite_height = 60,60
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x-=3
            x2-=3
        if pressed[pygame.K_RIGHT]: 
            x+=3
            x2+=3
        if pressed[pygame.K_UP]:
            y-=3
            y2+=3
        if pressed[pygame.K_DOWN]: 
            y+=3
            y2-=3

        x = min(max(0, x),screen_width - sprite_width)
        y = min(max(0, y),screen_height//2 - sprite_height)
        x2 = min(max(0, x2),screen_width - sprite_width)
        y2 = min(max(screen_height//2, y2),screen_height - sprite_height)

        surface.fill((255,255,255))
        fps = clock.get_fps()
        fps2 = math.floor(fps)
        text = pygame.font.Font("PYGAME\CLASS-3-PYGAME-SPRITES\PROJECT\Menlo-Regular.ttf", 20).render(f"Mirror {fps2}FPS", True, pygame.Color("black"))
        text_rect = text.get_rect(center=(600//2-200, 600//2 + 20))
        
        pygame.draw.rect(surface, current_color2, (x, y, sprite_width, sprite_height))
        pygame.draw.rect(surface, current_color, (x2, y2, sprite_width, sprite_height))
        pygame.draw.line(surface, current_color2, spos, epos, 2)
        surface.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(120)
    
    pygame.quit()

if __name__ == "__main__":
    main()