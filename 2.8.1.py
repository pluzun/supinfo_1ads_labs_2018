def show_board(board):
    for line in board:
        for cell in line:
            print(cell,' ',end='')
        print('\n')


def create_board(size=3):
    return [['.'] * size for i in range(size)]


def board_is_full(board):
    for line in board:
        if "." in line:
            return False
    return True


def player_turn(board, player):
    print("Player {} turn!".format(player))
    line = int(input("choisis une ligne"))
    column = int(input("choose the column"))

    while not valid_position(board, line, column):
        line = int(input("choisis une ligne"))
        column = int(input("choose the column"))

    board[line][column] = player


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
    return board[line][column] == '.'


def choose_first_player():
    return 'x'


board = create_board()
playing_player = choose_first_player()

while not board_is_full(board):
    show_board(board)
    player_turn(board, playing_player)
    if check_win(board, playing_player):
        print("Player {} win!".format(playing_player))
        break

    playing_player = 'o' if playing_player == 'x' else 'x'

else:
    print('Equality!')

show_board(board)
