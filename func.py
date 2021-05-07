def change_value(board, pos, value):
    board[pos[0]][pos[1]] = value
    return board


def get_value(board, pos):
    try:
        return board[pos[0]][pos[1]]
    except IndexError:
        return 0


def get_pos(board, val):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == val:
                return i, j