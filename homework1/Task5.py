revenue = int(input('Введите сумму выручки '))
costs = int(input('Введите сумму издержек '))

if revenue < costs:
    print('Фирма работает в убыток!')
elif revenue == costs:
    print('Фирма работает в ноль!')
else:
#elif revenue > costs:
    print('Фирма работает в прибыль!!!')
    profitability = (revenue / costs) * 100
    print('Рентабельность составляет', profitability, '%')
    num_emp = int(input('Введите количество сотрудников '))
    profit_per_emp = int((revenue - costs) / num_emp)
    print('Прибыль фирмы в расчете на одного сотрудника составляет', profit_per_emp)






