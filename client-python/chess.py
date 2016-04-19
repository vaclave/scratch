import random

##########################################################

chess_board = [] 
plyNumber = 1

def get_intDepth():
	global plyNumber

	intDepth = 0
	intDepth = (plyNumber / 2) + (plyNumber % 2)
	return intDepth

def get_strNext():
	global plyNumber

	strNext = ''
	if (plyNumber % 2 == 0):
		strNext = 'B'
	else:
		strNext = 'W'
	return strNext

def set_plyNumber(intDepth, strNext):
	global plyNumber

	if (strNext == 'W'):
		plyNumber = (intDepth * 2) - 1
	else:
		plyNumber = intDepth * 2

	return plyNumber 

def chess_reset():
	global chess_board
	global plyNumber

	plyNumber = 1
	intDepth = 1
	strNext = 'W'	

	chess_board = []
	chess_board.append('kqbnr')
	chess_board.append('ppppp')
	chess_board.append('.....')
	chess_board.append('.....')
	chess_board.append('PPPPP')
	chess_board.append('RNBQK')

	return

def chess_boardGet():
	global chess_board

	intDepth = get_intDepth()
	strNext = get_strNext()

	strOut = ''
	strOut += str(intDepth) + ' ' + strNext + '\n'
	strOut += chess_board[0] + '\n'
	strOut += chess_board[1] + '\n'
	strOut += chess_board[2] + '\n'
	strOut += chess_board[3] + '\n'
	strOut += chess_board[4] + '\n'
	strOut += chess_board[5] + '\n'

	return strOut

def chess_boardSet(strIn):
	global chess_board
	global plyNumber

	strIn = strIn.split('\n')

	intDepth = int(strIn[0].split(" ")[0])
	strNext = strIn[0].split(" ")[1]	
	set_plyNumber(intDepth, strNext)
	
	chess_board = []
	chess_board.append(strIn[1])
	chess_board.append(strIn[2])
	chess_board.append(strIn[3])
	chess_board.append(strIn[4])
	chess_board.append(strIn[5])
	chess_board.append(strIn[6])

	return

def chess_winner():
	# determine the winner of the current state of the game and return '?' or '=' or 'W' or 'B' - note that we are returning a character and not a string
	global chess_board
	global plyNumber

	# Considered false until king found within board.
	white_has_king = False
	black_has_king = False

	for row in chess_board:
		if 'K' in row:
			white_has_king = True
		elif 'k' in row:
			black_has_king = True	

	if (plyNumber >= 80):
		return '='

	if (black_has_king == False):
		return 'W'
	elif (white_has_king == False):
		return 'B'

	return '?'

def chess_isValid(intX, intY):
	if intX < 0:
		return False
		
	elif intX > 4:
		return False
	
	if intY < 0:
		return False
		
	elif intY > 5:
		return False
	
	return True


def chess_isEnemy(strPiece):
	# with reference to the state of the game, return whether the provided argument is a piece from the side not on move - note that we could but should not use the other is() functions in here but probably
	global plyNumber
	
	strNext = get_strNext()
	white_pieces = ['K', 'Q', 'B', 'N', 'R', 'P']
	black_pieces = ['k', 'q', 'b', 'n', 'r', 'p']
	
	if (strPiece == '.'):
		return False
	if (strNext == 'W'):
		for piece in black_pieces:
			if (strPiece == piece):
				return True
	elif (strNext == 'B'):
		for piece in white_pieces:
			if (strPiece == piece):
				return True
	return False

def chess_isOwn(strPiece):
	# with reference to the state of the game, return whether the provided argument is a piece from the side on move - note that we could but should not use the other is() functions in here but probably
	global plyNumber

        strNext = get_strNext()
        white_pieces = ['K', 'Q', 'B', 'N', 'R', 'P']
        black_pieces = ['k', 'q', 'b', 'n', 'r', 'p']

        if (strPiece == '.'):
                return False
        if (strNext == 'W'):
                for piece in white_pieces:
                        if (strPiece == piece):
                                return True
        elif (strNext == 'B'):
                for piece in black_pieces:
                        if (strPiece == piece):
                                return True
	return False

def chess_isNothing(strPiece):
	# return whether the provided argument is not a piece / is an empty field - note that we could but should not use the other is() functions in here but probably
	
	if (strPiece == '.'):
		return True
	else:	
		return False

