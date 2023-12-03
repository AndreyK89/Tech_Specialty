# Погружение в Python. Часть 1 (семинары)
# Урок 2. Простые типы данных.

# Задача 1.
# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


num = int(input('Введите число в десятичной системе: '))
def self_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result
print(f'Шестнадцатеричное представление -> {self_hex(num)}')

print(f'Проверка функция hex -> \t\t{hex(num)}')

# Задача 2.
# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего
# кода используйте модуль fractions.


from fractions import Fraction
import math


def shortenFraction(n: int, m: int):                                # Переделал без fractions.
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return str(n // k) + "/" + str(m // k)
        else:
            k -= 1
    return str(n) + "/" + str(m)


def sum_fractions(str_1, str_2):
    num_1 = str_1.split("/")
    num_2 = str_2.split("/")
    lcm_fraction = math.lcm(int(num_1[1]), int(num_2[1]))
    numeratorFraction_1 = int(lcm_fraction / int(num_1[1]) * int(num_1[0]))
    numeratorFraction_2 = int(lcm_fraction / int(num_2[1]) * int(num_2[0]))
    return shortenFraction(numeratorFraction_1 + numeratorFraction_2, lcm_fraction)


def mult_fraction(str1, str2):
    num_1 = str1.split("/")
    num_2 = str2.split("/")
    #return int(num_1[0]) * int(num_2[0]) / (int(num_1[1]) * int(num_2[1]))
    return shortenFraction(int(num_1[0]) * int(num_2[0]), int(num_1[1]) * int(num_2[1]))


def check_fraction(str1, str2, operation):              # Fraction
    num_1 = str1.split("/")
    num_2 = str2.split("/")
    if operation == "*":
        return Fraction(int(num_1[0]), int(num_1[1])) * Fraction(int(num_2[0]), int(num_2[1]))
    elif operation == "+":
        return Fraction(int(num_1[0]), int(num_1[1])) + Fraction(int(num_2[0]), int(num_2[1]))
    elif operation == "-":
        return Fraction(int(num_1[0]), int(num_1[1])) - Fraction(int(num_2[0]), int(num_2[1]))
    else:
        return Fraction(int(num_1[0]), int(num_1[1])) / Fraction(int(num_2[0]), int(num_2[1]))


str_1 = input("Введите первую дробь вида a/b: ")
str_2 = input("Введите вторую дробь вида a/b: ")

print("Расчет по программе:")
print(f'{str_1} * {str_2} = {mult_fraction(str_1, str_2)}')
print(f'{str_1} + {str_2} = {sum_fractions(str_1, str_2)}')

print("\nПроверка по Fraction:")
print(f'{str_1} * {str_2} = {check_fraction(str_1, str_2, "*")}')
print(f'{str_1} + {str_2} = {check_fraction(str_1, str_2, "+")}')

