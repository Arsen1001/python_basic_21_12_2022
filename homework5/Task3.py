"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
"""
from pprint import pprint

my_dict = {}
emp_list = []
all_emp = 0
PATH = '/Users/arseniyblinov/Desktop/Py_test_folder'
with open(file=PATH+'salary_data.txt', encoding='UTF-8') as file:
    for line in file:
        all_emp += 1
        employee_salary = line.split()
        my_dict[employee_salary[0]] = float(employee_salary[1])
for key, value in my_dict.items():
    if float(value) < 15000:
        emp_list.append(key)
average_salary = round(sum(my_dict.values()) / all_emp)
print(average_salary)

pprint(emp_list)
