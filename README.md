# GUI application to showcase backtracking

With a grid of a given dimension, the goal is to pass through each cells, only once.
You can only move 3 cells orthogonally or 2 cells diagonally.


This algorithm solves this puzzle automatically, and shows the steps taken through the graphical interface.

### How to solve this problem
This idea is to use backtracking. Meaning starting somewhere, and try each position, until it is either solved or there are no more moves possible.
When there are no more possible moves, the algorithm 'back track' to a position where it is possible to try other moves.

### Issues with the solution
A problem arise when the dimension of the grid is too big (starting from 7x7), as the number of iterations needed to solve this puzzle increase exponentially.
It indeed becomes way too long to compute and the solution is therefore impractical.

### Solution implemented
As the algorithm works well and quickly for a 5x5 grid, the idea is to divide the grid into 5x5 smaller grids. We are now able to solve even a 100x100 almost instantaneously.
The program then solve a first 5x5 grid with the added condition that it must finish in the middle of this grid, so as to be able to move easily to other smaller grids.
When the first grid is solved, we then move to another smaller grid and continue the previous steps until full grid is solved.
