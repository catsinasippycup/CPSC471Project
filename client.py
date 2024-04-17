import sys
import os
import socket

def recvAll(sock, numBytes):

	# The buffer
	recvBuff = ""
	
	# The temporary buffer
	tmpBuff = ""
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		
		# Attempt to receive bytes
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff.decode()
	
	return recvBuff

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
    
    if command.startswith('get'):
        
        # Send all commands in order to get data from server
        connSock.send(command.encode())
        
        # The buffer to all data received from the client.
        fileData = ""
        
        # The temporary buffer to store the received data.
        recvBuff = ""
        
        # The size of the incoming file
        fileSize = 0
        
        # The buffer containing the file size
        fileSizeBuff = ""
        
        # Receive the first 10 bytes indicating the size of the file
        fileSizeBuff = recvAll(connSock, 10)
        
        # Get the file size
        fileSize = int(fileSizeBuff)
        
        print (f"The file size is  {fileSize} bytes" )
        
        # Get the file data
        fileData = recvAll(connSock, fileSize)
        
        print ("The file data is: ")
        print (fileData, "\n")
        
    elif command.startswith('quit'):
        print("Disconnecting")
        break
     

print("Socket closing")   
connSock.close()