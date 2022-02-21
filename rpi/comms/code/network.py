import socket
import select

### Networking configuration
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	host = '0.0.0.0'
	port = 10000
	s.bind((host, port))
	return s

def command(s):
	data, addr = s.recvfrom(1024)
	data = data.decode()
	array = data.split('/')

	motor_L = float(array[0])
	motor_R = float(array[1])

	return motor_L, motor_R