import sys
import os
import socket

# Command line argument check
if len(sys.argv) != 2:
    print("USAGE: " + sys.argv[0] + "<SERVER PORT>")
    sys.exit(1)

# The port on which to listen
listenPort = int(sys.argv[1])		

# Create a welcome socket
welcomeSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
welcomeSock.bind(('', listenPort))

# Start listening on the socket
welcomeSock.listen(1)

print("Server listening on port", listenPort)

client_socket, client_address = welcomeSock.accept()
print(f"Connection from {client_address} established.")

client_socket.close()