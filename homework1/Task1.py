my_first_var = 20
my_second_var = 23
print(my_first_var)
print(my_first_var, my_second_var)
print(my_first_var + my_second_var)
type(my_second_var)
print(type(my_second_var))



while True:
    user_info = input('Введите своё имя\n')
    if not user_info.isdigit():
        user_info = str(user_info)
        break
    print('Имя вводится буквами')

print(user_info)

