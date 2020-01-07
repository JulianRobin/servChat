import socket
import threading
import sys

def sending(client):
	while True:
		try:
			msg = input()

			if msg == 'quit':
				client.close()
				sys.exit()

			# print ('outgoing:', msg)
			client.sendall(msg.encode('utf-8'))
		except:
			print("connection borked")
			client.close()
			sys.exit()

def listening(client):
	while True:
		try:
			print(client.recv(1024).decode('utf-8'))
		except:
			print('Connection borked')
			client.close()
			sys.exit()

# start server
server = socket.socket()
port = int(input('enter port\n'))

server.bind(('', port))
server.listen(5)

print('starting server, "quit" to exit')

client, addr = server.accept()
#client = ''

print('creating threads')
listener = threading.Thread(target = listening, args = [client])
sender = threading.Thread(target = sending, args = [client])

listener.start()
sender.start()

