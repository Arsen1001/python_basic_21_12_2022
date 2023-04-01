num = int(input('Введите целое положительное число  '))
max = num % 10
while num >= 1:
    num //= 10
    if num % 10 > max:
        max = num % 10
print('Максимальное число', max)

