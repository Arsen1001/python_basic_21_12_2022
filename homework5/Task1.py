"""
1) Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

text_file = input('file name:  ')
with open(text_file, 'w') as file:
    while True:
        data = input('insert data:  ')
        if data == '':
            break
        file.write(f'{data}\n')

