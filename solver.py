from func import change_value, get_value, get_pos


class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.full_board = self.puzzle.full_board
        self.moves = [(3, 0), (-3, 0), (0, 3), (0, -3), (-2, -2), (2, -2), (2, 2), (-2, 2)]
        self.nb_board = self.puzzle.nb_small_boards

        self.steps = 0
        self.counter = 1

    def solve_full_board(self):
        pos = (1, 1)
        pos_on_full_board = (7, 7)

        for i in range(self.nb_board):
            board = self.puzzle.create_board(5)
            change_value(board, pos, self.counter)
            self._solve_small_board(board, pos)

            self.puzzle.fuse_boards(board, pos_on_full_board)
            try:
                pos, pos_on_full_board = self._next_small_board()
            except TypeError:
                pass

    def _next_small_board(self):
        pos = get_pos(self.full_board, self.counter)
        for move in self.moves:
            future_pos = (pos[0] + move[0], pos[1] + move[1])
            if self._check_moves(self.full_board, future_pos):
                self.counter += 1
                change_value(self.full_board, future_pos, self.counter)
                pos_on_full_board = future_pos
                pos = self.puzzle.pos_on_small_board(pos_on_full_board)

                return pos, pos_on_full_board

    def _solve_small_board(self, board, pos):
        if self._complete(board) and pos == (2, 2):
            return True

        self.steps += 1

        for move in self.moves:
            future_pos = (pos[0] + move[0], pos[1] + move[1])
            if self._check_moves(board, future_pos):
                self.counter += 1
                change_value(board, future_pos, self.counter)

                if self._solve_small_board(board, future_pos):
                    return True

                change_value(board, future_pos, 0)
                self.counter -= 1

        return False

    @staticmethod
    def _check_moves(board, pos):
        value = get_value(board, pos)
        if pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board) or value != 0:
            return False

        return True

    @staticmethod
    def _complete(board):
        for row in board:
            for val in row:
                if val == 0:
                    return False
        return True

