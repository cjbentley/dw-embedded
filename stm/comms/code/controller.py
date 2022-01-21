import socket
import select

### Networking configuration
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	host = '0.0.0.0'
	port = 10000
	s.bind((host, port))
	return s

#ser = serial.Serial('/dev/ttyUSB0')
#print(ser.name)         # check which port was really used
def command(s):
	#timeout = 0.01
	#ready = select.select([s], [], [], timeout)
	#if ready[0]:
	data, addr = s.recvfrom(1024)
	data = data.decode()
	array = data.split('/')
	array = array[1:-1]

	# To make life easier
	LS_X = array[0]
	LS_Y = array[1]
	RS_X = array[2]
	RS_Y = array[3]
	LT = array[4]
	RT = array[5]
	DPAD = array[6]
	A = array[7]
	B = array[8]
	X = array[9]
	Y = array[10]
	LB = array[11]
	RB = array[12]
	LS_B = array[13]
	RS_B = array[14]
	SELECT = array[15]

	# Robot control
	motor_L = int(round(100*float(LT), 0))
	motor_R = int(round(100*float(RT), 0))




	return motor_L, motor_R