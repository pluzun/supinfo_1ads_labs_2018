import json
import sys

import pygame

from pygame.locals import *


COLORS = {
    'black': (0, 0, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 197, 33)
}
PACMAN_IMAGES = {
    '00': pygame.image.load("PacMan00.png"),
    '90': pygame.image.load("PacMan90.png"),
    '180': pygame.image.load("PacMan180.png"),
    '270': pygame.image.load("PacMan270.png")
}
FPS = 30


def import_map(map_name):
    with open('{name}.json'.format(name=map_name), 'r') as file:
        file_line = file.read()

    try:
        # Try to import the json file
        return json.loads(file_line)
    except json.decoder.JSONDecodeError as error:
        # The json file is uncorrect
        print('There is an issue with your JSON file!')
        print(error)
        return {}


def draw_wall(surface, x, y):
    pygame.draw.rect(surface, COLORS['blue'], (x * 30, y * 30, 30, 30))


def draw_pacball(surface, x, y):
    pygame.draw.circle(surface,COLORS['yellow'], ((x * 30) + 15, (y * 30) + 15), 4)


def draw_pacgum(surface, x, y):
    pygame.draw.circle(surface,COLORS['yellow'], ((x * 30) + 15, (y * 30) + 15), 10)


def draw_pacman(surface, x, y, inclinaison):
    surface.blit(PACMAN_IMAGES[inclinaison], ((x * 30), (y * 30)))


def draw_map(surface, map):
    for line_nb in range(len(map)):
        for cell_nb in range(len(map[line_nb])):
            cell = map[line_nb][cell_nb]
            if cell == 9:
                draw_wall(surface, cell_nb, line_nb)
            elif cell == 2:
                draw_pacball(surface, cell_nb, line_nb)
            elif cell == 3:
                draw_pacgum(surface, cell_nb, line_nb)


def pacman():
    pygame.init()
    surface = pygame.display.set_mode((840, 840))
    pygame.display.set_caption('Pacman')
    surface.fill(COLORS['black'])

    fontObj = pygame.font.Font('OpenSans.ttf', 26)
    texteSurface = fontObj.render('New game', True, COLORS['black'], COLORS['blue'])
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (20, 800)
    surface.blit(texteSurface, texteRect)

    inProgress = True
    fpsClock = pygame.time.Clock()

    map = import_map('map_1')
    pacmac_position = map['pacman_position']
    while inProgress:
        draw_map(surface, map['map'])
        draw_pacman(surface, pacmac_position['x'], pacmac_position['y'], pacmac_position['inclinaison'])
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False

        pygame.display.update()
        fpsClock.tick(FPS)
    pygame.quit()


pacman()
