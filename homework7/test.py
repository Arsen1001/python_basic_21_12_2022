# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#     def __del__(self):
#         print(f"Deleting object {self.param} of MyClass class")
#
#
# mc = MyClass("text")
# del mc
# print(1)

# class MyClass:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#
#     def __add__(self, other):
#         return MyClass(self.width + other.width, self.height + other.height)
#
#     def __str__(self):
#         return f"Объект с параметрами ({self.width}, {self.height})"
#
# mc_1 = MyClass(10, 20)
# mc_2 = MyClass(30, 40)
# print(mc_1 + mc_2)


# class MyClass:
#     def __setattr__(self, attr, value):
#         if attr == "width":
#             self.__dict__[attr] = value
#             print(f"Attribute {attr} is {value}")
#         else:
#             print(f"Attribute {attr} is invalid")
#
# mc = MyClass()
# mc.width = 40

# class Class1:
#     def __init__(self, param):
#         self.param = param
#
#     def __str__(self):
#         return str(self.param)
#
#
# class Class2:
#     def __init__(self, *args):
#         self.my_list = []
#         for el in args:
#             self.my_list.append(Class1(el))
#
#     def __getitem__(self, index):
#         return self.my_list[index]
#
#
# my_obj = Class2(10, True, "text", 155, 5.6, None)
# print(my_obj[5])

# class Factorial:
#     def __init__(self):
#         self.cache = {}
#     def __call__(self, n):
#         if n not in self.cache:
#             if n == 0:
#                 self.cache[n] = 1
#             else:
#                 self.cache[n] = n * self.__call__(n-1)
#         return self.cache[n]
#
# fact = Factorial()
#
# for i in range(10):
#     print(f"{i}! = {fact(i)}")

# class MyClass:
#     def __init__(self, val):
#         self.val = val
#
#     def __iadd__(self, other):
#         self.val += other
#         return self
#
# mc = MyClass(100)
# print(mc.val)
# mc += 300
# print(mc.val)

# from abc import ABC, abstractmethod
#
# class MyAbstractClass(ABC):
#     @abstractmethod
#     def my_method_1(self):
#         pass
#     @abstractmethod
#     def my_method_2(self):
#         pass
#
# class MyClass(MyAbstractClass):
#     def my_method_1(self):
#         print("My_method_1")
#
#     def my_method_2(self):
#         print("My_method_2")
#
# mc = MyClass()
# mc.my_method_1()

# class Iterator:
#     def __init__(self, start=0):
#         self.i = start
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
# class IterObj:
#     def __init__(self, start=0):
#         self.start = start - 1
#     def __iter__(self):
#         return Iterator(self.start)
#
#
# obj = IterObj(start=2)
# for el in obj:
#     print(el)

# class MyClass:
#     def __init__(self, param_1, param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#
#     @property
#     def my_method(self):
#         return f"Parameters passed to the Class:" \
#             f" {self.param_1}, {self.param_2}"
#
# mc = MyClass("text_1", "text_2")
# print(mc.param_1)
# print(mc.param_2)
#
# print(mc.my_method)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
print(p1)
format(p1)