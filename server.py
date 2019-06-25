#Since there is no connection, per se, the server does not need to listen for and accept connections. It only needs to use bind() to associate its socket with a port, and then wait for individual messages.

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 3000)
print('Starting server on port 3000')

sock.bind(server_address)

#Messages are read from the socket using recvfrom(), which returns the data as well as the address of the client from which it was sent.

while True:
    #Recive a message from the client pi. This could be nothing so we need to check.
    data, address = sock.recvfrom(4096)

    #If there is data, print it out and make a decision
    if data: 
        print(data)
        if data == "1":
            print("Button Pressed!")

