import socket
import threading
from time import sleep



class socket_thread:
	def __call__(self):
		while a:
			print('I am running')
			self.data = soc.recv(1024)
			self.data = self.data.decode('utf-8')
			if self.data == 'PING':
				soc.send(b'PONG')
				sleep(60)
			else:
				message_r = self.data
			print('Server said ', self.data)
			sleep(1)





if __name__ == '__main__':
	a=1
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_adress = ('localhost',10080)
	try:
		soc.connect((server_adress))
		sc_listen = socket_thread()
		t = threading.Thread(target=sc_listen)
		t.start()
	except ConnectionRefusedError:
		print('Server is down or address is incorrect')
	sleep(10)
	a=0
	soc.send(b'STOP')
	soc.close()

