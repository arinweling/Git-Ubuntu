import time
from roboclaw_3 import Roboclaw
import signal
import sys
import os
from serial.serialutil import SerialException as SerialException


#Linux comport name
rc = Roboclaw("/dev/ttyUSB0",115200)

rc.Open()
address_1 = 0x80
address_2 =0x81
address_3 =0x82





while(1):
	speed_1=input("Enter speed_1: ")
	speed_2=input("Enter speed_2: ")
	speed_3=input("Enter speed_3: ")
	rc.ForwardM2(address_1,int(speed_1))
	rc.ForwardM2(address_2,int(speed_2))
	rc.ForwardM2(address_3,int(speed_3))

	
	