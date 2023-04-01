"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
 учебный предмет и наличие лекционных, практических и лабораторных занятий по
 этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
 были все типы занятий. Сформировать словарь, содержащий название предмета и общее
 количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика:      30(л) — 10(лаб)
Физкультура:   — 30(пр) —

Пример словаря:  {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re

my_dict = {}
new_dict = {}
PATH = '/Users/arseniyblinov/Desktop/Py_test_folder/'
with open(file=PATH+'file_task_6.txt', encoding='UTF-8') as file:
    for line in file:
        correct_line = line.split(': ')
        my_dict[correct_line[0]] = correct_line[1]
    # print(my_dict)
        a = correct_line[1]
        nums = re.findall(r'\d+', a)
        nums = [int(i) for i in nums]
        # print(sum(nums))
        new_dict[correct_line[0]] = sum(nums)
    print(new_dict)
