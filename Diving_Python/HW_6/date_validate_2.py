"""
Задача 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

import calendar
from sys import argv

def funcDate():
    text = (input('DD.MM.YYYY - >>> '))
    text = text.split('.')
    month = int(text[1])
    days = calendar.monthrange(int(text[2]), int(text[1]))[1]
    if int(text[0]) <= days and int(text[1]) <= 12:
        print('Корректная дата')
        a = input('')
        return True
    else :
        print('Некорректная дата')
        a = input('')
        return False

def vys_Year(year):
    if calendar.monthrange(year, 2) == 29:
        return True
    else:
        return False


if __name__ == '__main__':
#   funcDate()
    funcDate()(argv[1:])         # Возможность запуска в терминале