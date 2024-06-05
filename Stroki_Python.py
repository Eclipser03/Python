from __future__ import annotations
from pprint import pprint
from copy import deepcopy
from time import sleep

from pip._internal.cli.cmdoptions import python

# Интерактивное отображение работы питон
# https://pythontutor.com/

# интерактивное отображение алгоритмов
# https://www.cs.usfca.edu/~galles/visualization/Algorithms.html

# рисовать диаграммы
# https://app.diagrams.net/

# Отменить действие в vscode:
# CTRL+Z
# Вернуть отменённое действие в vscode:
# CTRL+Y
# Импортировать модуль объекта на котором стоит курсор в vscode:
# CTRL+. затем ENTER

# Интерактивная консоль Python в vscode, типо IDLE
# CTRL+SHIFT+P
# Ввести: "repl"
# И выбрать: "Python: Запустить REPL"
# либо SHIFT+ENTER

# Типы данных

# Изменяемые (mutable)
# print(type(   {1, 1, "a"}    )) # -> set Множество
# print(type(  {'a':1, 2: 'b'} )) # -> dict Словарь
# print(type( [1, 1, 'a']      )) # -> list Список
# from array import array
# ?print(type(  array("l", [1, 1, 2])  ))      # -> array Массив
# ?print(type(  bytearray(3)  ), bytearray(3)) # -> Массив байт

# Неизменяемые (not mutable)
# print(type( 'abc'        )) # -> str Строка
# print(type(  (1, 1, 'a') )) # -> tuple Кортеж
# print(type(  None        )) # -> NoneType Отсутствие данных
# print(type(  True        )) # -> bool Логическое значение
# print(type(  1           )) # -> int Целое число
# print(type(  1.4         )) # -> float Число с плавающей точкой
# from decimal import Decimal
# print(type(Decimal('1.4'))) # -> decimal Точное число с плавающей точкой
# ?print(type(  1 + 1j       )) # -> complex Комплексное число
# ?print(type( frozenset([1, 1, 'a'])  )) # -> frozenset неизменяемое множество
# ?print(type(  bytes(3)  ), bytes(3))     # -> Байт


# класс Decimal служит для более точной работы с дробными числами чем встроенный тип float
# print(Decimal('1.4') * Decimal('0.1'), 1.4 * 0.1)

# print(complex(2, 3j)) # создание комплексного числа

# Узнать айди объекта
# print(id('строка'))
# print(id([1,2,3]))

# узнать адресс в памяти в шестнадцатеричном формате
# print(hex(id('строка')))
# print(hex(id([1, 2, 3])))

# print(license())

# ?запустить Pyton код прямо в консоли:
# python -c 'for i in range(5):print(i)'

# ?memoryview позволяет коду Пайтон получать доступ к внутренним данным обьекта,
# который поддерживает буферный протокол, без необзодимости копирования.
# Это позволяет программе использовать меньше памяти и увеличивает скорость выполнения.
# ba = bytearray('ABC', 'utf-8')
# mv = memoryview(ba)
# print('memoryview:', mv)
# print('байт под нулевым индексом:', mv[0])
# print('байт строка в unicode представлении:', bytes(mv[0:2]))
# print('список байт:', list(mv[0:2]))
# print(f'до изменения с помощью memoryview: {ba!r}')
# mv[1] = 90
# ?print(f'после изменения с помощью memoryview: {ba!r}')



# ?print("52 =", bytes(52)) # Преобразует объект в неизменяемую строку байтов
# print("Привет Мир! =", bytes('Привет Мир!', encoding='utf-8'))

# ?метод fromhex у класса bytes может преобразовывать шестнадцатиричную последовательность чисел в байт-строку
# b = bytes.fromhex('31 4B CE A9')
# print(b)
# b = b.decode('utf8')
# print(b) # один кило ОМ


# print("52 =", bin(52)) # преобразует десятичное число в двоичную (бинарную) строку с префиксом '0b'
# print("52 =", bin(52))[2:]

