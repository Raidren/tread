#запись с помощью 6 потоков:
import time
import multiprocessing
def calc():
    m = 0
    for i in range(0,30000000):
        m+=1
    print(m)
def calc1():
    m = 0
    for i in range(0,30000000):
        m+=1
    print(m)
def calc2():
    m = 0
    for i in range(0,30000000):
        m+=1
    print(m)
def calc3():
    m = 0
    for i in range(0,30000000):
        m+=1
    print(m)
def calc4():
    m = 0
    for i in range(0,30000000):
        m+=1
    print(m)
def calc5():
    m = 0
    for i in range(0,30000000):
        m+=1
    print(m)
if __name__ == '__main__':
    start_time = time.time()
    multiprocessing.freeze_support()
    p = multiprocessing.Process(target=calc)

    p1 = multiprocessing.Process(target=calc1)

    p2 = multiprocessing.Process(target=calc2)

    p3 = multiprocessing.Process(target=calc3)

    p4 = multiprocessing.Process(target=calc4)

    p5 = multiprocessing.Process(target=calc5)
    p.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p.join()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    print((time.time() - (start_time)))

