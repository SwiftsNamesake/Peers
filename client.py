#
# Peers - client.py
# Peer to peer connections over LAN
#
# Jonatan H Sundqvist
# December 21 2014
#

# TODO | - Promises (?)
#        -
#
# SPEC | -
#        -



import socket, sys, time               # Import socket module
import pickle
import tkinter as tk
import random
import threading, queue

from math import sin, cos, pi as π
from cmath import rect, polar

from PIL import Image
from PIL import ImageTk



def hexString(rgb):
	return  '#{:02x}{:02x}{:02x}'.format(*rgb)



def lotus(root, canvas):

	'''
	Docstring goes here

	'''

	origin = 250+250j
	palette = ((origin+rect(θ*0.3, θ*π/180.0), hexString((θ % 255, int(θ*1.5) % 255, int(θ*2.5) % 255))) for θ in range(0, 360, 10))

	def animate():
		for pos, colour in palette:
			id = canvas.create_oval((pos.real-2, pos.imag-2, pos.real+2, pos.imag+2), fill=colour)
			for r in range(2, 9):
				canvas.coords(id, (pos.real-r, pos.imag-r, pos.real+r, pos.imag+r))
				# root.after(1000//24, lambda: next(frames))
				yield
				# time.sleep(1.0/24)

	frames = animate()
	next(frames)




def original():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Create a socket object
	host = socket.gethostname()	# Get local machine name
	port = 10000				# Reserve a port for your service.
	sock.bind((host, port))		# Bind to the port


	host = '192.168.1.88'
	print(host, port)
	sock.connect((host, port))
	sock.close



def connect(host, port):
	
	'''
	Establish a connection with the server

	'''

	sock = socket.socket()
	delay = 1.0

	while True:
		try:
			print('Attempting to connect to {0:}'.format(host))
			sock.connect((host, port))
			print('Succeeded to connect.')
			break
		except:
			print('Failed to connect to {0:}'.format(host))
			print('Retrying after {0:} seconds'.format(delay))

	return sock



def main():
	
	'''
	Application entry point

	'''

	SIZE = 720, 480
	root = tk.Tk()
	root.title('Client')
	root.geometry('{0:}x{1:}'.format(*SIZE))
	root.canvas = tk.Canvas(width=SIZE[0], height=SIZE[1])
	root.canvas.pack()

	updates = queue.Queue()

	conn = connect('localhost', 44000)

	root.bind('<Return>', lambda e: lotus(root, root.canvas))

	def draw(event):
		point = event.x, event.y
		updates.put(point, False) # Do not block (?)

		root.canvas.create_oval((event.x-10, event.y-10, event.x+10, event.y+10), fill='blue', width=0)

	def cursor(event):
		point = event.x, event.y
		updates.put(('cur', point))

	def upload():

		'''
		Uploads changes to the server

		'''

		points = []
		while not updates.empty():
			points.append(updates.get(False))
		data = pickle.dumps(points)
		conn.send(bytes('{0:04d}'.format(len(data)), 'utf-8') + data) # TODO: Protocol for sending smaller packets of pickled data in sequence

		root.after(1000//30, upload) # TODO: Better model for pushing updates (?)

	root.bind('<B1-Motion>', draw)
	root.bind('<Motion>', cursor)
	upload()


	root.mainloop()





if __name__ == '__main__':
	main()
	# other()