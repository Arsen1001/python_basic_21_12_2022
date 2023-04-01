"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.Обратите
 внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
  предусмотреть условие его завершения.
"""
import sys
from itertools import cycle, count

def my_sequence(start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)

def my_cycle_func(my_list, quantity):
    c = 0
    iter = cycle(my_list)
    while c < quantity:
        print(next(iter))
        c += 1

ask = {
    'count': my_sequence,
    'cycle': my_cycle_func,
}

_, func_name, a, b, *__ = sys.argv
#_, func_name, *args = sys.argv

print(ask[func_name](str(a), int(b)))
