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

def add_and_multiply_fractions(STR1, STR2):
 STR1 = Fraction(STR1)
 STR2 = Fraction(STR2)

 sum_fraction = STR1 + STR2
 multiply_fraction = STR1 * STR2

 sum_fraction_str = f"{sum_fraction.numerator}/{sum_fraction.denominator}"
 multiply_fraction_str = f"{multiply_fraction.numerator}/{multiply_fraction.denominator}"

 return sum_fraction_str, multiply_fraction_str

STR1 = input("Введите первую дробь вида a/b: ")
STR2 = input("Введите вторую дробь вида a/b: ")

sum_fraction, multiply_fraction = add_and_multiply_fractions(STR1, STR2)

print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", multiply_fraction)

