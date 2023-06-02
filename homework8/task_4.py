"""
4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках
реализовать параметры, уникальные для каждого типа оргтехники.


5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.

6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""
class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if not isinstance(quantity, int):
            raise ValueError("Количество должно быть целым числом.")
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity


    def transfer_item(self, item, quantity, department):
        if not isinstance(quantity, int):
            raise ValueError("Количество должно быть целым числом.")
        if item in self.inventory:
            if quantity > self.inventory[item]:
                raise ValueError("Недостаточное количество оргтехники на складе.")
            self.inventory[item] -= quantity
            if self.inventory[item] == 0:
                del self.inventory[item]
            print(f"{quantity} единиц(ы) оргтехники {item} передано в {department}.")
        else:
            raise ValueError("Оргтехника отсутствует на складе.")

    def print_inventory(self):
        print("Инвентарь склада:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")


class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} (Цена: {self.price})"


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, is_color):
        super().__init__(brand, model, price)
        self.is_color = is_color

    def __str__(self):
        color_info = "Цветной" if self.is_color else "Черно-белый"
        return f"Принтер {super().__str__()}, {color_info}"


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, resolution):
        super().__init__(brand, model, price)
        self.resolution = resolution

    def __str__(self):
        return f"Сканер {super().__str__()}, Разрешение: {self.resolution} dpi"


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, price, speed):
        super().__init__(brand, model, price)
        self.speed = speed

    def __str__(self):
        return f"Ксерокс {super().__str__()}, Скорость: {self.speed} стр/мин"


printer = Printer("Epson", "L3150", 12000, True)
scanner = Scanner("Canon", "CanoScan LiDE 400", 5000, 4800)
xerox = Xerox("Xerox", "WorkCentre 3345", 20000, 33)

warehouse = Warehouse()

warehouse.add_item(printer, 5)
warehouse.add_item(scanner, 3)
warehouse.add_item(xerox, 2)

warehouse.print_inventory()

warehouse.transfer_item(printer, 2, "Отдел продаж")
warehouse.transfer_item(scanner, 1, "Отдел маркетинга")

warehouse.print_inventory()


