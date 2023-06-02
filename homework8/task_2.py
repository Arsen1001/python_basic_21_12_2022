"""
2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = float(input("Input dividend: "))
divisor = float(input("Input divisor: "))

try:
    if divisor == 0:
        raise MyError('Division by zero!')
except MyError as err:
    print(err)
else:
    print(dividend / divisor)
