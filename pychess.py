import numpy as np

board = np.array([
    ['♜','♞','♝','♛','♚','♝','♞','♜'],
    ['♟','♟','♟','♟','♟','♟','♟','♟',],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['♙','♙','♙','♙','♙','♙','♙','♙'],
    ['♖','♘','♗','♕','♔','♗','♘','♖'],
])

def display_board ():
  print('┌──────────────────────────┐')
  c = 0
  for i in range(len(board)):
    print('│ ', end='')
    for j in range(len(board[i])):
        color = '\033[30m\033[47m' if c % 2 == 0 else '\033[37m\033[40m'
        print(color + ' ', end='')
        char = board[i][j] if board[i][j] else ' '
        print(char, end='')
        print(' \033[0m', end='')
        c += 1
    c += 1
    print(' │')
  print('└──────────────────────────┘')

display_board()