# print(bin(52), int(bin(52), 2)) # Возвращает двоичное представление целого числа.
# print(oct(52), int(oct(52), 8)) # Возвращает восьмеричное представление целого числа.
# print(hex(52), int(hex(52), 16)) # Возвращает шестнадцатеричное представление целого числа


# ?дизассемблировать(отобразить) байт-код скомпилированной функции на языке ассемблера.
# from dis import dis
# def func(a, b):
#     return a + b
# dis(func)


# Относительный импорт:
# from .filename import myfunc # импортировать функцию myfunc из файла filename который находится на одном уровне с файлом из котрого происходит импорт
# from ..filename import myfunc # импортировать функцию myfunc из файла filename который находится на уровень выше чем файл из котрого происходит импорт
# from ...filename import myfunc # импортировать функцию myfunc из файла filename который находится на два уровня выше чем файл из котрого происходит импорт
# и т.д.
# Абсолютный импорт:
# from foldername.filename import myfunc


# список изменяемый объект (id объекта всегда один и тот же)
# x = [1, 2, 3]
# print(id(x), x)
# x[2] = 6
# print(id(x), x)
# x.append(8)
# print(id(x), x)

# строка неизменяемый объект
# (но добавление нового элемента не меняет id в отличие от изменения существующего элемента)
# так работает в python <= 3.8, в python 3.11 например, id изменяется при любом раскладе
# y = '123'
# print(id(y), y)
# y = y[:2] + '6'
# print(id(y), y)
# y += '8'
# print(id(y), y)

# Области видимости (Пространства имен)
# built-in # встроенные функции в интерпретаторе, для их использования не надо импортировать модули, а так же операторы (зарезервированные слова).
# global   # объекты доступные в пространстве имён модуля.
# local    # объекты доступные внутри функции.
# nonlocal # делает доступной переменную в блоке внешней функции (обёртки).

# def a():
#     ''' документация функции "a" '''
# class b:
#     ''' документация класса "b" '''
#     def MY_METHOD_MY_METHOD_MY_METHOD_MY_METHOD_MY_METHOD():
#         pass
# print('Имя объекта:', a.__name__, b.__name__) # позволяет посмотреть имя объекта
# print('Документация объекта:', a.__doc__, b.__doc__) # позволяет посмотреть документацию объекта
# print(help(a)) # позволяет посмотреть документацию объекта
# print(globals()) # возвращает словарь с доступными объектами в пространстве имён текущего модуля

import math
#pprint(dir(math)) # позволяет узнать какие объекты содержаться в функции/модуле (без аргументов в текущем пространстве имён модуля)
#def func(): pass
# получить список атрибутов объекта
#pprint(dir(func))
#pprint(func.__dir__())

# ?print(__name__) # узнать какое состояние имеет переменная __name__ в текущем пространстве имён модуля

# ?pprint(__builtins__.__dict__)
# ?print(str.__dict__)
# ?print(vars(str))

# ?print(callable(len), callable('строка')) # проверяем является ли объект вызываемым

# ?print(locals()) # возвращает словарь с переменными и их значениями из текущей локальной области видимости в виде словаря
# ?print(vars()) # без аргумента работает как locals

# узнать инфу о функции
# def func(a: str, b: int) -> list:
#     c = 2; d = 'Hello, World!'
#     return c, d
# print(func.__code__.co_argcount)
# ?print(func.__code__.co_consts)
# ?print(func.__code__.co_varnames)

# ?Узнать родителей в иерархическом порядке у объекта
# class A: pass
# class B(A): pass
# print(B.mro())

# принадлежность объекта к конкретному классу можно проверить функцией isinstance
# 1арг. объект который мы хотим проверить, 2арг. класс (или кортеж классов) к которому они должны принадлежать, вернёт True/False
# print(isinstance('строка', int))
# print(isinstance('строка', str))
# # либо тоже самое с помощью класса type()
# print(type('строка') == int)
# print(type('строка') == str)

