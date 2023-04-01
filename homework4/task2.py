"""
2) Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

my_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# print([my_numbers[idx] for idx in range(1, len(my_numbers)) if my_numbers[idx] > my_numbers[idx - 1]])


def test_iter(*args):
    prev = -float('inf')
    for num in args:
        if num > prev:
            yield num
        prev = num

#if __name__ == '__main__':
print(list(test_iter(*my_numbers)))