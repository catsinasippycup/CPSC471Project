import sys
import os
import socket

def recvAll(sock, numBytes):
    # The buffer
    recvBuff = ""
    
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

# Command line argument check
if len(sys.argv) != 2:
    print("USAGE: " + sys.argv[0] + " <SERVER PORT>")
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

# Accept the connection
client_socket, client_address = welcomeSock.accept()
print(f"Connection from {client_address} established.")

fileno = 0

# Keep sending until all is sent
while True:
    # Receive the data
    command = client_socket.recv(1024).decode()
    
    if command.startswith("get"):
        fileName = command[4:]
        try:
            with open(fileName, "r") as fileObj:
                # Read 65536 bytes of data
                fileData = fileObj.read(65536)
                # Make sure we did not hit EOF
                if fileData:
                    # Get the size of the data read and convert it to string
                    dataSizeStr = str(len(fileData))
                    
                    # Prepend 0's to the size string until the size is 10 bytes
                    while len(dataSizeStr) < 10:
                        dataSizeStr = "0" + dataSizeStr
                    # Prepend the size of the data to the file data.
                    fileData = dataSizeStr + fileData
                    # The number of bytes sent
                    numSent = 0
                    # Send the data!
                    while len(fileData) > numSent:
                        numSent += client_socket.send(fileData[numSent:].encode())
                # The file has been read. We are done
                else:
                    break
                print ("Sent ", numSent, " bytes.")
                print ("Get command success")

        except FileNotFoundError:
            print("File not found")

    elif command.startswith('ls'):
        try:
            # get list of files in current directory
            files = os.listdir('.')
            # convert list of files into string seprated by new lines
            files_list = "\n".join(files)
            # send list of fiels back to the client
            client_socket.sendall(files_list.encode())
            print ('List command success')
        except FileNotFoundError:
            # directory not found error
            client_socket.send("Directory not found".encode())

    elif command.startswith("put"):
        
        # The buffer to all data received from the client.
        fileData = ""
        
        # The temporary buffer to store the received data.
        recvBuff = ""
        
        # The size of the incoming file
        fileSize = 0
        
        # The buffer containing the file size
        fileSizeBuff = ""
        
        # Receive the first 10 bytes indicating the size of the file
        fileSizeBuff = recvAll(client_socket, 10)
        
        # Get the file size
        fileSize = int(fileSizeBuff)
        
        print (f"The file size is {fileSize} bytes" )
        
        # Get the file data
        fileData = recvAll(client_socket, fileSize)
        
        fileName = command.split("\\")[-1]
        fileOut = open(fileName, "w")
        fileOut.write(fileData)
        fileOut.close()
    else:
        print(f"Client: {client_address} disconnected")
        break

# Close the connection
client_socket.close()
