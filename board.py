class Puzzle:
    def __init__(self, size):
        self.size = size
        self.full_board = self.create_board(self.size)
        self.nb_small_boards = self._divide_board()

    @staticmethod
    def create_board(size):
        board = []
        for i in range(0, size):
            row = [0] * size
            board.append(row)
        return board

    def print_board(self):
        for row in self.full_board:
            print(row)

    def _divide_board(self):
        return int((self.size / 5) ** 2)

    def fuse_boards(self, small_board, pos_on_full_board):
        inter_row, inter_col = self._get_interval(pos_on_full_board)
        for i, row in enumerate(self.full_board[inter_row:inter_row + 5]):
            for j, col in enumerate(row[inter_col:inter_col + 5]):
                self.full_board[j + inter_col][i + inter_row] = small_board[j][i]

    @staticmethod
    def pos_on_small_board(pos_on_full_board):
        row = pos_on_full_board[0]
        col = pos_on_full_board[1]
        while col >= 5 or row >= 5:
            if col >= 5:
                col -= 5
            if row >= 5:
                row -= 5

        return row, col

    @staticmethod
    def _get_interval(pos):
        inter_col = int(pos[0] / 5) * 5
        inter_row = int(pos[1] / 5) * 5

        return inter_row, inter_col


