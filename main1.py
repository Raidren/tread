#запись с помощью одного потока:
import time
start_time = time.time()
def calc():

    m = 0
    for i in range(0,30000000):
        m+=1
    print(m)
calc()
print('Время выполнения записи значений в файл: ',(time.time() - (start_time)))
