import socket
import threading
import sys
import subprocess
import traceback
from colorama import init
from colorama import Fore, Back, Style
init()

def sending(client):
	while True:
		try:
			user = subprocess.run(['whoami' ], stdout=subprocess.PIPE).stdout.decode('utf-8').strip().split('\\')[-1]
			print (Fore.RED + user + ":", end = " ")
			msg = input()

			if msg == 'quit':
				client.close()
				sys.exit()

			user = subprocess.run(['whoami'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip().split('\\')[-1]
			#print (user, msg)
			colonstring = ": "
			toSend = "\n" + Fore.RED + user + colonstring + msg
			client.sendall(toSend.encode('utf-8'))
		except Exception as e:
			track = traceback.format_exc()
			print (track)
			print("connection borked")
			client.close()
			sys.exit()

def listening(client):
	while True:
		try:
			print(client.recv(1024).decode('utf-8'))
			print(Fore.RED, end=" ")
		except:
			print('Connection borked')
			client.close()
			sys.exit()

# start server
server = socket.socket()
# user = subprocess.run(['whoami'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\\')[-1]
# print (user)
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
