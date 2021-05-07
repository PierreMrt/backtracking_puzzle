from tkinter import *
import time


class Interface(Frame):
    def __init__(self, board, master=None):
        Frame.__init__(self, master)
        self.board = board
        self.config(bg='black')
        self.pack()

        self._create_board()
        self._walkthrough()

    def _create_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                label = Label(self, text=self.board[i][j], justify='center', width=4, bg='white', fg='white')
                label.grid(row=i, column=j, padx=1, pady=1, ipady=9, ipadx=4)

    def _walkthrough(self):
        for i in range(1, len(self.board) ** 2 + 1):
            for r in range(len(self.board)):
                for c in range(len(self.board)):
                    if self.board[r][c] == i:
                        label = self.grid_slaves(r, c)[0]
                        label.config(bg='green')
                        time.sleep(0.1)
                        self.update()
