import config as c
import random
from math import inf as infinity

player_icon, ai_icon = 'X', 'O'

scores = {}

def ai(difficulty, icon_ai):
	global player_icon, ai_icon, scores
	is_maximizing = False
	if icon_ai == 'O':
		ai_icon = 'O'
		player_icon = 'X'
	elif icon_ai == 'X':
		ai_icon = 'X'
		player_icon = 'O'

	scores = {
		"tie": 0,
		player_icon: -10,
		ai_icon: 10
	}

	board = c.board
	move = []
	
	if difficulty == 'easy':
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					move.append([i, j])
	else:
		if difficulty == 'normal':
			depth = 1
		elif difficulty == 'hard':
			depth = 2
		elif difficulty == 'impossible':
			depth = 20
		else:
			raise NameError(f"The difficulty {difficulty} doesn't exist'! the possible difficulties are: easy, normal, hard, impossible")
		best_score = -infinity
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					board[i][j] = ai_icon
					score = minimax(board, is_maximizing, depth, -20, 20)
					board[i][j] = ''
					if score > best_score:
						best_score = score
						move = [[i, j]]
					elif score == best_score:
						move.append([i, j])
	move = random.choice(move)
	board[move[0]][move[1]] = ai_icon


def minimax(board, is_maximizing, depth, alpha, beta):
	end = c.game_ended()
	if end:
		return scores[end]
	if depth == 0:
		return 0

	if is_maximizing:
		max_eval = -infinity
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					board[i][j] = ai_icon
					evaluation = minimax(board, False, depth-1, alpha, beta)
					board[i][j] = ''
					max_eval = max(evaluation, max_eval)
					alpha = max(evaluation, alpha)
					if beta < alpha:
						break

		return max_eval

	else:
		min_eval = infinity
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					board[i][j] = player_icon
					evaluation = minimax(board, True, depth-1, alpha, beta)
					board[i][j] = ''
					min_eval = min(evaluation, min_eval)
					beta = min(evaluation, beta)
					if beta < alpha:
						break

		return min_eval
