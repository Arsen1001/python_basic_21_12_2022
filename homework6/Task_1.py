"""
1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго
(желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение
между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
Родительский метод класса Transport Родительский метод класса Auto Родительский метод класса Bus

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

# from time import sleep
# from datetime import datetime
#
#
# class TrafficLight:
#     """ Класс TrafficLight, который переключает цвета при запуске метода runnnig """
#     __values = {'red': 7, 'yellow': 2, 'green': 9}
#     __color = ()
#
#     def running(self):
#         """ метод для переключения светофора"""
#         for color, switch_time in self.__values.items():
#             self.__color = color
#             start_point = datetime.now()
#
#             print(f"TrafficLight turns '{self.__color}' light "
#                   f"on {switch_time} seconds")
#
#             sleep(switch_time)
#
# a = TrafficLight()
# a.running()


from time import sleep


class TrafficLight:
    """ Все просто: класс светофор и три цвета в нем))"""
    __color = ['Red light', 'Yellow light', 'Green light']

    def running(self):
        i = 0
        while i < 3:
            print(f'TrafficLight switches to:\n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(9)
            i += 1


a = TrafficLight()
a.running()






