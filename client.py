#
# Peers - client.py
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
sock.bind((host, port))		# Bind to the port


host = '192.168.1.88'
print(host, port)
sock.connect((host, port))
sock.close