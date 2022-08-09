import minimax
import config
import pygame
import sys
import argparse



############################
# Variables inizialization #
############################

# Parser
parser = argparse.ArgumentParser(description='TicTacToe Game')

parser.add_argument('player_1', type=str,
                    help='Specify who the first player will be\nCan be: player, ai-easy, ai-normal, ai-difficult, ai-impossible')
parser.add_argument('player_2', type=str,
                    help='Specify who the second player will be\nCan be: player, ai-easy, ai-normal, ai-diffucult, ai-impossible')

args = parser.parse_args()

players_type = ['', '']
# First player
if args.player_1 == 'player':
	players_type[0] = 'player'
else:
	players_type[0] = args.player_1.split('-')[1]

# Second player
if args.player_2 == 'player':
	players_type[1] = 'player'
else:
	players_type[1] = args.player_2.split('-')[1]

# Pygame variables

pygame.init()
turn_of_player = 0

END_FONT = pygame.font.SysFont('ubuntu', 50)
END_COLOR = pygame.Color('#ffffff')

BKG_COLOR = pygame.Color('#14bdac')
GRID_COLOR = pygame.Color('#0da192')
AI_COLOR = pygame.Color('#f2ebd3')
PLAYER_COLOR = pygame.Color('#545454')

GRID_THICK = 10
PLAYER_THICK = 30
AI_THICK = 20

PLAYER_OFF = 50
AI_OFF = 40

row, column = 0, 0

players = ['X', 'O']

window_w, window_h = 1000, 600 # Window sizes
w, h = 600, 600 # Grid sizes
screen = pygame.display.set_mode((window_w, window_h))

#############
# Functions #
#############

win_message = ''

def end_game():
	global win_message, END_COLOR
	end = config.game_ended()
	if end:
		if end == 'tie':
			win_message = "Pareggio!"
		else:
			win_message = end + " ha vinto!"
			if end == 'X':
				END_COLOR = PLAYER_COLOR
			else:
				END_COLOR = AI_COLOR


def player_move(row, col, play_index):
	curr_player = players[play_index]

	config.board[col][row] = curr_player
	end_game()

def ai_move(play_index):
	curr_player = players[play_index]

	print(players_type[play_index], curr_player)
	minimax.ai(players_type[play_index], curr_player)
	end_game()



def draw_grid():
	for i in range(1, 4):
		# Vertical Lines
		pygame.draw.line(screen, GRID_COLOR, (w/3*i, 0), (w/3*i, h), GRID_THICK)

		# Horizontal Lines
		pygame.draw.line(screen, GRID_COLOR, (0, h/3*i), (w, h/3*i), GRID_THICK)

def draw_player(row, col):
	pygame.draw.line(screen, PLAYER_COLOR, (w/3*col+PLAYER_OFF, h/3*row+PLAYER_OFF), (w/3*(col+1)-PLAYER_OFF, h/3*(row+1)-PLAYER_OFF), PLAYER_THICK)
	pygame.draw.line(screen, PLAYER_COLOR, (w/3*(col+1)-PLAYER_OFF, h/3*row+PLAYER_OFF), (w/3*col+PLAYER_OFF, h/3*(row+1)-PLAYER_OFF), PLAYER_THICK)

def draw_ai(row, col):
	pygame.draw.circle(screen, AI_COLOR, (w/3*col+w/6, h/3*row+h/6), w/6-AI_OFF, AI_THICK)

###################
# Pygame Mainloop #
###################

def mainloop():
	global turn_of_player, row, column
	player_ready = False

	while True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				return True
			elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
				if not win_message:
					mouse_x, mouse_y = pygame.mouse.get_pos()
					row = (mouse_x // (w//3))
					column = (mouse_y // (h//3))
					if config.board[column][row] == '':
						player_ready = True




			

		# Drawing on screen

		screen.fill(BKG_COLOR)
		draw_grid()

		for i in range(3):
			for j in range(3):
				if config.board[i][j] == 'O':
					draw_ai(i, j)
				elif config.board[i][j] == 'X':
					draw_player(i, j)

		if win_message:
			end_render = END_FONT.render(win_message, True, END_COLOR)
			screen.blit(end_render, (w+(window_w-w)/2-end_render.get_width()/2, h/2-end_render.get_height()/2))


		# Moves
		if not win_message:
			if turn_of_player == 0:
				if players_type[0] == 'player':
					if player_ready:
						player_move(row, column, 0)
						player_ready = False
						turn_of_player = int(not turn_of_player)
				else:
					ai_move(0)
					turn_of_player = int(not turn_of_player)
			else:
				if players_type[1] == 'player':
					if player_ready:
						player_move(row, column, 1)
						player_ready = False
						turn_of_player = int(not turn_of_player)
				else:
					ai_move(1)
					turn_of_player = int(not turn_of_player)



		pygame.display.flip()


if mainloop():
	pygame.quit()
