"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""
user_input = input('Введите три числа через пробел:\n').split()
user_input[:] = list(map(int, user_input)) #привел к интам

def my_func(a, b, c):
    result = sum((a, b, c)) - min(a, b, c) #сумма работает только так - в двойных скобках
    return result
tilt = my_func(*user_input)
print(tilt)



