from multiprocessing import Process
from threading import Thread
import time
start_time = time.time()
def writer():
    with open("test12.txt", 'w') as fout:
        for i in range(500000):
            fout.write('1fjgkdfjgkdds')
def Tread():
    t1 = Thread(writer())
    t1.start()
    t1.join()
Tread(),print((time.time() - start_time))
def notTread():
    with open('test12.txt','w') as fout:
        for i in range (1000000):
            fout.write('1fsdfsdfsd')
notTread(),print((time.time() - (start_time)))

if __name__ == '__main__':
    proc = Process(target=writer())
    proc.start()
print((time.time() - (start_time)))
#Выполнение через потоки выходят куда эффективнее, чем без них