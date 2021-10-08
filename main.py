import multiprocessing
from multiprocessing import Process

import time
start_time = time.time()
f = open('text.txt', 'r')
f1 = open('text1.txt', 'w')
def reader_writer():
            for i in f:
                f1.write(i)
if __name__ == '__main__':
    multiprocessing.freeze_support()
    for i in range(6):
        multiprocessing.Process(target=reader_writer).start()
    print('Время выполнения записи значений в файл: ',(time.time() - (start_time)))