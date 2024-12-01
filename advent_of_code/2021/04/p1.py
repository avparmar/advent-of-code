with open('inputs/p1/input.txt') as input:
  calls = list(map(int, input.readline().rstrip("\n").split(",")))

  boardsRaw = input.readlines()
  input.close()

boards = []
currBoard = []
i = 0
for line in boardsRaw:
  if i != 0:
    currBoard.append(list(map(int, line.rstrip("\n").split())))
  i+=1

  if i == 6:
    boards.append(currBoard)
    currBoard = []
    i = 0

def markAndCheckBoard(board, call):
  for i in range(5):
    for j in range(5):
      if board[i][j] == call:
        board[i][j] = -1
  for i in range(5):
    if sum(board[i]) == -5:
      return True
    if sum(list(map(lambda ls : ls[i], board))) == -5:
      return True
  return False
  
def countBoard(board):
  sum = 0
  for i in range(5):
    for j in range(5):
      if board[i][j] != -1:
        sum+=board[i][j]
  return sum

winner = False
i = 0
while winner is False:
  call = calls[i]
  i+=1

  for board in boards:
    if (markAndCheckBoard(board, call)):
      winner = True
      print(countBoard(board) * call)