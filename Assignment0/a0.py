#!/usr/bin/env python
import sys,time,itertools


# Count # of pieces in given row
def count_on_row(board, row):
    return sum(board[row])


# Count # of pieces in given column
def count_on_col(board, col):
    return sum([row[col] for row in board])


# Count total # of pieces on board
def count_pieces(board):
    return sum([sum(row) for row in board])


# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    new_board = ""
    for i in range(0, N):
        for j in range(0, N):
            if board[i][j] == 1:
                new_board += char1 + " "
            elif rowx > 0 and colx > 0 and i == rowx - 1 and j == colx - 1:
                new_board += "X "
            else:
                new_board += "_ "
        new_board += "\n"
    return new_board


# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1, ] + board[row][col + 1:]] + board[row + 1:]


# check if board is a goal state
def is_goal_of_n_queen(board):
    return count_pieces(board) == N and \
           all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
           all([count_on_col(board, c) <= 1 for c in range(0, N)]) and \
           check_board_for_diagonal(board)


# check if board is a goal state
def is_goal_of_n_rook(board):
    return count_pieces(board) == N and \
           all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
           all([count_on_col(board, c) <= 1 for c in range(0, N)])


def check_board_for_diagonal(board):
    elements_list = [(i, j) for i, x in enumerate(board) for j, y in enumerate(x) if y == 1]
    for x, y in itertools.combinations(elements_list, 2):
        if abs(y[1] - x[1]) == abs(y[0] - x[0]):
            return False
    return True


# Solve n-rooks!
def solve_n_rook_using_DFS(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors(fringe.pop()):
            if is_goal_of_n_rook(s):
                return (s)
            fringe.append(s)
    return False


# solve n-rooks
def solve_n_rook_using_BFS(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors(fringe.pop(0)):
            if is_goal_of_n_rook(s):
                return (s)
            fringe.append(s)
    return False


# Solve n-queens
def solve_n_queens_using_DFS(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors_queen(fringe.pop()):
            if is_goal_of_n_queen(s):
                return (s)
            if count_pieces(s) != N:
                fringe.append(s)
    return False


# Get list of successors of given board for n-rooks
def successors(board):
    row = 0
    col = []
    new_board = []
    for i in range(0, N):
        if count_on_row(board, i) == 0:
            row = i
            break
    for i in range(0, N):
        if count_on_col(board, i) == 0:
            col.append(i)
    if rowx != 0 and colx != 0:
        if row == rowx - 1 and colx - 1 in col:
            col.remove(colx - 1)
    col.reverse()
    for col_number in col:
        new_board.append(add_piece(board, row, col_number))
    return new_board


# Get list of successors of given board state for n-queen
def successors_queen(board):
    row = 0
    col = []
    new_board = []
    for i in range(0, N):
        if count_on_row(board, i) == 0:
            row = i
            break
    for i in range(0, N):
        if count_on_col(board, i) == 0:
            col.append(i)
    if rowx != 0 and colx != 0:
        if row == rowx - 1 and colx - 1 in col:
            col.remove(colx - 1)
    flag= False
    for col_number in col:
        for i, j in zip(range(row-1, -1, -1), range(col_number-1, -1, -1)):
            if board[i][j]:
                flag=True
                col.remove(col_number)
                break
        if not flag:
            for i,j in zip(range(row-1, -1, -1), range(col_number+1, N, 1)):
                if board[i][j]:
                    col.remove(col_number)
                    break
    col.reverse()
    for col_number in col:
        new_board.append(add_piece(board, row, col_number))
    return new_board


# No of rooks
N = int(sys.argv[2])
initial_board = a = [[0] * N for i in range(N)]
code = sys.argv[1]
rowx = int(sys.argv[3])
colx = int(sys.argv[4])
char1 = "R" if code == "nrook" else "Q"
#print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
if code == "nrook":
    old_time = time.time()
    solution = solve_n_rook_using_DFS(initial_board)
    run_time = time.time() - old_time
elif code == "nqueen":
    old_time = time.time()
    solution = solve_n_queens_using_DFS(initial_board)
    run_time = time.time() - old_time
print (printable_board(solution) if solution else "")

