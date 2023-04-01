"""
7) Создать вручную и заполнить несколькими строками текстовый файл, в котором
каждая строка должна содержать данные о фирме: название, форма собственности,
выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее
в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
from pprint import pprint
import json

my_dict = {} # словарь для преобразования строк
profit_dict= {} # словарь прибыли
av_profit_dict = {} # словарь со средней прибылью
count = 0 # счетчик фирм

final_list = []

PATH = '/Users/arseniyblinov/Desktop/Py_test_folder/'

with open(file=PATH+'file_task_7.txt', encoding='UTF-8') as file:
    for line in file:
        count += 1
        correct_line = line.split()
        # print(correct_line)
        my_dict[correct_line[0]] = correct_line[1:]
        for value in my_dict.values():
            a = int(value[1]) - int(value[2])
            profit_dict[correct_line[0]] = a

    l = sum([x for x in profit_dict.values() if x > 0]) / count # (!!!!)
    av_profit_dict["average_profit"] = l
    # print(av_profit_dict)
final_list.append(profit_dict)
final_list.append(av_profit_dict)
pprint(final_list)

json_obj = json.dumps(final_list)
with open(file=PATH+'json_obj.json', mode='w', encoding='UTF-8') as file:
    file.write(json_obj)
















    # print(my_dict)



