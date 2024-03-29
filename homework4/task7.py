"""
7) Реализовать генератор с помощью функции с ключевым словом yield,
 создающим очередное значение. При вызове функции должен создаваться
 объект-генератор. Функция должна вызываться следующим образом:
 for el in fact(n).Функция отвечает за получение факториала числа,
  а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

def fact():
    prev = 1
    result = 1
    while True:
        yield result
        prev += 1
        result *= prev

def rec_fact(n):
    if n == 1:
        return n
    else:
        return n*rec_fact(n-1)

print(rec_fact(500))

for idx, itm in enumerate(fact(), 0):
    print(idx, itm)
    if idx == 1:

        break
