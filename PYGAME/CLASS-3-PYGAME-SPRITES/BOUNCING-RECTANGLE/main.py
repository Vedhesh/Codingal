import pygame
import random
pygame.init()
#SPRITE
RED = pygame.Color("red")
BLUE = pygame.Color("blue")
GREEN = pygame.Color("green")
#BACKGROUND
PURPLE = pygame.Color("purple")
MAGENTA = pygame.Color("magenta")
YELLOW = pygame.Color("yellow")

COLOR_CHANGED = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGED = pygame.USEREVENT + 2

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        COLLISION = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            COLLISION = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            COLLISION = True
        
        if COLLISION:
            pygame.event.post(pygame.event.Event(COLOR_CHANGED))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGED))
        
    def color_changed(self):
        self.image.fill(random.choice([RED, BLUE, GREEN]))

def background_color_changed():
    global BACKGROUND_COLOR
    BACKGROUND_COLOR = random.choice([PURPLE, MAGENTA, YELLOW])

SPRITE_GROUP = pygame.sprite.Group()
SPRITE = Sprite(RED, 20, 30)

SPRITE.rect.x = random.randint(0, 480)
SPRITE.rect.y = random.randint(0, 370)

SPRITE_GROUP.add(SPRITE)

SCREEN = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Bouncing Square")

BACKGROUND_COLOR = BLUE
SCREEN.fill(BACKGROUND_COLOR)

DONE = False
CLOCK = pygame.time.Clock()

while not DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True

        elif event.type == COLOR_CHANGED:
            SPRITE.color_changed()

        elif event.type == BACKGROUND_COLOR_CHANGED:
            background_color_changed()

    SPRITE_GROUP.update()
    SCREEN.fill(BACKGROUND_COLOR)
    SPRITE_GROUP.draw(SCREEN)
    
    pygame.display.flip()
    CLOCK.tick(75)

pygame.quit()