# принадлежность объекта к конкретному субклассу можно проверить функцией issubclass
# 1арг. тип к которому должен принадлежать объект который мы хотим проверить, 2арг. тип (или кортеж типов) проверяемых объектов, вернёт True/False
# print(issubclass(int, type(72)))
# print(issubclass(int, type("Hello World!")))
# print(issubclass(str, type("Hello World!")))

# class Obj: myattr = 7
# # получить атрибут у объекта
# print('getattr:', getattr(Obj, 'myattr')) # obj, name
# # установить атрибут для объекта
# setattr(Obj, 'myattr2', 'Hello World!') # obj, name, value
# # удалить атрибут у объекта
# delattr(Obj, 'myattr') # obj, name
# # проверить есть ли атрибут у объекта, возвращает True/False
# print('hasattr:', hasattr(Obj, 'myattr2')) # obj, name
# print('hasattr:', hasattr(Obj, 'myattr'))

# функция type определяет тип данных
# if type(True) == bool :
# #     print('bool')
# # if type(1) == int :
# #     print('int')

# Класс bool преобразует числовое значение в истину или ложь
# если число 0 значит ложь, остальные числа - истина
# print(bool(11))
# print(bool(-11))
# print(bool(0))
# так же работает и со строками, только в качестве лжи применяется пустая строка
# print(bool('a'))
# print(bool(''))
# так же и с коллекциями
# print(bool([1, 2]))
# print(bool([]))

# умножение разных типов данных
# print(1*5)
# print('1'*5) # строка
# print([[]]*5) # список
# print((1,)*5) # кортеж
# print(True*5, 1*5) # булевые
# print(False*5, 0*5)

# булевые значения можно суммировать если они суммируются в integer object
#         1     1      0      1     0
# array = [True, True, False, True, False]
# int_count = 0
# for bool_value in array:
#     int_count += bool_value
# print(int_count, sum(array))

# print(hash('string')) # хэш можно найти только у неизменяемых типов данных
# print(hash([1, 2, 3])) # TypeError: unhashable type: 'list'
# если в кортеже будет находиться изменяемый тип данных
# он перестаёт иметь хэш, функция выбросит исключение TypeError
# print(hash((1, 2, '3', '4')))
# print(hash((1, 2, [3, 4])))
# Если объекты равны то их хэш тоже равен
# Но равные хэши не гарантируют на 100% равенство объекта
# Если хэши не равны то объекты точно не равны
# print(hash((1, 2)), hash((1, 2)))
# print(hash('Hello World!'), hash('Hello World!'))

# код можно писать в одну строку с помощью точки с запятой ';'
# a = 1; b = 2; c = [1,2]
# print(a,b,c)

# по умолчанию print разделяет аргументы одиночными пробелами
# но при помощи параметра sep можно указать другой разделитель
# print('a', 'b', 'c', sep='111')

# параметр end может склеивать принты вместе
# print('a', 'b', 'c', end=' ')
# print('d', 'e', 'f')

# ?читабельный вывод словарей с табуляцией
# import json
# print(json.dumps(словарь, indent=4, ensure_ascii=False))

# перевод числового значения int или float в строку с помощью метода str()
# a = 5
# b = 5.7
# c = 'Строка с числом ' + str(a) + str(b)
# print(c)

# функция input запрашивает данные для ввода и передаёт их в строке
# функция int переводит строковые значения(цифровые) в целые числа
# функция float переводит строковые значения(цифровые) в числа с плавающей точкой
# a = input("Введите число:\n")
# b = int(a) + 5
# b = float(a) + 5
# print(b)

# a = float(input("Введите число: "))
# b = float(input("Введите число: "))
# print("Результат:", a + b)
# print("Результат:" + str(a + b)) # объединение строки с числом

# # eval() может выполнить лишь выражение Python
# print(eval("1024 + 1024"))
# print(eval("sum([8, 16, 32])"))
# print(eval("min([1, 2, 3])"))
# print(eval("[i for i in range(5)]"))
# x, y = 7, 7
# print(eval("x != y")) # в eval можно передавать глобальные переменные
# print(eval("x != y", {"x": 7})) # в eval можно указать только определенные переменные в формате словаря которые должны попасть в функцию.

