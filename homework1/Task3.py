while True:
    user_input = input('Введите число от 1 до 9 ')
    if user_input.isdigit():
        user_input = int(user_input)
        break
    print('Введите именно число')

a = str(user_input) + str(user_input)
b = a + str(user_input)
sum = int(b) + int(a) + user_input
print(sum)
# result = int(user_input) + int(user_input*2) + int(user_input*3)
# print(result)

