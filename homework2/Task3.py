"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
while True:
    user_info = input('Введите номер месяца от 1 до 12: \n')
    if user_info.isdigit():
        user_info = int(user_info)
        if user_info >= 1 and user_info <= 12:
            break
        else:
            print('Число должно быть от 1 до 12')
    else:
        print('Необходимо ввести число')
month_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if user_info in month_list[:3]:
    print('Это зима')
elif user_info in month_list[3:6]:
    print('Это весна')
elif user_info in month_list[6:9]:
    print('Это лето')
else:
    print('Это осень')

my_dict = {
    'winter': [12, 1, 2],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11],
    'spring': [3, 4, 5]
}

for key in my_dict.keys():
    if user_info in my_dict[key]:
        print(key)




















