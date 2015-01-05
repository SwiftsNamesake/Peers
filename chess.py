#
# Chess.py
# Description...
# 
# Jonatan H Sundqvist
# January 4 2015
#

# TODO | - Rulebook (interactive, animated?)
#        - 3D
#        - Sounds, pygame (?)
#        - Strict separation between logic and interaction
#
# SPEC | -
#        -



import tkinter as tk

from collections import namedtuple

from SwiftUtils.MultiSwitch import MultiSwitch
from Board import Board
from Piece import Piece



def main():
	
	'''
	Docstring goes here

	'''

	for piece in '♔♕♖♗♘♙♚♛♜♝♞♟':
		x = Piece(piece)
		print('{0.name} is {0.colour}'.format(x))

	root = tk.Tk()
	root.title('Chess')
	root.resizable(width=False, height=False)
	canvas = tk.Canvas(width=8*60, height=8*60)
	canvas.pack()

	board = Board(60)
	board.render(canvas)

	def onclick(event):
		col, row = event.x//board.size, event.y//board.size
		print('x={0.x}, y={0.y}, col={1}, row={2}'.format(event, col, row))
		board.highlight(canvas, True, (event.x//board.size, event.y//board.size)) # TODO: Coordinate method, handle offsets and margins probably

	root.bind('<Button-1>', onclick)

	root.mainloop()


if __name__ == '__main__':
	main()