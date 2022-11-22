import random
import sys

import pygame

from const import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pyng')


p1_speed = 0
p2_speed = 7
p1_score = 0
p2_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)


def move_p1():
    P1.y += p1_speed
    if P1.top <= 0:
        P1.top = 0
    if P1.bottom >= SCREEN_HEIGHT:
        P1.bottom = SCREEN_HEIGHT


def move_p2():
    if P2.top < BALL.y:
        P2.top += p2_speed
    if P2.bottom > BALL.y:
        P2.bottom -= p2_speed
    if P2.top <= 0:
        P2.top = 0
    if P2.bottom >= SCREEN_HEIGHT:
        P2.bottom = SCREEN_HEIGHT


def ball_restart():
    global BALL_SPEED_X, BALL_SPEED_Y
    BALL.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    BALL_SPEED_Y *= random.choice((1, -1))
    BALL_SPEED_X *= random.choice((1, -1))


def animate_ball():
    global BALL_SPEED_X, BALL_SPEED_Y, p1_score, p2_score
    BALL.x += BALL_SPEED_X
    BALL.y += BALL_SPEED_Y
    if BALL.top <= 0 or BALL.bottom >= SCREEN_HEIGHT:
        BALL_SPEED_Y *= -1
    if BALL.left <= 0:
        p1_score += 1
        ball_restart()

    if BALL.right >= SCREEN_WIDTH:
        p2_score += 1
        ball_restart()
    if BALL.colliderect(P1) or BALL.colliderect(P2):
        BALL_SPEED_X *= -1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p1_speed += 7
            if event.key == pygame.K_UP:
                p1_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                p1_speed -= 7
            if event.key == pygame.K_UP:
                p1_speed += 7

    animate_ball()
    move_p1()
    move_p2()

    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, FG_COLOR, P1)
    pygame.draw.rect(screen, FG_COLOR, P2)
    pygame.draw.ellipse(screen, FG_COLOR, BALL)
    pygame.draw.aaline(screen, FG_COLOR,
                       (SCREEN_WIDTH / 2, 0),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    p1_text = basic_font.render(f'{p1_score}', False, FG_COLOR)
    screen.blit(p1_text, (660, 470))
    p2_text = basic_font.render(f'{p2_score}', False, FG_COLOR)
    screen.blit(p2_text, (600, 470))

    pygame.display.flip()
    clock.tick(60)
