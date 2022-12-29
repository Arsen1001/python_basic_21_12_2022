# PEP8

"""int - Это целое число
float - Это дробное число
str - это строка
"""


catalog_id_1 = 14  #это комментарий
catalog_id_2 = 15
my_float = 12.134
my_str1 = 'это строка 1'
my_str2 = "Это тоже строка 2"
my_str3 = """то строка из
множества 
строк"""

my_str4 = 'Нужно выделить "ТЕРМИН"'
my_str5 = "Нужно выделить \"ТЕРМИН\""

print(my_str4, my_float)

# age = 17
#
# if not age >= 18:
#     print('Доступ запрещен')

while True:
    age = input('введите возраст\n')
    if age.isdigit():
        age = int(age)
        break
    print('возраст должен быть числом')

if age >= 18:
    print('Доступ разрешен во все разделы включая XXX')
elif age >= 16:
    print('Доступ разрешен во все разделы')
elif age >= 8:
    print('Доступ разрешен в раздел мультики')
else:
    print('Доступ запрещен')



