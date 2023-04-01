def my_sum(a: float, b: float, c:float=22.0) -> float:
    """Функция-сумматор двух элементов
    :param a: float
    :param b: float
    :return: float
    """
a = [2, 3, 4, 5, 6]

def my_pow(x):
    return x ** 2

def my_map(func, iter_obj):
    result = []
    for itm in iter_obj:
        result.append(func(itm))
    return result

b = my_map(my_pow, a)
print(b)

