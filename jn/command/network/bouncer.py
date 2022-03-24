# receive data from other nodes and forward to rpi
import socket

incoming = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
outgoing = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

target = '10.0.0.2', 10000
host = '0.0.0.0', 10000
incoming.bind(host)

while True:
	package, addr = incoming.recvfrom(1024)
	package = package.decode()
	print(package)

	outgoing.sendto(package.encode(), target)