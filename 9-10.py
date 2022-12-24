# lst = [1, 2, 3, 4]
# s = 'hello'
#
#  for i in lst:
#      print(i)
# print(iter(lst))
# print(iter(s))
#
# list_iterator = iter(lst)
# print(list_iterator)
# print(list_iterator.__next__())
# print(list_iterator.__next__())
# print(list_iterator.__next__())
# print(list_iterator.__next__())
# print(len(a))
# print(name)
# print(12 + 15)
# time = 0
# a = 125
#
# try:
#     print(10 + 15)
# print(5 / 0.5)
# if time != None:
#     print(len('125'))
#     print(time)


# except (TypeError, ZeroDivisionError, NameError):
#     print("Общая ошибка!")
#     a = str(a)
#     print(len(a))
# else:
#     print('ELSE')
# finally:
#     print('FINAly')
# def checker(var):
#     if type(var) != str:
#         raise TypeError(f'Мы не будем работать с {var}')
#     else:
#         return var
#
#
# print(checker('hello'))
# print(checker('125'))
# class BuildingError(Exception):
#     def __str__(self):
#         return 'Материала на дом не хватает'
#
#
# def checker(materials, limit_materials):
#     if materials < limit_materials:
#         raise BuildingError(materials)
#     else:
#         print('Материалов достаточно для постройки дома')
#
#
# checker(125, 300)\
# lst = [1, 2, 3, 4]
# s = 'hello'
#
#  for i in lst:
#      print(i)
# print(iter(lst))
# print(iter(s))
#
# list_iterator = iter(lst)
# print(type(list_iterator))
# print(list_iterator)
# print(list_iterator.__next__())
# print(list_iterator.__next__())
# print(list_iterator.__next__())
# print(list_iterator.__next__())

# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= self.end:
#             number = self.current
#             self.current += 1
#             return number
#         raise StopIteration
#
#
# my_range = MyRange(1, 10)
# for i in my_range:
#     print(i, end=' ')
# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count ** 2
#         count += 1
#
#
# c = count_up_to(150)
# print(c)
# for i in range(15):
#     print(c.__next__())
# def my_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator.__next__())
#         except StopIteration:
#             break
#
#
# my_for([1, 2, 3, 4])
# p = print
# p(10 + 5)
# def func():
#     return 2 + 2
# f = func
# print(f)
#
# print(f())
# def func()
#     age = 15
#     def my_func():
#         print(age)
#     return my_func
# f = func()
# f()
# print(age)
def first_func(value):
    name = value
    def second_func():
        print('Меня зовут', name)
    return  second_func
n = first_func('Олег')
n()