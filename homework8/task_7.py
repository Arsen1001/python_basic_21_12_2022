"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу
проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        if self.imaginary_part >= 0:
            return f"{self.real_part} + {self.imaginary_part}i"
        else:
            return f"{self.real_part} - {-self.imaginary_part}i"

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary = self.imaginary_part + other.imaginary_part
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return ComplexNumber(real, imaginary)


c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, -1)
sum_result = c1 + c2
print(f"result: {sum_result}")
mul_result = c1 * c2
print(f"result: {mul_result}")