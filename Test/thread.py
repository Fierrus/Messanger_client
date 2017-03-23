from threading import Thread
from time import sleep
flag = 0
class MyThread(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		global flag
		for i in range(20):
			print ('Значение', flag)
			flag+=1
			sleep(0.222)

def smth():
	k=0
	while k<50:
		print("Somemthing")
		k+=1
b = MyThread()
b.setDaemon(True)
b.start()
smth()
