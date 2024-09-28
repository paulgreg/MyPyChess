
def convert_column(letter):
    return ord(letter) - ord('a')

def convert_move(board, move):
  l = len(move)
  if l == 5: 
    # piece = move[0]
    column1 = move[1]
    row1 = move[2]
    column2 = move[3]
    row2 = move[4]
  else:
    raise Exception('only notation with 5 chars is supported')
  y1 = convert_column(column1)
  x1 = 8 - int(row1)
  y2 = convert_column(column2)
  x2 = 8 - int(row2)
  if (y1 < 0 or y1 > 7 or x1 < 0 or x1 > 7 or y2 < 0 or y2 > 7 or x2 < 0 or x2 > 7):
    raise Exception('invalid move')
  return x1,y1,x2,y2

def execute_move(board, move):
  x1,y1,x2,y2 = convert_move(board, move)
  if board[x1,y1] == '':
    raise Exception('no piece there !')
  new_board = board.copy()
  new_board[x2,y2] = new_board[x1,y1]
  new_board[x1,y1] = ''
  return new_board