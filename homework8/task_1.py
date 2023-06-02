"""
1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import time


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def extract_numbers(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return day, month, year

    @staticmethod
    def validate_date(date_str):
        try:
            time.strptime(date_str, '%d-%m-%Y')
            print("Date is correct.")
        except:
            print("Date is incorrect!!!")


date_str = "29-02-2023"
my_date = Date(date_str)
day, month, year = Date.extract_numbers(date_str)
print(f"Day: {day}, Month: {month}, Year: {year}")
is_valid = Date.validate_date(date_str)
# print(is_valid)
# if is_valid:
#     print("date is correct.")
# else:
#     print("Date is incorrect.")

