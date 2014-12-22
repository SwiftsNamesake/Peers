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

from PIL import Image
from PIL import ImageTk



def original():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Create a socket object
	host = socket.gethostname()	# Get local machine name
	port = 10000				# Reserve a port for your service.
	sock.bind((host, port))		# Bind to the port


	host = '192.168.1.88'
	print(host, port)
	sock.connect((host, port))
	sock.close



def other():
	# Sockets client script

	world = []
	x = 0

	s = socket.socket()

	print("Connecting to server...")

	while True:
		try:
			s.connect(("localhost", 44000))
			break
		except:
			print("Retrying connection to server...")
			time.sleep(1)

	print("Connection Matched!")

	while True:
		# keyboardInput = input("Enter the message: ")
		# s.send(bytes(message, 'UTF-8'))
		# message = keyboardInput.encode('utf-8')
		# s.send(message)

		update = []
		for i in range(random.randint(1, 10)):
			update.append((x, 40+20*sin(x*π/180.0)))
			x += 5
		world += update

		# TODO: Protocol for sending smaller packets of pickled data in sequence
		data = pickle.dumps(update)
		s.send(bytes('{0:04d}'.format(len(data)), 'utf-8') + data) # Send data with padded length prefix

		print("Message sent!")
		# r = s.recv(512) #(128*10)
		# a = r
		# a = r.decode('utf-8')
		# print("Confirmation received message: ", r)
		# if keyboardInput == "quit":
			# break
		time.sleep(1)

	print("Good bye")

	s.close()

	a = input("Enter key to End:")



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
		conn.send(bytes('{0:04d}'.format(len(data)), 'utf-8') + data)

		root.after(1000//30, upload) # TODO: Better model for pushing updates (?)

	root.bind('<B1-Motion>', draw)
	root.bind('<Motion>', cursor)
	upload()


	root.mainloop()





if __name__ == '__main__':
	main()
	# other()