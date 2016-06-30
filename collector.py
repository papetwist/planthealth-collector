#!/bin/python
#0.1

import sqlalchemy
import time
import serial

# detect com port
for com in range(0,4):
    try:
		board = serial.Serial()
		board.port = '/dev/ttyACM'+str(com)
		board.baudrate = 9600
		board.timeout = 4 
		board.databits = 8
		board.stopbits = 1
		board.open()
		time.sleep(2)
		#board.close()		
		break
    except:
		pass

configmatch = 1

while configmatch:
	actuators = board.readline()
	print actuators
	print "read..."

print "end"

def updateconfig():
	board.write("TEST;")
	answer = board.readline()
	return 0

board.close()
