#
# Peers - server.py
# Peer to peer connections over LAN
#
# Jonatan H Sundqvist
# December 21 2014
#

# TODO | -
#        -
#
# SPEC | -
#        -



import socket, sys               # Import socket module
import pickle

import tkinter as tk
# from PIL import Image
# from PIL import ImageTk

import random
import threading, queue



def createContext():

	'''
	Docstring goes here

	'''

	SIZE = 720, 480
	root = tk.Tk()
	root.title('Server')
	root.geometry('{0:}x{1:}'.format(*SIZE))
	root.canvas = tk.Canvas(width=SIZE[0], height=SIZE[1])
	root.canvas.pack()

	updates = queue.Queue()

	return root, updates


root, updates = createContext()


def listen(ip, port):
	
	'''
	Docstring goes here

	'''

	#
	clients = []
	running = True

	# Create and bind socket for incoming connections
	sock = socket.socket() # TODO: Arguments to constructor (?)
	sock.bind((ip, port))
	sock.listen(5)

	# TODO: Managing clients after connection
	# TODO: Quitting gracefully

	#
	while running:
		client = sock.accept() # Client connection (conn, addr)
		clients.append(client)
		print('Accepted client #{0:}: {1:}'.format(len(clients), client[1]))
		clientFork(*client)

	sock.close()



def clientFork(conn, addr):

	'''
	Docstring goes here

	'''

	print('Creating a new client process for {0:}.'.format(addr))


	fill = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	height = 0 #random.randint(20, 125)
	cur = root.canvas.create_oval((0,0,0,0), fill=fill)

	def protocol(conn, addr):

		# TODO: Separate IO and logic

		# Communication logic
		try:
			size = int(conn.recv(4).decode('utf-8')) 	# Read size prefix (padded to four digits)
			received = conn.recv(size) 					# Read data
		except:
			print('Lost connection with {0:}.'.format(addr))
			return False

		data = pickle.loads(received)
		print('Server received {0:} bytes from {1:}.'.format(size, addr)) # TODO: Print representation of incoming data (?)

		# Application logic
		if isinstance(data, str) and data.lower() in ('quit', 'q', 'exit', 'stop', 'no more', 'please', 'leave me alone', 'terminate'):
			print('Terminating client process ({0:}).'.format(addr))
			return False
		else:
			for point in data:
				if point[0] == 'cur':
					x, y = point[1]
					root.canvas.coords(cur, (x-10, y-10, x+10, y+10))
				else:
					updates.put((point, fill, height), block=False)
			return True

		# root.after(1000//30, lambda: protocol(conn, addr)) # Run again after a set amount of time

	def program(conn, addr):
		running = protocol(conn, addr)
		while running:
			print('Running protocol')
			running = protocol(conn, addr)

	threading.Thread(target=program, args=(conn, addr)).start()



def configure():

	'''
	Docstring goes here

	'''

	pass



def main():

	'''
	Docstring goes here

	'''
	
	threading.Thread(target=listen, args=('localhost', 44000)).start()

	def pollUpdates():
		while not updates.empty():
			print('Polling updates')
			point, fill, height = updates.get(block=False)
			print('Point is a', type(point))
			root.canvas.create_rectangle((point[0], point[1]+height, point[0]+15, point[1]+15+height), fill=fill, width=0)
		root.after(1000//30, pollUpdates)

	pollUpdates()
	
	root.mainloop()

if __name__ == '__main__':
	main()