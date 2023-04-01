"""
4) Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
 возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
#
# x = 4
# y = -3
# def my_func(base, exp):
#     i = 1
#     result = 1
#     while i <= abs(exp):
#         result = result * base
#         i += 1
#     return 1 / result
# m = my_func(x, y)
# print(m)

def my_multip(x, y):
    result = 0
    for _ in range(y):
        result += x
    return result

def my_func(x: float, y: int):
    result = 1
    for _ in range(abs(y)):
        result = my_multip(result, x)
    return result if y > 0 else 1 / result






