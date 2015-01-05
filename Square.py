#
# Square.py
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



from Piece import Piece



class Square(object):

	'''
	Docstring goes here

	'''


	def __init__(self, size, col, row, piece, **styles):

		'''
		Docstring goes here

		'''

		# TODO: Move styles to render method
		# TODO: Reduce to single expression or move to method
		self.styles = {
			# Tkinter
			'fill': ('grey', 'white')[col%2==row%2],
			'width': 0,

			# Other (will be removed during initialization)
			'hlFill': ('blue', 'cyan')[col%2==row%2]
		}

		self.styles.update(styles)

		self.size = size
		self.col = col
		self.row = row
		self.piece = Piece(piece) if piece != ' ' else None # TODO: Decide how to handle empty squares
		self.id = None # Canvas item ID

		# TODO: More generic handling of styles and highlighting
		self.highlighted = False
		self.hlFill = self.styles.pop('hlFill') # Highlight fill colour


	def render(self, canvas):
		
		'''
		Docstring goes here

		'''

		col, row, size = self.col, self.row, self.size

		self.coords = (col*size, row*size, (col+1)*size, (row+1)*size)
		self.id = canvas.create_rectangle(self.coords, **self.styles)
		if self.piece is not None:
			self.piece.render(canvas, size, self.col, self.row)



def main():

	'''
	Docstring goes here

	'''

	s = Square(60, 4, 4, '♔')



if __name__ == '__main__':
	main()