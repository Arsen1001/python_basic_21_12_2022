"""
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
 русские. Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {}
PATH = '/Users/arseniyblinov/Desktop/Py_test_folder/'
with open(file=PATH+'file_task_4.txt', encoding='UTF-8') as file:
    for line in file:
        correct_line = line.split(' - ')
        my_dict[correct_line[0]] = correct_line[1].strip()
        # print(my_dict)
right_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
#right_dict = dict(zip(right_list, list(my_dict.values())))
for key in my_dict:
    print(right_dict[key])


with open(PATH+'new_file_task_4.txt', 'w') as f:
    for key, value in my_dict.items():
        f.write(f'{right_dict[key]} - {value}\n')





