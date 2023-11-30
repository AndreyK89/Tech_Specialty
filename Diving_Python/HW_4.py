# Погружение в Python. Часть 1 (семинары).
# Урок 4. Функции.

# Задача 1. Напишите функцию для транспонирования матрицы.

matrix = [[1, 2, 3],
          [10, 20, 30],
          [100, 200, 300]]

print("Исходная матрица:\n", matrix)

def matrix_transposition(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)


print("Транспонированная матрица:")
matrix_transposition(matrix)

# Задача 2. Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.


names = ['str', 'int', 'bool', 'None', 'float', 'list', 'tuple', 'set']
vals = ['abc', 24, True, None, 3.14, [1, 2, 3], (1, 2, 3), {1, 2, 3}]

def form_dict(name_list, val_list):
    res_dict = {}
    for name, val in zip(name_list, val_list):
        try:
            res_dict[val] = name
        except TypeError:
            res_dict[str(val)] = name
    return res_dict

print(form_dict(names, vals))

# Задача 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Напишите программу банкомат.
# Начальная сумма равна нулю.
# Допустимые действия: пополнить, снять, выйти.
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте.
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
# Любое действие выводит сумму денег.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from datetime import date

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01

def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank, "y.e.")

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("Списаны проценты за cash: ", 30, "y.e.")
    elif cash * percent_take > 600:
        bank -= 600
        print("списаны проценты за cash: ", 600, "y.e.")
    else:
        bank -= cash * percent_take
        print("Списаны проценты за cash: ", cash * percent_take, "y.e.")
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank, "y.e.")


def exit_bank():
    print("Рады вас видетеь снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:
            return cash

list_operation = []

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax, "y.e.")
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("no money\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax, "y.e.")
        print("Баланс = ", bank, "y.e.")
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax, "y.e.")
        print("Баланс = ", bank, "y.e.")

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank, "y.e.")
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()
