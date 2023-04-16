"""
Реализуйте базовый класс Car.У данного класса должны быть следующие атрибуты: speed,
 color,name,is_police (булево). А также методы: go,stop,turn(direction),которые должны
 сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
 дочерних классов: TownCar,SportCar,WorkCar,PoliceCar.Добавьте в базовый класс метод
 show_speed, который должен показывать текущую скорость автомобиля. Для классов
 TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
 (TownCar)и 40 (WorkCar)должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} started moving'

    def stop(self):
        return f'{self.name} stopped'

    def turn_right(self):
        return f'{self.name} turns right'

    def turn_left(self):
        return f'{self.name} turns left'

    def show_speed(self):
        return f'{self.name} current speed is {self.speed} kph'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Attention! Speed of {self.name} exceeded the speed limit!!!'
        else:
            return f'Speed of {self.name} is ok'

    def police(self):
        if self.is_police:
            return f'{self.name} is a police car'
        else:
            return f'{self.name} is not a police car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is a police car'
        else:
            return f'{self.name} is not a police car'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Attention! Speed of {self.name} exceeded the speed limit!!!'
        else:
            return f'Speed of {self.name} is ok'

    def police(self):
        if self.is_police:
            return f'{self.name} is a police car'
        else:
            return f'{self.name} is not a police car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is a police car'
        else:
            return f'{self.name} is not a police car'



peugeot_partner = SportCar(150, 'White', 'Peugeot', False)
fiat_500 = TownCar(40, 'Red', 'Fiat_500', False)
toyota_prius = WorkCar(85, 'Blue', 'Toyota_prius', False)
skoda_octavia = PoliceCar(110, 'Green',  'Skoda', True)


print(toyota_prius.turn_left())
print(fiat_500.show_speed())
print(toyota_prius.show_speed())
print(skoda_octavia.police())
print(fiat_500.police())
print(peugeot_partner.color)
print(peugeot_partner.is_police)

