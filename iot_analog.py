#1v =1000mv
# 1023=5
# 5000mv =1023
# x*5000/1023 = 4.88

import Netmaxiot   
from time import sleep
while 1:
	read= Netmaxiot.analogRead(0)
	voltage=read*4.88
	print read
	print voltage
	sleep(4)
	print "____________"




