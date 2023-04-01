"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.
"""
import os
from pprint import pprint
file_path = os.path.join(os.path)
PATH = '/Users/arseniyblinov/Desktop/Py_test_folder'
with open(file=PATH+'test_text_file.txt', encoding='UTF-8') as file:
    lines = 0
    words_in_line = {}
    # print(type(file))
    for line in file:
        lines += 1
        # words += len(line.split())
        k = f'кол-во слов в {str(lines)}-й строке'
        words_in_line[k] = len(line.split())




    print("Колличество строк:", lines)
    pprint(words_in_line)


# test_data = [f'{idx} - {len(line.split())}' for idx, itm in enumerate(file)]