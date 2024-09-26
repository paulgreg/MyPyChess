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

WHITE_ON_BLACK = '\033[30m\033[47m'
BLACK_ON_WHITE = '\033[37m\033[40m'
RESET_COLOR = '\033[0m'

def display_board() -> None:
  print('┌──────────────────────────┐') 
  c = 0
  for i, row in enumerate(board):
    print('│ ', end='')
    for j, piece in enumerate(row):
        color = WHITE_ON_BLACK if c % 2 == 0 else BLACK_ON_WHITE
        char = piece if piece else ' '
        print(f'{color} {char} {RESET_COLOR}', end='')
        c += 1
    c += 1
    print(' │')
  print('└──────────────────────────┘')

display_board()

