import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
BG_COLOR = pygame.Color('grey12')
FG_COLOR = (200, 200, 200)

BALL = pygame.Rect(
    SCREEN_WIDTH/2 - 15,
    SCREEN_HEIGHT/2 - 15,
    30, 30)

BALL_SPEED_X = 7
BALL_SPEED_Y = 7

P1 = pygame.Rect(
    SCREEN_WIDTH - 20,
    SCREEN_HEIGHT/2 - 70,
    10, 140)
P2 = pygame.Rect(
    10,
    SCREEN_HEIGHT/2 - 70,
    10, 140)
