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
#        - Clock
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

		self.selected = None # Selected piece (square)


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

		self.bind('<Button-1>', lambda e: self.onclick(e))
		self.bind('<Motion>', lambda e: self.onmove(e))


	def createMenus(self):
		
		'''
		Docstring goes here

		'''

		pass


	def askNames(self):

		'''
		Docstring goes here

		'''

		self.players = namedtuple('Players', 'one two')(input('Name of the first player'), input('Name of the second player'))


	def onclick(self, event):
		
		board = self.board
		canvas = self.canvas
		pos = board.at(event.x, event.y)

		if pos == False:
			return

		# TODO: Take turns into account
		# TODO: Turn feedback

		if self.selected is None and board.board[pos[0]][pos[1]].piece != None:
			self.selected = pos
			col, row = self.selected
			piece = board.board[col][row].piece
			board.highlight(canvas, True, *piece.moves(board, col, row))
			print('Selecting a piece ({0})'.format(piece))
		elif self.selected is not None:
			self.board.move(self.selected, pos)
			self.board.render(self.canvas)
			print('Moving a piece ({0})'.format(board.board[self.selected[0]][self.selected[1]].piece))
			self.selected = None


	def onmove(self, event):
		return
		board = self.board
		canvas = self.canvas
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

	game = ChessApp(60)
	game.run()



if __name__ == '__main__':
	main()