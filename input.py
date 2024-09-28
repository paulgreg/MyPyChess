
pieces = '♟♜♞♝♛♚♟♜♞♝♛♚'
char_pieces = 'prnbqkprnbqk'

def input_move():
  valid = False
  while not valid:
    move = input('Enter move like Pc2c4 (r to restart or q to quit): ').lower()
    if (move == 'q'):
      exit()
    elif (move == 'r'):
      raise Exception('restart')

    valid = len(move) == 5 and move[0] in char_pieces 

  return move