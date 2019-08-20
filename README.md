# python-example-socket
Example implementation of Python socket communication between Raspberry Pis. 

## Setup
You need a client and a server Raspberry Pi. The client will have your inputs (buttons, sensors, etc) the server will run your actions (run motors, print text, etc). For the example, connect a button to the client Pi as shown below.

![Wiring Diagram](/assets/02_Push-button_bb-min.jpg)

Clone this repo to both Pis.

```
git clone https://github.com/oschwartz10612/python-example-socket.git
```

Edit the server.py and change the IP "localhost" to the IP of the client Pi. Edit the client.py and change the IP "localhost" to the IP of the server Pi.

Run the server.py script on the server Pi and client.py on the client Pi. When you press the button, you should see a message on the server.
```
python server.py

python client.py
```

## Explanation
Read the comments and try to understand the code. Modify the client and the server to get a better understanding of how they work.

#### Server
```python
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
```

#### Client
```python
#The UDP echo client is similar the server, but does not use bind() to attach its socket to an address. It uses sendto() to deliver its message directly to the server, and recvfrom() to receive the response.

import socket #Import the socket

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

#Setup Rraspberry Pi GPIO
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Run a loop and check for a button press on pin 10
while True:
    if GPIO.input(10) == GPIO.HIGH:
        #If the button is pressed send to the server a message. 1 meaning pressed.
        client_socket.sendto(data, ("IP", 6666))
        print ("Sending request")

        except Exception as ex:
            print ex
            raw_input()
        
        client_socket.close()
```

#### Add more inputs?
Connect your input as instructed. Read its data and use the sendto() function to send the data to the server. Call this for all of your sensors. 

On the server receive the data and process it. Identifiers for each sensor may be required.
