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
