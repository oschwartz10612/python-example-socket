# python-example-socket

#Setup
You need a client and a server Raspberry Pi. The client will have your inputs (buttons, sensors, etc) the server will run your actions (run motors, print textm, etc). For the example, connect a button to the client Pi as shown below.

![Wiring Diagram](/assets/02_Push-button_bb-min.jpg)

Clone this repo to both Pis.

```
git clone https://github.com/oschwartz10612/python-example-socket.git
```

Run the server.py script on the server Pi and client.py on the client Pi. When you press the button, you should see a message on the server.
```
python server.py

python client.py
```

#Explanation
Read the comments and try to understand the code. Modify the client and the server to get a better understanding of how they work.

###Server
```python
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
```

###Client
```python
#The UDP echo client is similar the server, but does not use bind() to attach its socket to an address. It uses sendto() to deliver its message directly to the server, and recvfrom() to receive the response.

import socket #Import the socket

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

#Setup Rraspberry Pi GPIO
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Connect to the server pi. Make sure to change the IP address.
server_address = ('localhost', 3000)

#Run a loop and check for a button press on pin 10
while True:
    if GPIO.input(10) == GPIO.HIGH:
        #If the button is pressed send to the server a message. 1 meaning pressed.
        sock.sendto("1", server_address)
```

###Add more inputs?
Connect your input as instructed. Read its data and use the sendto() function to send the data to the server. Call this for all of your sensors. 

On the server receive the data and process it. Identifiers for each sensor may be required.
