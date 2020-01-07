import socket
import threading
import sys

def sending(server):
        while True:
                msg = input()

                if msg == 'quit':
                        server.close
                        sys.exit()

                print ('outgoing:', msg)
                server.sendall(msg.encode('utf-8'))

def listening(server):
	while True:
		print(server.recv(1024).decode('utf-8'))


# Create a socket object
server = socket.socket()

# Define the port on which you want to connect
port = int(input('Enter port\n'))

# connect to the server on local computer
server.connect(('127.0.0.1', port))


print('creating threads')
listener = threading.Thread(target = listening, args = [server])
sender = threading.Thread(target = sending, args = [server])

listener.start()
sender.start()
