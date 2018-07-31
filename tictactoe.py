import replit

def printMatrix(matrix):
	for rowNum in range(len(matrix)):
		rowString = ''
		for colNum in range(len(matrix[rowNum])):
			rowString = rowString + str(matrix[rowNum][colNum]) + '  '
		print rowString
		

def play():
	replit.clear()
	blankBoard = [['-','-','-'],['-','-','-'],['-','-','-']]
	players = ['X','O']
	player = 0
	win = False
	tie = False
	printMatrix(blankBoard)
	while not win and not tie:
			print(players[player] + ' turn')
			row = getValidInput('Row 1, 2 or 3? ','Invalid row. Row 1, 2 or 3? ')
			column = getValidInput('Column 1, 2 or 3? ','Invalid column. Column 1, 2 or 3? ')
			if blankBoard[(row-1)][(column-1)] == '-':
				blankBoard[(row-1)][(column-1)] = players[player]
				player = not player
			elif blankBoard[(row-1)][(column-1)] != '-':
				print('Spot already taken')
			replit.clear()
			printMatrix(blankBoard)
			win = checkWin(blankBoard)
			tie = checkTie(blankBoard)
	if win == True:
		print players[not player] + ' wins!'
	elif tie == True:
		print('Tie game')

def checkWin(blankBoard):
	win = False
	for item in blankBoard:
		if item[0] == item[1] and item[1] == item[2] and item[1] != '-':
			win = True
	for i in range(0,3):
		if blankBoard[0][i]==blankBoard[1][i] and blankBoard[1][i] == blankBoard[2][i] and blankBoard[1][i] != '-':
			win = True
	if blankBoard[0][0]==blankBoard[1][1] and blankBoard[1][1]== blankBoard[2][2] and blankBoard[1][1] != '-':
		win = True
	if blankBoard[0][2]==blankBoard[1][1] and blankBoard[1][1]== blankBoard[2][0] and blankBoard[1][1] != '-':
		win = True
	return win

def checkTie(blankBoard):
	for item in blankBoard:
		for space in item:
			if space == '-':
			  return False
	return True

def getValidInput(msg, errormsg):
  notValid = True;
  while notValid:
    newInput = raw_input(msg);
    try: 
        newInput = int(newInput)
    except ValueError:
        newInput = 0
    if newInput <= 3 and newInput >=  1:
      notValid = False;
    msg = errormsg;
  return newInput;
  
play();
	
	
