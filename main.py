from board import Puzzle
from solver import Solver
from gui import *


if __name__ == '__main__':
    puzzle = Puzzle(15)
    solver = Solver(puzzle)
    solver.solve_full_board()
    solver.puzzle.print_board()
    print(f'\nPuzzle solved in {solver.steps - solver.counter} iterations.')

    root = Tk()
    app = Interface(solver.puzzle.full_board, master=root)
    app.mainloop()
    root.destroy()


