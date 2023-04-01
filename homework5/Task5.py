"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
 выводить ее на экран.
"""
import random
PATH = '/Users/arseniyblinov/Desktop/Py_test_folder/'
with open(file=PATH+'file_task_5.txt', mode='w', encoding='UTF-8') as file:
    for i in range(1, 11):
        file.write(str(random.randint(0, 9)) + ' ')

with open(file=PATH+'file_task_5.txt', encoding='UTF-8') as file_1:
    data = file_1.readline().split()
    print(data)
    data_1 = [int(itm) for itm in data]
    data_2 = list(map(int, data))
    print(data_1, data_2, sum(data_1))