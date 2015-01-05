#
# Piece.py
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




def main():

	'''
	Docstring goes here

	'''
	
	p = Piece('♔')



if __name__ == '__main__':
	main()