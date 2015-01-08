#
# Piece.py
# Description...
# 
# Jonatan H Sundqvist
# January 5 2015
#

# TODO | - Use Enums (?)
#        - 
#
# SPEC | -
#        -




import tkinter as tk
from itertools import takewhile, chain

from SwiftUtils.MultiSwitch import MultiSwitch



class Piece(object):

	'''
	Docstring goes here

	'''

	# TODO: Simplify treatment of colours (black/white)
	white  = set('♔♕♖♗♘♙')
	black  = set('♚♛♜♝♞♟')
	pieces = white | black

	names = MultiSwitch({'♖♜': 'rook',
			 			 '♘♞': 'knight',
			 			 '♗♝': 'bishop',
			 			 '♕♛': 'king',
			 			 '♔♚': 'queen',
			 			 '♙♟': 'pawn'})


	def __init__(self, piece, **styles):

		'''
		Docstring goes here

		'''

		assert piece in Piece.pieces, 'Invalid piece: {0}'.format(piece) # TODO: Extract valid piece logic

		self.styles = {
			'font': ('Tahoma', 40)
		}

		self.styles.update(styles)

		self.piece = piece
		self.colour = 'black' if piece in Piece.black else 'white'
		self.name = Piece.names[piece] # TODO: Simplify treatment of colours (black/white)
		self.id = None # Canvas item ID


	def render(self, canvas, size, col, row):
		
		'''
		Docstring goes here

		'''

		# TODO: Render and update, cache IDs
		self.id = canvas.create_text(int((col+0.5)*size), int((row+0.5)*size), text=self.piece, anchor=tk.CENTER, **self.styles)


	def moves(self, board, x, y):

		'''
		Retrieves a list of valid moves for this piece, given a board and a position.

		'''

		# TODO: Optimise, cache, lazy evaluation (create the switch only once)
		# TODO: Simplify with itertools, generators
		# TODO: Prevent NoneType errors (square.piece is None if square is empty) (find a better way to represent empty squares?)

		# TODO: Pre-calculate maximum range based on position (eg. maximum dx = 8-x) (?)

		within = board.within
		isEmpty = lambda cl, rw: board.board[cl][rw].piece == None
		hasEnemy = lambda cl, rw: within(cl,rw) and not isEmpty(cl, rw) and board.board[cl][rw].piece.colour != self.colour
		valid = lambda cl, rw: within(cl, rw) and (hasEnemy(cl, rw) or isEmpty(cl, rw))

		def accessible(previous):
			# Creates a function which determines if a particular square is accessible
			# Previous is a function which returns the previous square in a series of moves
			def predicate(m):
				return valid(*m) and (previous(*m).piece in (None, self)) # TODO: Add prev argument (?)
			return predicate

		

		dyPawn = (-1, 1)[self.colour=='white']

		return MultiSwitch({
			# Maximum steps in any direction is seven
			# There are always 14 (8+8-2) possible moves, ignoring blocked squares
			# Blocked squares are those that are occupied by an ally piece, or obscured by an enemy piece
			# TODO: Extract helper functions (comparing colour, etc.)
			'♖♜': chain( takewhile(accessible(lambda mx, my: board.board[mx-1][my]), ((x+dx, y) for dx in range(1, 7+1))),
				           takewhile(accessible(lambda mx, my: board.board[mx+1][my]), ((x-dx, y) for dx in range(1, 7+1))),
				           takewhile(accessible(lambda mx, my: board.board[mx][my-1]), ((x, y+dy) for dy in range(1, 7+1))),
				           takewhile(accessible(lambda mx, my: board.board[mx][my+1]), ((x, y-dy) for dy in range(1, 7+1)))),
			# Moves two steps in one direction and two in the other (not diagonally).
			# Is able to jump over other pieces
			'♘♞': [(x+dx, y+dy) for dx in (-1, 1, -2, 2) for dy in (-1, 1, -2, 2) if valid(x+dx, y+dy) and abs(dx) != abs(dy)],
			# Can move any number of steps diagonally
			# 
			'♗♝': [(x+delta, y+delta) for delta in range(1, 7+1) if valid(x+delta, y+delta) and accessible((x+delta,y+delta))] +
					[(x-delta, y+delta) for delta in range(1, 7+1) if valid(x+delta, y+delta) and accessible((x+delta,y+delta))] +
					[(x+delta, y-delta) for delta in range(1, 7+1) if valid(x+delta, y+delta) and accessible((x+delta,y+delta))] +
					[(x-delta, y-delta) for delta in range(1, 7+1) if valid(x+delta, y+delta) and accessible((x+delta,y+delta))],
			#
			'♕♛': [],
			#
			'♔♚': [],
			# Direction depends on colour 
			# TODO: Avoid hard-coding colour-dependent direction
			# TODO: Simplify 
			'♙♟': ([(x, y+dyPawn)] if valid(x, y+dyPawn) else []) + [(x+dx, y+dyPawn) for dx in (-1, 1) if hasEnemy(x+dx, y+dyPawn)]
		}, mnemonic='moves')[self.piece]



def main():

	'''
	Docstring goes here

	'''
	
	p = Piece('♔')



if __name__ == '__main__':
	main()