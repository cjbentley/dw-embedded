import serial
from controller import connect, command

ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600
ser.timeout = 1
ser.rtscts = False # disable hardware (RTS/CTS) flow control

s = connect()

def direction(val):
	if val < 0:
		return "R"
	else:
		return "F"

def msg(motorL, motorR): # Inputs as -100 to 100
	msg = "X" + direction(motorL) + f"{abs(motorL):03}" + direction(motorR) + f"{abs(motorR):03}" + "\n"
	return(msg)

while True:
	L, R = command(s)

	if ser.is_open == False:
		ser.open()
	ser.write(bytes(msg(L, R), 'ascii')) # X is dropped 🤔
	x = ser.read()
	y = []
	if x == b'\n': # End of line marker
		for i in range(0,9):
			tmp = ser.read()
			y.append(tmp)
		y.pop(0)
		print(y)