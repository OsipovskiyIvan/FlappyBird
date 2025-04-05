import sys

import pygame as pg

from config import *


def welcome_main_screen():
    p_x = int(SCREEN_WIDTH / 5)
    p_y = int((SCREEN_HEIGHT - game_image['player'].get_height()) / 2)

    msg_x = int((SCREEN_WIDTH - game_image['message'].get_width()) / 2)
    msg_y = int(SCREEN_HEIGHT * 0.13)

    bg_x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and (event.key == pg.K_ESCAPE or event.key == pg.K_UP):
                return
            else:
                display.blit(game_image['background'], (0, 0))
                display.blit(game_image['player'], (p_x, p_y))
                display.blit(game_image['message'], (msg_x, msg_y))
                display.blit(game_image['base'], (bg_x, bg_y))

                display.update()
                pg.time_clock(FPS)


def main_gameplay():
    score = 0
    p_x = int(SCREEN_WIDTH / 5)
    p_y = int(SCREEN_HEIGHT / 2)
    bg_x = 0

    n_pipe1 = get_random_pipes()
    n_pipe2 = get_random_pipes()

    up_pipe = [
        {
            'x': SCREEN_WIDTH + 200,
            'y': n_pipe1[0]['y']
        },
        {
            'x': SCREEN_WIDTH + 200,
            'y': n_pipe2[0]["y"]
        }
    ]
    low_pipe = [
        {
            'x': SCREEN_WIDTH + 200,
            'y': n_pipe1[1]['y']
        },
        {
            'x': SCREEN_WIDTH + 200,
            'y': n_pipe2[1]["y"]
        }
    ]

    pip_Vx = -4

    p_vx = -9
    p_mvx = 10
    p_accuracy = -8

    p_flap_accuracy = -8
    p_flap = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and (event.key == pg.K_ESCAPE or event.key == pg.K_UP):
                if p_y > 0:
                    p_vx = p_flap_accuracy
                    p_flap = True
                    game_audio['wind'].play()
        cr_tst = is_Colliding()
        if cr_tst:
            return


def get_random_pipes():
    pass

def is_Colliding():
    pass