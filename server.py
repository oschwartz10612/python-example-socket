#Since there is no connection, per se, the server does not need to listen for and accept connections. It only needs to use bind() to associate its socket with a port, and then wait for individual messages.

import socket

# Create a Server Socket and wait for a client to connect
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 6666))
print ("UDP Server Waiting for client on port 6666")

# Recive data from client and decide which function to call
while True:
    dataFromClient, address = server_socket.recvfrom(256)
    print(dataFromClient)