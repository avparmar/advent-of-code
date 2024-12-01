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
  if len(board[0]) == 6:
    return False
  for i in range(5):
    for j in range(5):
      if board[i][j] == call:
        board[i][j] = -1
  winner = False
  for i in range(5):
    if sum(board[i]) == -5:
      winner = True
    if sum(list(map(lambda ls : ls[i], board))) == -5:
      winner = True
  if winner == True:
    board[0].append(0)
  return winner
  
def countBoard(board):
  sum = 0
  for i in range(5):
    for j in range(5):
      if board[i][j] != -1:
        sum+=board[i][j]
  return sum

lastWinner = (0,0, [])
count = 1
for index, call in enumerate(calls):
  for board in boards:
    if (markAndCheckBoard(board, call)):
      count+=1
      lastWinner = (countBoard(board), call, board)

print(lastWinner[0] * lastWinner[1])