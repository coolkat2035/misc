import os
board = [['.' for x in range(7)] for y in range(6)]
#len(board) number of rows
#len(board[0]) number of cols
#board[row][col]
#wow i havent touched 2d arrays for 2 years

def cls():
  if name == 'nt':#windows
    os.system('cls') 
  else:#mac and linux
    os.system('clear')

def check_ava(col:int):
  """checks if the column is ok to place in"""
  global board
  if (col < 0 or col >= len(board[0])):#outside board range
    return 1
  if board[0][col] != '.':#row is full
    return 2
  return 0#haha reference

def place(col:int, piece):
  """puts a piece at the bottom of column"""
  global board
  piece = piece.lower()
  if (piece != 'o' and piece != 'x'):
    return False
  for i in range(len(board)-1, -1, -1):
    #find backwards next free
    if board[i][col] == '.':
        board[i][col] = piece
        return True

def show_board():
  #shows the board?
  global board
  print("A B C D E F G")
  for row in range(len(board)):
    for col in board[row]:
      print(col,end=' ')
    print()

def check_win(who:str):
  """checks if a player has matched a pattern (|-/\)"""
  
  #vertical, [0][0] to [2][6]
  for row in range(len(board)-3):
    for col in range(len(board[0])):
      if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == who:
        return True
  #horizontal, [0][0] to [5][6]
  for row in range(len(board)):
    for col in range(len(board[0])-3):
      if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == who:
        return True
  #diagona/, [0][3] to [2][6]
  for row in range(len(board)-3):
    for col in range(3,len(board[0])):
      if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == who:
        return True
  #diagona\, [0][0] to [2][3]
  for row in range(len(board)-3):
    for col in range(len(board[0])-3):
      if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == who:
        return True
  return False

###############actual gameplay#########################
turn = 'x'
print("maybe add an intro screen(wip)")
#A is 65
while True:
  cls()
  show_board()
  while True:#only valid moves break the loop
    move = input(f"It is {turn.upper()}'s turn! Select a column: ").upper()#ABCDEFG
    if move not in "ABCDEFG" or len(move) != 1:
      print("That is not a valid column!")
      continue
    move = ord(move)-65#turn character into number (A => 65 => 0)
    
    if check_ava(move) == 0:
      place(move,turn)
      break
    elif check_ava(move) == 1:
      print("Not a valid column!")
      continue
    elif check_ava(move) == 2:
      print("Column is full!")
      continue
    else:
      print("You shouldn't see this message!")
      break
    
  if check_win(turn):
    cls()
    show_board()
    print(turn, "wins!")
    break

  for r in board:
    if '.' in r:
      break
  else:
    print("The board is full... I call it a tie!")
    break
    
  if turn == 'x':
    turn = 'o'
  else:
    turn = 'x'

os.system("pause")

      
