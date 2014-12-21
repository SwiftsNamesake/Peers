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



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Create a socket object
host = socket.gethostname()	# Get local machine name
port = 10000				# Reserve a port for your service.
sock.bind(('192.168.1.88', port))		# Bind to the port

sock.listen(5)                 # Now wait for client connection.

while True:
	connection, address = sock.accept()     # Establish connection with client.
	print('Got connection from', address)
	connection.send('Thank you for connecting')
	connecting.close()