# # compile() можно использовать для предоставления объектов кода для eval() вместо обычных строк.
# code = compile('5+4', '<string>', 'eval')
# print(eval(code))
# # exec() может выполнить любой фрагмент кода Python
# exec('if 1 > 0: print("da, 1 bolshe 0")')

# простейший калькулятор с использованием функции eval

# while True: print(eval(input()))

# while True:
#     text = input()
#     try:
#         result = eval(text)
#         print("\033[A                             \033[A")
#         print(text, '=', result)
#     except Exception as exc:
#         print(exc)


# print(1)
# print(2)
# print(3)
# ?for _ in range(3):
#     sleep(1)
#     print("\033[A                             \033[A") # удаляет одну строку в консоли

# Операторы условий
# if
# elif
# else
# :
# pass # оператор заглушка, допустим что бы не писать print() или кавычки документации ''' '''
# ... # так же работает как заглушка
# del <объект> # оператор удаления объекта
# del(<объект>) # тоже самое только с указанием объекта для удаления в круглых скобках

# Логические операторы (имеют приоритет выполнения)
# not # первый
# and # второй
# or  # третий

# continue # оператор для работы с циклами, пропускает итерацию и начинает следующую с самого начала
# break # оператор для работы с циклами, останавливает цикл и выходит из тела цикла
# else # оператор в том числе и для работы с циклами, сработает только в том случае
# если цикл завершиться сам по себе, то есть выполнит все итерации



# print(chr(i) for i in range(1, 4))
# ?for char in (chr(i) for i in range(1, 4)):
#     print(char)


# добавить более одного элемента за итерацию используя collection comprehension
# можно с помощью вложенных циклов и тернарного оператора
# lst = [1, 0, 2, 3, 0, 4]
# res = [i for N in lst for i in ([N] if N else ['hello', 'World'])]
# print(res)


# выражение присваивания/моржовый оператор
# присваиваем b значение a ** 2
# и проверяем если b > 0
a = 4

# if (b := a ** 2) > 0:
#     print(f'Kvadrat {a} eto {b}')

# # без использование скобок в b присвоится True
# if b := a ** 2 > 0:
#     print(f'Квадрат {a} это {b}')

name = 'Arseniy Astafev'
x = False
#
# if (name := name.split()[-1]) and not x:
#     print(name)
# print(name)

# # без использования скобок в name присвоится True
# if name := name.split()[-1] and not x:
#     print(name)
# print(name)


# на самом деле оператор del удаляет не сам объект а ссылку на объект
# и в качестве побочного результата сборщик мусора должен удалить объект
# если на него более никто не ссылается
# from sys import getrefcount
# from weakref import finalize
# a = {1, 2}
# ender = finalize(a, lambda : print('Garbage Collector eat {1, 2} object'))
# print('refcount:', getrefcount(a), ' object alive?', ender.alive)
# b = a # теперь на объект {1, 2} ссылаются переменные "a" и "b"
# print('refcount:', getrefcount(a), ' object alive?', ender.alive)
# c = b # теперь на объект {1, 2} ссылаются переменные "a", "b", "c"
# print('refcount:', getrefcount(a), ' object alive?', ender.alive)
# del a # теперь на объект {1, 2} ссылаются переменные "b", "c"
# print('refcount:', getrefcount(c), ' object alive?', ender.alive)
# del b # теперь на объект {1, 2} ссылается только переменная "c"
# print('refcount:', getrefcount(c), ' object alive?', ender.alive)
# c = 'Hello World!' # теперь на объект {1, 2} более никто не ссылается и сборщик мусора может удалить объект
# print('             object alive?', ender.alive)


# конструкция math case позволяет проверять первый аргумент последовательности
# и записывать последующие в переменные
# message = ['BEEPER', 440, 3]
# message = ['LED', 77, '214', '251', '192']
# # message = ['NECK', 440]
# # message = ['UNKNOWN', 'abcdef']
# match message:
#     case ['BEEPER', frequency, times]:
#         print(1)
#     case ['NECK', angle]:
#         print(2)
#     case ['LED', ident, intensity]:
#         print(3)
#     # можно указывать охранное условие if на ряду с case
#     case ['LED', ident, red, green, blue] if int(green) < 255:
#         print(4)
#     case _:
#         print(5)

