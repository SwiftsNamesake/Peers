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
from itertools import takewhile

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

		return MultiSwitch({
			# Maximum steps in any direction is seven
			# There are always 14 (8+8-2) possible moves, ignoring blocked squares
			# Blocked squares are those that are occupied by an ally piece, or obscured by an enemy piece
			# TODO: Extract helper functions (comparing colour, etc.)
			'♖♜': takewhile(lambda m: board[x+dx][y].piece.colour != self.colour and board[x+dx-1][y].piece == None, ((x+dx, y) dx in range(7))),
			#
			'♘♞': [(x, y) for x in () for y in ()],
			#
			'♗♝': [],
			#
			'♕♛': [],
			#
			'♔♚': [],
			#
			'♙♟': []
		}, mnemonic='moves')[self.piece]



def main():

	'''
	Docstring goes here

	'''
	
	p = Piece('♔')



if __name__ == '__main__':
	main()