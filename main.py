import multiprocessing
from multiprocessing import Process
from threading import *
import time
f = open('text.txt', 'r')
f1 = open('text1.txt', 'w')
start_time = time.time()
def reader_writer3():
    for i in f:
        f1.write(i)
def reader_writer2():
    m = 1
    for i in range (10000000):
        m*=3

def reader_writer():
    m = 10000000
    for i in range(10000000):
        m -= 2
t1 = Thread(target = reader_writer3())
t1.start()
t1.join()
print('Время выполнения записи значений в файл: ',(time.time() - (start_time)))
if __name__ == '__main__':
    start_time = time.time()
    multiprocessing.freeze_support()
    for i in range (12):
        multiprocessing.Process(target=reader_writer3()).start()
    print('Время выполнения записи значений в файл: ',(time.time() - (start_time)))