# phone = '162367721261'
# phone = '262367721261'
# phone = '362367721261'
# phone = '462367721261'
# match tuple(phone): # превращаем строку в коллекцию символов
#     case ['1', *rest]: # проверяем первый символ остальные помещаем в переменную rest
#         print(1)
#     case ['2', *rest]:
#         print(2)
#     case ['3' | '4', *rest]:
#         print(3,4)

# location = ['Shanghai', 'CN', 24.9, (31.1, 121.3)]
# match location:
#     # для переменных можно указывать алиасы
#     case [name as title, _, _, (lat, lon) as coord]:
#         print(title, coord)

# i = 0
# print('>>> IN')
# while i < 10:
#     i += 1
#     if i > 3 and not i > 6: # если i больше 3 и i не больше 6 тогда пропускаем итерацию
#         print('i =', i, 'continue')
#         continue
#     print('i =', i)
#     if i == 8:
#         print('i =', i, 'break')
#         break
# else:
#     print('сработал оператор else')
# print('>>> OUT')

# вместо двух указателей идущих на встречу друг другу можно использовать цикл
# N = 10
# for i in range(N):
#     print(i, N-i-1)

# Убираем повторяюзиеся элементы из списка с помощью цикла
# a = [1, 2, 3, 4, 32, 4, 5, 3, 5]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(a)
# print(b)

# сортировка строки по маленьким и большим буквам и не буквенным символам с помощью цикла
# s = 'h@lLo WOrld!'
# for i in s:
#     if i >= 'a' and i <= 'z':
#         print(i, 'small')
#     elif 'A' <= i <= 'Z':
#         print(i, 'big')
#     else:
#         print(i, 'не буквенный символ')

# подсчет кол-ва повторяющихся букв в строке с помощью циклов
# s = 'abczjhdf HG jgkfYGg jhgkdf 543 *(^($&*#'
# letters = [0] * 26
# print(ord('a'))
# for i in s.lower():
#     if i >= 'a' and i <= 'z':
#         number = ord(i) - 97
#         letters[number] += 1
# for i in range(26):
#     if letters[i] > 0:
#         print(chr(i + 97), letters[i])

# Операторы сравнений (Проверяют объекты на равенство их значений)
# ==
# <
# >
# <=
# >=
# !=

# построение диапазона с помощью операторов сравнений
# number = 4
# if 3 <= number <= 6:
# # if number >= 3 and number <= 6: # аналогичная запись
#     print('число в диапазоне от 3 до 6')

# операторы сравнения можно записывать в цепочке
# a, b, c, d = 1, 1, 1, 1
# if a == b == c == d:
#     print('все числа равны')

# оператор 'in' если часть объекта равна возвращает логическое значение True иначе False
# link1 = 'https://'
# link2 = 'https://#'
# link3 = 'https://www.youtube.com'
# print(link1 in link3) # True
# print(link2 in link3) # False

# оператор 'is' если объекты ссылаются на одну и туже ячейку в памяти то возвращает логическое значение True иначе False
# x = 'hi'
# y = 'hi'
# print(x is y) # True

# для слишком больших чисел выделяется отдельная область в памяти
# x = 31**25
# y = 31**25
# print(x, y, x is y) # True
# x = 31**26
# y = 31**26
# print(x, y, x is y) # False

# x = 32**21
# y = 32**21
# print(x, y, x is y) # True
# x = 32**25
# y = 32**25
# print(x, y, x is y) # False

# x = 25**25
# y = 25**25
# print(x, y, x is y) # True
# x = 26**26
# y = 26**26
# print(x, y, x is y) # False

# для списков выделяется отдельная область в памяти
# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]
# print(x is y) # True
# print(y is z) # False
# print(x is z) # False

