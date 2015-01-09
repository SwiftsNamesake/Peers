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


	def check(self, board, x, y):
		
		'''
		Docstring goes here

		'''

		pass


	def moves(self, board, x, y, piece=None):

		'''
		Retrieves a list of valid moves for this piece, given a board and a position.

		'''

		# TODO: Take piece type as argument (?)

		# TODO: Optimise, cache, lazy evaluation (create the switch only once)
		# TODO: Simplify with itertools, generators
		# TODO: Prevent NoneType errors (square.piece is None if square is empty) (find a better way to represent empty squares?)

		# TODO: Pre-calculate maximum range based on position (eg. maximum dx = 8-x) (?)

		# TODO: Function to combine predicates

		piece = piece or self.piece # Optional argument for piece type (defaults to self)

		within = board.within
		isEmpty = lambda cl, rw: board.board[cl][rw].piece == None
		hasEnemy = lambda cl, rw: within(cl,rw) and not isEmpty(cl, rw) and board.board[cl][rw].piece.colour != self.colour
		valid = lambda cl, rw: within(cl, rw) and (hasEnemy(cl, rw) or isEmpty(cl, rw))

		def accessible(previous):
			# Creates a function which determines if a particular square is accessible
			# Previous is a function which returns the previous square in a series of moves
			def predicate(m):
				px, py = previous(*m)
				return valid(*m) and (not valid(px, py) or board.board[px][py].piece in (None, self)) # TODO: Add prev argument (?)
			return predicate

		

		dyPawn = (-1, 1)[self.colour=='white']

		return MultiSwitch({
			# The Rook
			# Maximum steps in any direction is seven
			# There are always 14 (8+8-2) possible moves, ignoring blocked squares
			# Blocked squares are those that are occupied by an ally piece, or obscured by an enemy piece
			# TODO: Extract helper functions (comparing colour, etc.)
			'♖♜': lambda: chain( takewhile(accessible(lambda mx, my: (mx-1, my)), ((x+dx, y) for dx in range(1, 7+1))),
				                   takewhile(accessible(lambda mx, my: (mx+1, my)), ((x-dx, y) for dx in range(1, 7+1))),
				                   takewhile(accessible(lambda mx, my: (mx, my-1)), ((x, y+dy) for dy in range(1, 7+1))),
				                   takewhile(accessible(lambda mx, my: (mx, my+1)), ((x, y-dy) for dy in range(1, 7+1)))),
			# The Knight
			# Moves two steps in one direction and two in the other (not diagonally).
			# Is able to jump over other pieces
			'♘♞': lambda: [(x+dx, y+dy) for dx in (-1, 1, -2, 2) for dy in (-1, 1, -2, 2) if valid(x+dx, y+dy) and abs(dx) != abs(dy)],
			# The Bishop
			# Can move any number of steps diagonally
			'♗♝': lambda: chain( takewhile(accessible(lambda mx, my: (x-1,y-1)), ((x+delta, y+delta) for delta in range(1, 7+1))),
						           takewhile(accessible(lambda mx, my: (x-1,y+1)), ((x+delta, y-delta) for delta in range(1, 7+1))),
						           takewhile(accessible(lambda mx, my: (x+1,y-1)), ((x-delta, y+delta) for delta in range(1, 7+1))),
						           takewhile(accessible(lambda mx, my: (x+1,y+1)), ((x-delta, y-delta) for delta in range(1, 7+1)))),
			# The Queen
			# Can move any number of steps in any one direction (equivalent to a combined Rook and Bishop)
			'♕♛': lambda: chain(self.moves(board, x, y, piece='♖'), self.moves(board, x, y, piece='♗')),
			# The King
			# Can move a single step in any direction
			# TODO: Use itertools.product (?)
			'♔♚': lambda: [(x+dx, y+dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if valid(x+dx, y+dy)],
			# Direction depends on colour 
			# TODO: Avoid hard-coding colour-dependent direction
			# TODO: Simplify 
			'♙♟': lambda: ([(x, y+dyPawn)] if within(x, y+dyPawn) and isEmpty(x, y+dyPawn) else []) + [(x+dx, y+dyPawn) for dx in (-1, 1) if hasEnemy(x+dx, y+dyPawn)]
		}, mnemonic='moves')[piece]()


	def __str__(self):
		return '{0.colour} {0.name}'.format(self)

	def __repr__(self):
		raise NotImplementedError



def main():

	'''
	Docstring goes here

	'''
	
	p = Piece('♔')



if __name__ == '__main__':
	main()