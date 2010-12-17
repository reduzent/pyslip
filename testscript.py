#!/usr/bin/env python

PORT = 2345



# receive something
import socket, slip
conn = socket.socket()
conn.bind(('0.0.0.0', PORT))
conn.listen(1)
sock, addr = conn.accept()
rest = ''
started = False
escaped = False
deslipper = slip.slip()
while True:
	chunk = sock.recv(4096)
	if not chunk:
		break
	deslipper.append(chunk)
	packets = deslipper.decode()
	for packet in packets:
		print "RESULTS: ", repr(packet)
 		encoded = deslipper.encode(packet)
		sock.sendall(encoded)
