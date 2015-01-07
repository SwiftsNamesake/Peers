#
# Board.py
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

from Square import Square



class Board(object):

	'''
	Docstring goes here

	'''

	initial = ( '♖♘♗♕♔♗♘♖',
				'♙♙♙♙♙♙♙♙',
				'        ',
				'        ',
				'        ',
				'        ',
				'♟♟♟♟♟♟♟♟',
				'♜♞♜♛♚♝♞♜')

	# TODO: Implement magic methods

	def __init__(self, size, **styles):

		'''
		Docstring goes here

		'''

		self.board = self.create(size, **styles) # TODO: Rename (eg. squares, tiles) (?)
		self.size  = size # The size of each square
		self.highlighted = [] # Highlighted squares


	def create(self, size, **styles):

		'''
		Docstring goes here

		'''

		return [[Square(size, col, row, Board.initial[row][col], **styles) for row in range(8)] for col in range(8)]


	def render(self, canvas):

		'''
		Docstring goes here

		'''

		for col, row, square in self:
			square.render(canvas)


	def at(self, x, y):
		
		'''
		Retrieves the Square at the specified coordinate

		'''

		# TODO: Deal with invalid input (...)
		# TODO: Dealing with margins, padding, etc.
		# TODO: Flexible output (Square, col and row, etc.)

		col  = x//self.size
		row  = y//self.size

		if (0 <= col < 8) and (0 <= row < 8):
			return col, row
		else:
			return False


	def highlight(self, canvas, undo, *squares):

		'''
		Docstring goes here

		'''

		# Remove highlighting from those squares that currently have it
		if undo:
			for square in self.highlighted:
				square.highlighted = False
				canvas.itemconfig(square.id, fill=square.styles['fill'])
			del self.highlighted[:] # Update list of highlighted squares

		# Highlight squares
		for col, row in squares:
			square = self.board[col][row]
			if not square.highlighted:
				self.highlighted.append(square) # Add to list of highlighted squares for easy access
				canvas.itemconfig(square.id, fill=square.hlFill)
				square.highlighted = True



	def __iter__(self):

		'''
		Docstring goes here

		'''

		# TODO: Use named tuple (?)
		return ((col, row, self.board[col][row]) for col in range(8) for row in range(8))



def main():

	'''
	Docstring goes here

	'''
	
	b = Board(60)



if __name__ == '__main__':
	main()