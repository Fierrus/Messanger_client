import socket
from time import sleep
import logging
#logging.basicConfig(level = logging.DEBUG)

HOST = ''  # адрес хоста (сервера) пустой означает использование любого доступного адреса
PORT = 10080  # номер порта на котором работает сервер (от 0 до 65525, порты до 1024 зарезервированы для системы, порты TCP и UDP не пересекаются)
BUFSIZ = 1024  # размер буфера 1Кбайт
ADDR = (HOST, PORT)  # адрес сервера
 
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #создаем сокет сервера
tcpSerSock.bind(ADDR)  # связываем сокет с адресом
tcpSerSock.listen(1)  # устанавливаем максимальное число клиентов одновременно обслуживаемых
 
while True:  # бесконечный цикл сервера
	logging.debug('Waiting for client...')
	tcpCliSock, addr = tcpSerSock.accept()  # ждем клиента, при соединении .accept() вернет имя сокета клиента и его адрес (создаст временный сокет tcpCliSock)
	logging.debug('Connected from: {}'.format(addr))
	while True:  # цикл связи
		tcpCliSock.send(b'PING')
		data = tcpCliSock.recv(BUFSIZ)
		if data.decode('utf-8') == 'PONG':
			logging.debug('Client is OK')
		if not data:
			break  # разрываем связь если данных нет
		sleep(60)
	tcpCliSock.close()  # закрываем сеанс (сокет) с клиентом    
tcpSerSock.close()  # закрытие сокета сервера