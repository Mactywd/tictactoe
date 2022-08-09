board = [
	["", "", ""],
	["", "", ""],
	["", "", ""]
]

def update_board(positions, player):
	board[positions[0]][positions[1]] = player

def game_ended():
	winner = None
	result = ''

	if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != '':
		result = board[0][0]
	elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != '':
		result = board[1][1]

	else:
		for i in range(3):
			if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != '':
				result = board[i][0]
				break
			if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != '':
				result = board[0][i]
				break
		else:
			for i in range(3):
				for j in range(3):
					if board[i][j] == '':
						break
				else:
					continue
				break
			else:
				result = 'tie'

	if result:
		return result