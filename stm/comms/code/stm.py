import serial

ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600
ser.timeout = 1
ser.rtscts = False # disable hardware (RTS/CTS) flow control

while True:
	if ser.is_open == False:
		ser.open()
	ser.write(b'F024R015\n')
	#x = ser.read_until(b'\n');
	x = ser.read()
	y = []
	if x == b'\n':
		# print(x, ser.read())
		for i in range(0,8):
			tmp = ser.read()
			y.append(tmp)
		print(y)