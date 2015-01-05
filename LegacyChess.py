#
# LegacyChess.py
# Description...
# 
# Jonatan H Sundqvist
# January 5 2015
#

# TODO | - 
#        - 
#
# SPEC | -
#        -



import tkinter as tk



pieces = "♔♕♖♗♘♙|♚♛♜♝♞♟" # TODO: Should pieces be objects (?)



def createBoard():
	
	'''
	Docstring goes here

	'''
	
	return ('♖♘♗♕♔♗♘♖',
			'♙♙♙♙♙♙♙♙',
			'        ',
			'        ',
			'        ',
			'        ',
			'♟♟♟♟♟♟♟♟',
			'♜♞♜♛♚♝♞♜')
	# return [[(row, col) for row in range(8)] for col in range(8)]


def renderPiece(canvas, piece, col, row, size):

	'''
	Docstring goes here

	'''

	square = canvas.create_rectangle((col*size//8, row*size//8, (col+1)*size//8, (row+1)*size//8), width=0, fill=('grey', 'white')[col%2==row%2])
	piece  = canvas.create_text((col+0.5)*size//8, (row+0.5)*size//8, text=piece, font=('Tahoma', 40), anchor=tk.CENTER)
	return square, piece


def renderBoard(canvas, board, size):
	
	'''
	Docstring goes here

	'''

	return [[renderPiece(canvas, board[row][col], col, row, size) for row in range(8)] for col in range(8)]


def moves(board, col, row):

	'''
	Docstring goes here

	'''

	piece = board[col][row]

	# TODO: Simplify with itertools
	# TODO: Extract valid move condition (eg. validMoves(board, moves))

	# TODO: Dynamic snippet plugin (from selected text?)

	king   = ((0, 1), (1, 1), (1, 0), (-1, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)) # Moves one step in any direction
	queen  = () # Moves any number of steps in any direction. Cannot move past other pieces.
	bishop = () # Can move any number of steps diagonally. Cannot move past other pieces.
	knight = () # Can move two steps in one direction and one step in the other (not diagonally). Can move past other pieces.
	rook   = () # Can move any number of steps but not diagonally. Cannot move past other pieces.
	pawn   = () # Can move one step forwards. Captures by moving forwards diagonally.

	return {
		'♖': [(c, r) for c, r in [] if within(col+c, row+r) and board[c][r] == ' '],
		'♘': [(c, r) for c, r in [] if within(col+c, row+r) and board[c][r] == ' '],
		'♗': [],
		'♕': [(c, r) for c, r in king if within(col+c, row+r) and board[c][r] == ' '],
		'♔': [],
		'♙': []
	}[piece]()


def within(col, row):

	'''
	Checks if a coordinate is within the board

	'''

	return (0 <= col < 8) and (0 <= row < 8)


def showMoves(canvas, board, col, row, moves, fill='blue'):

	'''
	Docstring goes here

	'''

	for dx, dy in moves:
		square, piece = board[col+dx][row+dy]
		canvas.itemconfig(square, fill=fill)


def attachListeners(canvas, board):

	'''
	Docstring goes here

	'''

	# TODO: Find a better way of avoiding the leeking loop variable
	makeMoves = lambda cl, rw: (m for m in [(1, 1), (1, -1), (-1, -1), (-1, 1)] if within(m[0]+cl, m[1]+rw))

	def makeListener(col, row, fill):
		moves = makeMoves(col, row)
		def listener(event):
			print('Click')
			showMoves(canvas, board, col, row, moves, fill=fill)
		return listener

	print('attachListeners')
	for ncol, column in enumerate(board):
		for nrow, (square, piece) in enumerate(column):
			canvas.tag_bind(square, '<1>', makeListener(ncol, nrow, ('blue', 'cyan')[ncol%2==nrow%2]))
			# canvas.tag_bind(square, '<Leave>', makeListener(ncol, nrow, ('grey', 'white')[ncol%2==nrow%2]))



def main():
	
	'''
	Docstring goes here

	'''

	root = tk.Tk()
	root.title('Chess')
	root.resizable(width=False, height=False)
	canvas = tk.Canvas(width=8*60, height=8*60)

	board = renderBoard(canvas, createBoard(), 8*60)
	attachListeners(canvas, board)
	canvas.pack()

	root.mainloop()


if __name__ == '__main__':
	main()