def chess_eval():
	# with reference to the state of the game, return the the evaluation score of the side on move - note that positive means an advantage while negative means a disadvantage

	score = 0
	king_pts = 100
	queen_pts = 9
	rook_pts = 5
	bishop_pts = 3
	knight_pts = 3
	pawn_pts = 1
	
	for i in range (0, 6):
		for j in range(0, 5):
			cur_piece = chess_board[i][j]
			if (chess_isOwn(cur_piece)):
				if (cur_piece == 'k' or cur_piece =='K'):
					score += king_pts		
				elif (cur_piece == 'q' or cur_piece =='Q'):
					score += queen_pts
				elif (cur_piece == 'r' or cur_piece =='R'):
					score += rook_pts
				elif (cur_piece == 'b' or cur_piece =='B'):
					score += bishop_pts
				elif (cur_piece == 'k' or cur_piece =='K'):
					score += knight_pts
				elif (cur_piece == 'p' or cur_piece =='P'):
					score += pawn_pts
				else:
					continue

			else:
				if (cur_piece == 'k' or cur_piece =='K'):               
                                        score -= king_pts
                                elif (cur_piece == 'q' or cur_piece =='Q'):
                                        score -= queen_pts
                                elif (cur_piece == 'r' or cur_piece =='R'):
                                        score -= rook_pts
                                elif (cur_piece == 'b' or cur_piece =='B'):
                                        score -= bishop_pts
                                elif (cur_piece == 'k' or cur_piece =='K'):
                                        score -= knight_pts
                                elif (cur_piece == 'p' or cur_piece =='P'):
                                        score -= pawn_pts
                                else:
                                        continue
	return score

def chess_moves():
	# with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters
	global chess_board
	strOut = []
	
#	strOut.append('a2-a3\n')
#	strOut.append('b2-b3\n')
#	strOut.append('c2-c3\n')
#	strOut.append('d2-d3\n')
#	strOut.append('e2-e3\n')
#	strOut.append('b1-a3\n')
#	strOut.append('b1-c3\n')


		
	return strOut


def chess_movesShuffled():
	# with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here
	
	return []


def chess_movesEvaluated():
	# with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_movesShuffled() function in here
	
	return []

def get_value_int(value):

	# Strings need to be converted from unicode to int
	value = value.lower()	
	
	if (value == 'a' or value == '1'):
		value = 1
	elif (value == 'b' or value == '2'):
		value = 2
	elif (value == 'c' or value == '3'):
		value = 3
	elif (value == 'd' or value == '4'):
		value = 4
	elif (value == 'e' or value == '5'):
		value = 5
	elif (value == '6'):
		value = 6
	else:
		print("Invalid column value\n")
		return False

	return value

def chess_move(strIn):
	# perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move

	global chess_board
	
	# Get the row and column position as numerical value
	start = strIn.split("-")[0]
	finish = strIn.split("-")[1]

	start_column = get_value_int(start[0]) - 1
	finish_column = get_value_int(finish[0]) - 1

	start_row = 6 - get_value_int(start[1])
	finish_row = 6 - get_value_int(finish[1])

	# Get the value of the piece being moved
	current_piece = chess_board[start_row][start_column]
	
	# Check to ensure move is in range
	if not (chess_isValid(start_column, start_row)):
		print("Invalid Move: start out of range\n")
		return

	elif not (chess_isValid(finish_column, finish_row)):
		print("Invalid Move: finish out of range\n")
		return

	# Check to ensure piece is owned by player
	elif not (chess_isOwn(current_piece)):
		print("Invalid Move: Not your piece to move\n")
		return

	# If error checking passes, move the piece
	else:
		# Get current board setup
		old_board=chess_boardGet().split('\n')
		del old_board[0]
		print(old_board)
	
		# Update who's turn it is
		chess_board = []
		strNext = get_strNext()
		intDepth = get_intDepth()

		if (strNext == 'W'):
			strNext = 'B'
		else:
			strNext = 'W'
			intDepth += 1
		set_plyNumber(intDepth, strNext)

		# Move the piece to the correct position
		for i in range (0, 6):
			if (i == finish_row and finish_row != start_row):
				if (current_piece == 'P' and finish_row == 0):
					current_piece = 'Q'
				elif (current_piece == 'p' and finish_row == 6):
					current_piece = 'q'
				new = old_board[finish_row][:finish_column] + current_piece + old_board[finish_row][finish_column + 1:]
				chess_board.append(new)
			elif (i == start_row and start_row != finish_row):
				new = old_board[start_row][:start_column] + '.' + old_board[start_row][start_column + 1:]
				chess_board.append(new)
			elif ((i == start_row or i == finish_row) and start_row == finish_row):
				new = ''
				row = old_board[start_row]
				for i in range(0, 5):
					if i == start_column:
						new += '.'
					elif i == finish_column:
						new += current_piece
					else:
						new += row[i]
				chess_board.append(new)
			else:
				chess_board.append(old_board[i])
		return

def chess_moveRandom():
	# perform a random move and return it - one example output is given below - note that you can call the chess_movesShuffled() function as well as the chess_move() function in here
	
	return 'a2-a3\n'


def chess_moveGreedy():
	# perform a greedy move and return it - one example output is given below - note that you can call the chess_movesEvaluated() function as well as the chess_move() function in here
	
	return 'a2-a3\n'


def chess_moveNegamax(intDepth, intDuration):
	# perform a negamax move and return it - one example output is given below - note that you can call the the other functions in here
	
	return 'a2-a3\n'


def chess_moveAlphabeta(intDepth, intDuration):
	# perform a alphabeta move and return it - one example output is given below - note that you can call the the other functions in here
	
	return 'a2-a3\n'


def chess_undo():
	# undo the last move and update the state of the game / your internal variables accordingly - note that you need to maintain an internal variable that keeps track of the previous history for this
	
	pass
