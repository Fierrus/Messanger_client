import socket
import threading
from time import sleep


class socket_thread:  # Создание класса для использования как потока
    def __call__(self):
        i = 0
        while a:
            print('I am running')
            self.data = soc.recv(1024)  # Прием сокетом 1024 байт
            self.data = self.data.decode('utf-8')  # Декодирование из байт в utf-8
            if self.data == 'PING':
                soc.send(b'PONG')
            else:
                message_r = self.data  # В случае если это полезное сообщение, оно присваивается переменной
            print('Server said ', self.data)
            sleep(1)


if __name__ == '__main__':
    i = 0


    def start_socket_thread(flag):
        global i
        if flag in ('y', ''):
            a = 1
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Параметры семейств сокетов
            server_adress = ('localhost', 10080)
            try:  # Использование эксепшенов себе на пользу
                soc.connect((server_adress))
                sc_listen = socket_thread()
                t = threading.Thread(target=sc_listen)
                t.start()
            except ConnectionRefusedError:
                if i == 10:
                    print('Time is out')
                    pass
                else:
                    i += 1
                    print('Server is down or address is incorrect, next try within 5 seconds ({} of 10)'.format(i))
                    sleep(5)
                    start_socket_thread('')


        elif flag == 'n':
            pass
        else:
            print('Err')


    start_socket_thread(input('Start socket y/n?'))
    # sleep(10)
    # a=0
    # soc.send(b'STOP')	#Комманда серверу на закрытие сокета
    # soc.close()
