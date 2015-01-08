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
#        - Strict separation between logic and interaction (mvc, logic, graphics)
#        - Lift and drag a piece (shadow), animations
#
# SPEC | -
#        -



import tkinter as tk

from collections import namedtuple

from SwiftUtils.MultiSwitch import MultiSwitch
from Board import Board
from Piece import Piece


class ChessApp(tk.Tk):

	'''
	Docstring goes here

	'''

	def __init__(self, size):
		
		'''
		Docstring goes here

		'''

		self.createWindow(size)
		self.attachListeners()
		self.createMenus()

		self.board = Board(size)
		self.board.render(self.canvas)


	def createWindow(self, size):
		
		'''
		Docstring goes here

		'''

		super().__init__()

		self.title('Chess')

		self.resizable(width=False, height=False)
		self.canvas = tk.Canvas(width=8*size, height=8*size)
		self.canvas.pack()


	def attachListeners(self):
		
		'''
		Docstring goes here

		'''

		root.bind('<Button-1>', lambda e: self.onclick(e))
		root.bind('<Motion>', lambda e: self.onmove(e))


	def createMenus(self):
		
		'''
		Docstring goes here

		'''

		pass


	def onclick(self, event):
		
		pos = board.at(event.x, event.y)

		print('Click')
		if not pos:
			return

		print('Valid pos')
		col, row = pos

		if board.board[col][row].piece == None:
			return

		print('Non-empty square')
		print(*(board.board[col][row].piece.moves(board, col, row)))
		board.highlight(canvas, True, *(board.board[col][row].piece.moves(board, col, row)))
		# col, row = board.at(event.x, event.y)
		# board.highlight(canvas, True, (col, row)) # TODO: Coordinate method, handle offsets and margins probably

	def onmove(self, event):
		coord = board.at(event.x, event.y)
		if coord:
			board.highlight(canvas, True, coord)


	def run(self):
		
		'''
		Docstring goes here

		'''

		self.mainloop()



def main():
	
	'''
	Docstring goes here

	'''

	root = tk.Tk()
	root.title('Chess')
	root.resizable(width=False, height=False)
	canvas = tk.Canvas(width=8*60, height=8*60)
	canvas.pack()

	board = Board(60)
	board.render(canvas)

	def onclick(event):
		
		pos = board.at(event.x, event.y)

		print('Click')
		if not pos:
			return

		print('Valid pos')
		col, row = pos

		if board.board[col][row].piece == None:
			return

		print('Non-empty square')
		print(*(board.board[col][row].piece.moves(board, col, row)))
		board.highlight(canvas, True, *(board.board[col][row].piece.moves(board, col, row)))
		# col, row = board.at(event.x, event.y)
		# board.highlight(canvas, True, (col, row)) # TODO: Coordinate method, handle offsets and margins probably

	def onmove(event):
		coord = board.at(event.x, event.y)
		if coord:
			board.highlight(canvas, True, coord)

	root.bind('<Button-1>', onclick)
	root.bind('<Motion>', onmove)

	root.mainloop()


if __name__ == '__main__':
	main()