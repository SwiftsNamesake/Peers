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

		# TODO: Optimise, cache, lazy evaluation
		# TODO: Simplify with itertools, generators
		# TODO: Prevent NoneType errors (square.piece is None if square is empty) (find a better way to represent empty squares?)

		within = board.within

		accessible = lambda m: (board.board[m[0]][y].piece.colour != self.colour) and (board.board[m[0]-1][y].piece == None) # TODO: Add prev argument (?)

		isEmpty = lambda cl, rw: board.board[cl][rw].piece == None
		hasEnemy = lambda cl, rw: within(cl,rw) and not isEmpty(cl, rw) and board.board[cl][rw].piece.colour != self.colour
		
		valid = lambda cl, rw: within(cl, rw) and (hasEnemy(cl, rw) or isEmpty(cl, rw))

		dyPawn = (-1, 1)[self.colour=='white']

		return MultiSwitch({
			# Maximum steps in any direction is seven
			# There are always 14 (8+8-2) possible moves, ignoring blocked squares
			# Blocked squares are those that are occupied by an ally piece, or obscured by an enemy piece
			# TODO: Extract helper functions (comparing colour, etc.)
			'♖♜': chain( takewhile(accessible, ((x+dx, y) for dx in range(7))),
				           takewhile(accessible, ((x-dx, y) for dx in range(7))),
				           takewhile(accessible, ((x, y+dy) for dy in range(7))),
				           takewhile(accessible, ((x, y-dy) for dy in range(7)))),
			#
			'♘♞': [(x+dx, y+dy) for dx in (-1, 1, -2, 2) for dy in (-1, 1, -2, 2) if valid(x+dx, y+dy) and dx != dy],
			#
			'♗♝': [],
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