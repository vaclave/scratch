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
	
	return 0


def chess_moves():
	# with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters
	
	strOut = []
	
	strOut.append('a2-a3\n')
	strOut.append('b2-b3\n')
	strOut.append('c2-c3\n')
	strOut.append('d2-d3\n')
	strOut.append('e2-e3\n')
	strOut.append('b1-a3\n')
	strOut.append('b1-c3\n')
	
	return strOut


def chess_movesShuffled():
	# with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here
	
	return []


def chess_movesEvaluated():
	# with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_movesShuffled() function in here
	
	return []


def chess_move(strIn):
	# perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move
	
	pass


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
