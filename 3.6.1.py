import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CASE_SIZE = 150

def show_board(surface, board):
    pygame.draw.rect(surface, BLUE, (CASE_SIZE, CASE_SIZE, 3 * CASE_SIZE, 3 * CASE_SIZE))
    for i in range(2, 4):
        pygame.draw.line(surface, BLACK, (CASE_SIZE * i, CASE_SIZE), (CASE_SIZE * i, CASE_SIZE * 4))
    for i in range(2, 4):
        pygame.draw.line(surface, BLACK, (CASE_SIZE, CASE_SIZE * i), (CASE_SIZE * 4, CASE_SIZE * i))

    for x, line in enumerate(board):
        for y, cell in enumerate(line):
            if cell == 1:
                pygame.draw.line(surface, BLACK, ((x + 1) * CASE_SIZE + 20, (y + 1) * CASE_SIZE + 20), ((x + 2) * CASE_SIZE - 20, (y + 2) * CASE_SIZE - 20), 1)
                pygame.draw.line(surface, BLACK, ((x + 2) * CASE_SIZE - 20, (y + 1) * CASE_SIZE + 20), ((x + 1) * CASE_SIZE + 20, (y + 2) * CASE_SIZE - 20), 1)

            if cell == 2:
                pygame.draw.circle(surface, BLACK, ((x + 1) * CASE_SIZE + CASE_SIZE // 2, (y + 1) * CASE_SIZE + CASE_SIZE // 2), (CASE_SIZE - 30) // 2, 1)



def create_board(size=3):
    return [[0] * size for i in range(size)]


def board_is_full(board):
    for line in board:
        if 0 in line:
            return False
    return True


def check_win(board, player):
    # Check lines
    for line in board:
        if line.count(player) == len(line):
            return True

    # Check columns
    for column in range(len(board)):
        for line in board:
            if line[column] != player:
                break
        else:
            return True

    # Check diags
    for i in range(len(board)):
        if board[i][i] != player:
            break
    else:
        return True

    for i in range(len(board)):
        if board[i][len(board) - 1 - i] != player:
            break
    else:
        return True

    return False


def valid_position(board, line, column):
    return board[line][column] == 0


def choose_first_player():
    return 1

def select_case(board, pos):
    return pos[0] // CASE_SIZE - 1, pos[1] // CASE_SIZE - 1

def start():
    pygame.init()
    surface = pygame.display.set_mode((750, 750))
    pygame.display.set_caption('Morpion')
    surface.fill(BLACK)

    fontObj = pygame.font.Font('OpenSans.ttf', 26)
    texteSurface = fontObj.render('New game', True, BLACK, BLUE)
    texteRect = texteSurface.get_rect()
    texteRect.topright = (730, 20)
    surface.blit(texteSurface,texteRect)

    inProgress = True
    board = create_board()
    player_turn = choose_first_player()
    finished = False
    while inProgress:
        show_board(surface, board)
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            if event.type == MOUSEBUTTONUP:
                x, y = select_case(board, event.pos)
                if 0 <= x <= 2 and 0 <= y <= 2 and valid_position(board, x, y) and not finished:
                    board[x][y] = player_turn
                    if check_win(board, player_turn):
                        finished = True
                        winText = fontObj.render('Player {0} won !'.format(player_turn), True, BLACK, BLUE)
                        winRect = winText.get_rect()
                        winRect.topleft = (20, 20)
                        surface.blit(winText,winRect)
                    player_turn = 2 if player_turn == 1 else 1

                    if board_is_full(board) and not finished:
                        finished = True
                        drawText = fontObj.render('Draw !', True, BLACK, BLUE)
                        drawRect = drawText.get_rect()
                        drawRect.topleft = (20, 20)
                        surface.blit(drawText,drawRect)

                if texteRect.collidepoint(event.pos):
                    finished = False
                    player_turn = choose_first_player()
                    board = create_board()
                    pygame.draw.rect(surface, BLACK, (0, 0, 300, 100))

        pygame.display.update()
    pygame.quit()

start()
