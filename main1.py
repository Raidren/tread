#1. Записывает в файл большое количество значений и посчитать время выполнения:
import time
start_time = time.time()
with open("text.txt",'w') as f:
    for i in range (1000000):
        f.write('wefted45fgf')
print('Время выполнения записи значений в файл: ',(time.time() - (start_time)))