# float('inf') считается самым большим числом в python, он действует как неограниченное верхнее значение для сравнения
# print(float('inf') > 99999**99999) # True
# float('-inf') #считается самым малым числом в python.
# print(float('-inf') < -9999999999) # True
# from math import inf
# print(inf == float('inf'))

# создать и проверить объект на NaN
# from math import isnan
# nan = float('nan')
# print(isnan(nan)) # True
# print(isnan(1.7)) # False

# Математические операторы (имеют приоритет выполнения)
# a = 10 + 5
# a = 10 - 5
# a = 10 * 5
# a = 19 / 5 # обычное деление, ответ = 3.8
# a = 19 // 5 # деление с отбросом остатка после точки (в числе 19 число 5 помещается 3 раза)

# Остаток от деления 19 % 7 в число 19 число семь помещается 2 раза, остаток = 5

# Так же можно находить числа кратные числу, например найти числа кратные 4 в последовательности чисел
# for n in range(21):
#     if n % 4 == 0:
#         print(n)

# a = число % 2 # узнаём есть ли остаток после точки при делении
# возвращает 0 если остатка нет, 1 если остаток есть (можно вычислять четные или не четные числа)

# for n in range(1, 11):
#     if n % 2 == 0:
#         stri = 'Четное'
#     else:
#         stri = 'Не четное'
#     print(f'Число: {n} {stri}')

# a = 6 ** 3 # возведение в степень (аналог 6*6*6)
# унарный минус
# a = 10
# a = -a # из положительного в отрицательное значение
# a = -a # из отрицательного в положительное значение
# print(a)

# Операции с числами
# print(sum( [10, 7, 2, 15] )) # функция sum() складывает все числовые значения из списка
# print(abs(-13.2)) # функция abs() переводит число из отрицательного в положительное
# print(min(16,9,-3,42,25)) # возвращает минимальное число
# print(max(90,4,-2,54,63)) # возвращает максимальное число
# print(pow(16, 7), 16**7) # функция pow() возводит число в степень
# округление числа с плавающей точкой
# print(round(5.758, 1)) # округление от середины # так же может иметь 2 арг. который будет указывать с какой точки начинать округлять
# import math
# print(math.ceil(5.7)) # округление всегда в большую сторону
# print(math.floor(5.7)) # округление всегда в меньшую сторону
# print(math.trunc(54.748)) # обрезает знаки после точки оставляя только целое число # точно так же работает int(54.748)
# print("pi =", math.pi) # число пи

# print(
#     divmod(5, 5),
#     (5//5, 5%5),
#     (math.floor(5/5), 5%5),
# )
# lst = [1, 3, 5, 7, 9]
# print([divmod(x, 2) for x in lst])
# [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]

# для разделения математических операций по приоритету используются круглые скобки
# приоритет на примере
# # 7   5   6   4   3     2     1
# y = x + 7 > x + 2 * (x ** (3 ** x) )

# Арифметическая прогрессия
# a = int(input()) # 1  # 100
# b = int(input()) # 1  # 50
# c = int(input()) # 10 # 1
# x = a + b * (c - 1)
# print(x)

# Геометрическая прогрессия
# a = int(input()) # 1 # -2
# b = int(input()) # 2 # 10
# c = int(input()) # 5 # 3
# x = a * b ** (c - 1)
# print(x)

# разделение числа посимвольно с помощью математических операторов, замена срезам/индексации строк
# a = 1234
# n1 = a // 1000 # для первой цифры можно не использовать остаток от деления
# n2 = a // 100 % 10
# n3 = a // 10 % 10
# n4 = a // 1 % 10
# print(n1, n2, n3, n4, sep='   ')

# операции присваивания в пайтон
# a += b прибавляем a к b (аналог a = a + b)
# a -= b (аналог a = a - b)
# a *= b (аналог a = a * b)
# a /= b (аналог a = a / b)
# a //= b (аналог a = a // b)
# a %= b (аналог a = a % b)
# a &= b (аналог a = a & b)
# a |= b (аналог a = a | b)

