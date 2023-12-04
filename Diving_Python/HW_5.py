"""
Погружение в Python. Часть 1 (семинары).
Урок 5. Итераторы и генераторы.

Задача 1. Решить задачи, которые не успели решить на семинаре.

Задача 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os

string = "C:/Users/BETEPOK/Documents/Tech_Specialty/Diving_Python/HW_5.py"

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Путь до файла: {string} \nКортеж из пути: {fun(string)}')

"""
Задача 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа
и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.
"""


from pprint import pprint

names = ('Виктор Воронов', 'Андрей Орлов', 'Дмитрий Филинов')
salary = (90000, 120000, 50000)
bonus = ('10.25%', '12.5%', '15.3%')

bonus = {names[i]: salary[i] + salary[i] * (float(bonus[i][:-1]) / 100) for i in range(len(names))}

pprint(bonus)

"""
Задача 4. Создайте функцию генератор чисел Фибоначчи.
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
"""

a = int(input('Введите число: '))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(a)))