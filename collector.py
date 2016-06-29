#!/bin/python
#0.1

import sqlalchemy
import time
import serial

# detect com port
for com in range(0,4):
    try:
	PORT = '/dev/ttyACM'+str(com)
	BAUD = 9600
	board = serial.Serial(PORT,BAUD)
	#board.close()
	break
    except:
	pass

board.write("Hello")
answer = board.read()
print answer
