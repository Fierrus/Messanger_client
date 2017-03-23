import threading
from time import sleep

class A:
    def __call__(self, count=10, sleep_time=0.1):
        for i in range(count):
            print('Working class A, i=%s' % i)
            sleep(sleep_time)


class B:
    def __call__(self, count=10, sleep_time=0.1):
        for i in range(count):
            print('Working class B, i=%s' % i)
            sleep(sleep_time)



if __name__ == '__main__':
    a = A()
    b = B()

    t1 = threading.Thread(target=a, kwargs={'sleep_time': 0.1})
    t2 = threading.Thread(target=b, args=(12,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()