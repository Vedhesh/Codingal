import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_MIN_Y = 50
ENEMY_START_MAX_Y = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

ICON_IMAGE = pygame.image.load("PYGAME\\CLASS-5+6-SPACE-INVADER\\icon.png")
pygame.display.set_icon(ICON_IMAGE)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invaders in pygame")

PLAYER_IMAGE = pygame.image.load("PYGAME\\CLASS-5+6-SPACE-INVADER\\player.png")
PLAYER_X = PLAYER_START_X
PLAYER_Y = PLAYER_START_Y
PLAYER_X_CHANGE = 0

ENEMY_IMAGES = []
ENEMY_X = []
ENEMY_Y = []
ENEMY_CHANGE_X = []
ENEMY_CHANGE_Y = []

ENEMY_COUNT = 6

for ENEMY in ENEMY_IMAGES:
    ENEMY_IMAGE = pygame.load("PYGAME\\CLASS-5+6-SPACE-INVADER\\enemy.png")
    ENEMY_IMAGES.append(ENEMY_IMAGE)
    ENEMY_RANDOM_X = random.randint(0, SCREEN_WIDTH - 64)
    ENEMY_X.append(ENEMY_RANDOM_X)
    ENEMY_Y.append(random.randint(ENEMY_START_MIN_Y, ENEMY_START_MAX_Y))

BULLET_IMAGE = pygame.image.load("PYGAME\\CLASS-5+6-SPACE-INVADER\\bullet.png")
BULLET_X = 0
BULLET_Y = 0
BULLET_CHANGE_X = 0
BULLET_CHANGE_Y = BULLET_SPEED_Y
BULLET_STATE = "READY"

SCORE_VALUE = 0
SCORE_FONT = pygame.font.Font("freesansbold.ttf", 32)
SCORE_TEXT_X = 10
SCORE_TEXT_Y = 10

GAME_OVER_FONT = pygame.font.Font("freesansbold.ttf", 64)

def SHOW_SCORE(X, Y):
    SCORE = SCORE_FONT.render("Score: " + str(SCORE_VALUE, True, (255, 255, 255)))
    SCREEN.blit(SCORE, (X, Y))

def GAME_OVER_TEXT(X, Y):
    TEXT = GAME_OVER_FONT.render("Score: " + str(SCORE_VALUE, True, (255, 255, 255)))
    SCREEN.blit(TEXT, (X, Y))

def PLAYER(X, Y):
    SCREEN.blit(PLAYER_IMAGE, (X, Y))

def ENEMY(X, Y, I):
    SCREEN.blit(ENEMY_IMAGES[I], (X, Y))

def BULLET_FIRE(X, Y):
    global BULLET_STATE
    BULLET_STATE = "FIRE"
    BULLET_OFFSET_X = 16
    BULLET_OFFSET_Y = 10
    SCREEN.blit(BULLET_IMAGE, (X + BULLET_OFFSET_X, Y + BULLET_OFFSET_Y))

def COLLISION_CHECK(ENEMY_X, ENEMY_Y, BULLET_X, BULLET_Y):
    DISTANCE = math.sqrt((ENEMY_X - BULLET_X) ** 2 + (ENEMY_Y - BULLET_Y) ** 2)
    return DISTANCE < COLLISION_DISTANCE

DONE = False
while not DONE:
    SCREEN.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True

pygame.quit()