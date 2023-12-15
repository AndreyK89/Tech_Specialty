"""
Задание №6
✔ Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.

✔ Для тестированию возьмите pickle версию файла из задачи 5 этого семинара.

✔ Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""


import csv
import json
import pickle
from pathlib import Path


def pickle_to_csv(file: Path) -> None:
    with (
        open(file, 'rb') as f_read,
        open(f'{file.stem}.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        data = pickle.load(f_read)
        headers_list = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=headers_list, dialect='excel-tab', quoting = csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
     pickle_to_csv(Path('json_in.pickle'))