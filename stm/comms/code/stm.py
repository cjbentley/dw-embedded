import serial

ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600
ser.timeout = 1
ser.rtscts = False # disable hardware (RTS/CTS) flow control

def direction(val):
	if val < 0:
		return "R"
	else:
		return "F"

def msg(motorL, motorR): # Inputs as -100 to 100
	print(direction(motorL), f"{abs(motorL):03}", direction(motorR), f"{abs(motorR):03}")


while True:
	if ser.is_open == False:
		ser.open()
	ser.write(b'XF024R015\n') # X is dropped 🤔
	x = ser.read()
	y = []
	if x == b'\n': # End of line marker
		for i in range(0,9):
			tmp = ser.read()
			y.append(tmp)
		y.pop(0)
		print(y)

	msg(20,-100)