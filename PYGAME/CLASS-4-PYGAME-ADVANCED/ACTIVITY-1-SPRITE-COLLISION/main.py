import pygame
import random
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
FONT_SIZE = 70
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load("PYGAME\CLASS-4-PYGAME-ADVANCED\ACTIVITY-1-SPRITE-COLLISION\BG.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
WIN_FONT = pygame.font.SysFont("Times New Roman", FONT_SIZE)
MOVEMENT_SPEED = 5

class Sprite(pygame.sprite.Sprite):
    def __init__(self, COLOR, WIDTH, HEIGHT):
        super().__init__()
        self.image = pygame.Surface([WIDTH, HEIGHT])
        pygame.draw.rect(self.image, COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
    def move(self, X_CHANGE, Y_CHANGE):
        self.rect.x = max(min(self.rect.x + X_CHANGE, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + Y_CHANGE, SCREEN_HEIGHT - self.rect.height), 0)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Touch the coin!")
SPRITES = pygame.sprite.Group()

SPRITE1 = Sprite(pygame.Color("black"), 30, 20)
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

    if not WON:
        KEYS = pygame.key.get_pressed()
        X_CHANGE = (KEYS[pygame.K_RIGHT] - KEYS[pygame.K_LEFT]) * MOVEMENT_SPEED
        Y_CHANGE = (KEYS[pygame.K_DOWN] - KEYS[pygame.K_UP]) * MOVEMENT_SPEED
        SPRITE1.move(X_CHANGE, Y_CHANGE)
        
        if SPRITE1.rect.colliderect(SPRITE2.rect):
            SPRITES.remove(SPRITE2)
            WON = True
        
    SCREEN.blit(BACKGROUND_IMAGE, [0,0])
    SPRITES.draw(SCREEN)

    if WON:
        WIN_TEXT = WIN_FONT.render("You Win!", True, pygame.Color("black"))
        SCREEN.blit(WIN_TEXT, ((SCREEN_WIDTH - WIN_TEXT.get_width())//2, (SCREEN_HEIGHT - WIN_TEXT.get_height())//2)  )

    pygame.display.flip()
    CLOCK.tick(90)

pygame.quit()