# программа открывающая сайт https://www.youtube.com
# input не пропускает цикл пока пользователь не введёт какие либо данные
# import os
# while True :
# 	sayt = input("Введите адрес сайта:\n")
# 	if sayt == "завершить" :
# 		break
# 	if "https://" in sayt :
# 		os.system("start " + sayt)
# 		print("if")
# 	elif "www." in sayt :
# 		sayt = "https://" + sayt
# 		os.system("start " + sayt)
# 		print("elif")
# 	else :
# 		sayt = "https://www." + sayt
# 		os.system("start " + sayt)
# 		print("else")

# import time
# import os
# time.sleep(3)
# os.system("start https://www.youtube.com")
# time.sleep(3)
# os.system("start https://www.twitch.tv")
# time.sleep(3)
# os.startfile("C:\Program Files\CPUID\CPU-Z\cpuz.exe")

# полностью очистить терминал
# import os
# os.system('cls') # для windows
# os.system('clear') # для linux/mac

# модуль рандом
# import random
# print(random.randint(0, 0xFFFFFF))
# print(random.randint(0, 100)) # выбрать рандомный элемент из диапазона
# print(random.randrange(1, 100)) # выбрать рандомный элемент из range
# # выбрать рандомный элемент из коллекции
# print(random.choice(['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit']))
# lst = list(range(1, 10))
# print(lst)
# random.shuffle(lst) # перемешать элементы в коллекции
# print(lst)

# while оператор цикла исполняется (пока условие верно)
# цикл от 1 до 5
# можно подключить оператор else который сработает по завершению цикла
# a = 0
# while a < 5 :
# 	a += 1
# 	print(a)
# else :
# 	print("finish")

# while True :
# 	a = int(input())
# 	b = 1
# 	count = 0
# 	while count < a :
# 		count += 1
# 		b *= count
# 	else :
# 		print("result:", b)

# while True :
# 	a = ""
# 	while len(a) < 5 :
# 		b = input("Ввод данных: ")
# 		if b == "o" :
# 			continue # игнорируем символ
# 		if b == "t" :
# 			break # прерываем цикл
# 		a += b
# 	else :
# 		print("result:", a)
# 	print(">>> Сброс программы <<<")


# def _len(x):
#     print(_len.__name__, x)
#     return len(x)

# # в условии цикла while не стоит использовать вызываемые объекты т.к. они будут выполнены на каждой итерации
# L = [1, 2, 3]
# while _len(L) < 5:
#     pass


# цикл for

# basket = [1,2,3,4,5,6]
# # спискам в цикле можно применять метод среза тем самым укоротив цикл до 3 итераций
# for i in basket[:3]:
#     print(i)

# можно подключить оператор else который сработает по завершению цикла
# ищем конкретные символы
# a = "test text"
# count = 0
# for i in a :
# 	if i == "t" :
# 		print("найдено совпадение:", i)
# 		count += 1
# 	if i == "x" :
# 		break
# else :
# 	print("result:", i, "=", count)

# пропускаем символы
# a = "test text"
# count = 0
# for i in a :
# 	if i == "t" :
# 		continue
# 	print(i)
# else :
# 	print("result:", i, "=", count)

# подсчёт количества повторяющихся символов
# while True :
# 	a = "йцукенгшщзхъфывапролджэячсмитьбю0123456789"
# 	b = input("Введите строку:\n")
# 	for i in a :
# 		count = 0
# 		for index in b :
# 			if i == index :
# 				count += 1
# 		if count > 0 :
# 			# idk :D
# 			if count == 2 or count == 3 or count == 4 or count == 22 or count == 23 or count == 24 :
# 				name = "раза"
# 			else :
# 				name = "раз"
# 			print("буква", '"' + i + '"', "попалась", count, name)

# функция range принимает аргументы (start, end, step)
# for i in range(3, 16, 2) :
# 	print(i)

# for i in range(10, -1, -1): # обратная последовательность от 10 до 0
#     print(i)
# либо так
# for i in range(11)[::-1]:
#     print(i)

# for i in range(-10, 0): # отрицательная последовательность от -10 до -1
#     print(i)