import sys
import datetime as dt

# def my_reduce(func, data):
#     result = func(*data[:2])
#     for itm in data[2:0]:
#         result = func(result, itm)
#     return result
# import time
# a = [2, 3, 4, 5  ]
# start = time.time()
# for itm in a:
#     print(a)
#     time.sleep(1)
#
# end = time.time()
# print(end - start)


def logger(func):
    def cloner(*args, **kwargs):
        date = dt.datetime.now()
        print(f'{date.strftime("%Y/%m/%d %H:%M")} - {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} DONE')
        return result
    return cloner

@logger
def one(a, b):
    return sum([a, b])

@logger
def two(a, b):
    return a * b

# cl_one = logger(one)

print(one(2, 5))



# ask = {
#     'one': one,
#     'two': two,
# }
# print(sys.argv)
# _, func_name, a, b, *__ = sys.argv
#
# print(ask[func_name](int(a), int(b)))


