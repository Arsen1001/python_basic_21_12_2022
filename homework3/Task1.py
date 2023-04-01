"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_division(a, b):
    result = a / b
    return int(result) if a%b == 0 else result

while True:
    user_dividend = int(input('введите делимое:  '))
    user_divider = int(input('введите делитель:  '))

    try:
        print(my_division(user_dividend, user_divider))
        break
    except ZeroDivisionError:
        print('На ноль делить нельзя!!!')
        continue

# return None



