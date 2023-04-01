"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
def person_data(name, surname, date, city, mail, phone):
    print(f'Имя: {name}, Фамилия: {surname}, год рождения: {date}, город проживания: {city}, email: {mail}, телефон: {phone}')
person_data(name='Валера', surname='Блинов', date='1985', city='Мoscow', mail='mail', phone='89859626294')

# person_feature = ['name', 'surname', 'age', 'gender']
#
# person_dict = {}
# for feature in person_feature:
#     value = input(f'Введите {feature}: ')
#     person_dict[feature] = value
#     print(person_dict)
#
# person_data(**person_dict)
#
# person_data(name='Валера', surname='Блинов', date='1985', city='Мoscow', mail='mail', phone='89859626294')

