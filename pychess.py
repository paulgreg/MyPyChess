from display import display
from input import input_move
from move import execute_move
import numpy as np

initial_board = np.array([
    ['♖','♘','♗','♕','♔','♗','♘','♖'],
    ['♙','♙','♙','♙','♙','♙','♙','♙'],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['♟','♟','♟','♟','♟','♟','♟','♟',],
    ['♜','♞','♝','♛','♚','♝','♞','♜'],
])
board = initial_board.copy()

# 1. e4 e5 2. Cf3 Cf6 3. Cxe5 Cxe4 4. Df3 Cc5 5. Dxf7
# moves = ['♞b1c3', '♙d7d6']

while True:
  display(board)
  try:
    move = input_move()
    board = execute_move(board, move)
  except Exception as e:
    if (str(e) == 'restart'):
      board = initial_board.copy()
    else: 
      print(e)