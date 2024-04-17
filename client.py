import sys
import os
import socket

# Command line checks 
if len(sys.argv) != 3:
	print ("USAGE python " + sys.argv[0] + " <SERVER ADDRESS> <SERVER PORT>" )
	sys.exit(1)
 
serverAddr = sys.argv[1]
serverPort = int(sys.argv[2])
 
connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connSock.connect((serverAddr, serverPort))
print("Connected to server")
 
while True:
    command = input("ftp> ")
    connSock.send(command.encode())

    if command.lower() == 'quit':
        print("Disconnecting")
        break

print("Socket closing")   
connSock.close()