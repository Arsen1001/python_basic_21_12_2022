while True:
    user_time_input = input('Введите время в секундах: ')
    if user_time_input.isdigit():
        user_time_input = int(user_time_input)
        break
    print('Время вводится числами')

var_hours = user_time_input // 3600
var_minutes = (user_time_input % 3600) // 60
var_seconds = (user_time_input % 3600) % 60

right_time = f'{var_hours:>02}:{var_minutes:>02}:{var_seconds:>02}'
print(right_time)
