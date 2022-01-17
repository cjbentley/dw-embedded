import serial

ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600
ser.rtscts = False # disable hardware (RTS/CTS) flow control

while True:
	if ser.is_open == False:
		ser.open()
	ser.write(b"OK123456\n")
	x = ser.read(10);
	print(x)
