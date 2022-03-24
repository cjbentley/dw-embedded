import hid
import time
import socket
import os
from control_law import control_law

in_container = os.environ.get('IN_A_CONTAINER', False)

if in_container:
	target = 'network', 10000
else:
	print('Running outside container. Forwarding over Tailscale...')
	target = '100.77.206.50', 10000

### Networking
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# please get device vendor and product ID interactively using:
# for device in hid.enumerate():
#    print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

gamepad = hid.device()
gamepad.open(0x045e, 0x02fd)
gamepad.set_nonblocking(True) 	# don't hang if device not ready
stick_tol = 0.05 				# analog stick tolerance for zeroing

### Initialize with zero
LS_X = 0
LS_Y = 0 
RS_X = 0
RS_Y = 0
LT = 0 
RT = 0
DPAD = 0 
A = 0 
B = 0
X = 0
Y = 0
LB = 0 
RB = 0
LS_B = 0
RS_B = 0
SELECT = 0

while True:
	time.sleep(0.01)
	report = gamepad.read(64)
	if len(report) == 17: 		# don't want malformed reports
		### Left stick X-axis
		LS_X = (report[2]/255)-0.5
		if abs(LS_X) <= stick_tol: 	# analog stick tolerance for zeroing
			LS_X = 0
		
		### Left stick Y-axis
		LS_Y = -((report[4]/255)-0.5) # inverted from hid input; +'ve for forward, -'ve for backward
		if abs(LS_Y) <= stick_tol:
			LS_Y = 0

		### Right stick X-axis
		RS_X = (report[6]/255)-0.5
		if abs(RS_X) <= stick_tol:
			RS_X = 0

		### Right stick Y-axis
		RS_Y = -((report[8]/255)-0.5)
		if abs(RS_Y) <= stick_tol:
			RS_Y = 0

		### Left trigger
		LT = (report[9] + (report[10]*255))/1020

		### Right trigger
		RT = (report[11] + (report[12]*255))/1020

		### D-pad direction
		DPAD = report[13]

		### A/B/X/Y/LB/RB handling
		value = report[14]
		if value >= 128:
			RB = 1
			value = value - 128
		else: 
			RB = 0

		if value >= 64:
			LB = 1
			value = value - 64
		else:
			LB = 0

		if value >= 16:
			Y = 1
			value = value - 16
		else:
			Y = 0

		if value >= 8:
			X = 1
			value = value - 8
		else:
			X = 0

		if value >= 2:
			B = 1
			value = value - 2
		else:
			B = 0

		if value >= 1:
			A = 1
		else:
			A = 0

		### Stick buttons
		value = report[15]
		if value >= 64:
			RS_B = 1
			value = value - 64
		else:
			RS_B = 0

		if value >= 32:
			LS_B = 1
		else:
			LS_B = 0

		### Select button handling
		SELECT = report[16]

	### Sending
	array = str(LS_X), str(LS_Y), str(RS_X), str(RS_Y), str(LT), str(RT), str(DPAD), str(A), str(B), str(X), str(Y), str(LB), str(RB), str(LS_B), str(RS_B), str(SELECT) 
	motor_L, motor_R = control_law(array)
	print(array)
	packaged = str(motor_L) + '/' + str(motor_R)
	print(packaged)
	s.sendto(packaged.encode(), target)
