"""
5) Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных
пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной
сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если
 специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
 полученной ранее сумме и после этого завершить программу.
"""
def my_func():
    result = 0
    button = True
    while button == True:
        r = input('Введите числа через пробел:\n').split()
        for el in r:
            if el == 'q':
                button = False
                break
            el = int(el)
            result = result + el
        print(result)
    return result

m = my_func()
print(m)







