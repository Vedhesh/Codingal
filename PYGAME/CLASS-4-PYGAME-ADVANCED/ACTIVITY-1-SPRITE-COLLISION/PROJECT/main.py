import pygame
import random
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
MOVEMENT_SPEED = 5
COLOR_CHANGED = pygame.USEREVENT + 1
RED = pygame.Color("red")
BLUE = pygame.Color("blue")
GREEN = pygame.Color("green")
PURPLE = pygame.Color("purple")
MAGENTA = pygame.Color("magenta")
YELLOW = pygame.Color("yellow")
class Sprite(pygame.sprite.Sprite):
    def __init__(self, COLOR, WIDTH, HEIGHT):
        super().__init__()
        self.image = pygame.Surface([WIDTH, HEIGHT])
        pygame.draw.rect(self.image, COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
    def move(self, X_CHANGE, Y_CHANGE):
        self.rect.x = max(min(self.rect.x + X_CHANGE, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + Y_CHANGE, SCREEN_HEIGHT - self.rect.height), 0)
    def color_changed(self):
        self.image.fill(random.choice([RED, BLUE, GREEN, YELLOW, PURPLE, MAGENTA]))

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Inverted Elements")
SPRITES = pygame.sprite.Group()

SPRITE1 = Sprite(pygame.Color("blue"), 30, 20)
SPRITE1.rect.x = random.randint(0, SCREEN_WIDTH - SPRITE1.rect.width)
SPRITE1.rect.y = random.randint(0, SCREEN_HEIGHT - SPRITE1.rect.height)

SPRITE2 = Sprite(pygame.Color("red"), 30, 20)
SPRITE2.rect.x = random.randint(0, SCREEN_WIDTH - SPRITE2.rect.width)
SPRITE2.rect.y = random.randint(0, SCREEN_HEIGHT - SPRITE2.rect.height)

SPRITES.add(SPRITE1)
SPRITES.add(SPRITE2)

DONE, WON = False, False
CLOCK = pygame.time.Clock()

while not DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            DONE = True
        elif event.type == COLOR_CHANGED:
            SPRITE1.color_changed()
            SPRITE2.color_changed()

    KEYS = pygame.key.get_pressed()
    X_CHANGE = (KEYS[pygame.K_RIGHT] - KEYS[pygame.K_LEFT]) * MOVEMENT_SPEED
    Y_CHANGE = (KEYS[pygame.K_DOWN] - KEYS[pygame.K_UP]) * MOVEMENT_SPEED
    SPRITE1.move(X_CHANGE, Y_CHANGE)
    X2_CHANGE = (KEYS[pygame.K_LEFT] - KEYS[pygame.K_RIGHT]) * MOVEMENT_SPEED
    Y2_CHANGE = (KEYS[pygame.K_UP] - KEYS[pygame.K_DOWN]) * MOVEMENT_SPEED
    SPRITE2.move(X2_CHANGE, Y2_CHANGE)
    SCREEN.fill(pygame.Color("white"))
    SPRITES.draw(SCREEN)
    if SPRITE1.rect.colliderect(SPRITE2.rect):
        WON = True
        pygame.event.post(pygame.event.Event(COLOR_CHANGED))

    pygame.display.flip()
    CLOCK.tick(75)

pygame.quit()

