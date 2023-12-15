"""
Задание №7
✔ Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.

✔ Распечатайте его как pickle строку.
"""


import csv
import pickle
from pathlib import Path


def csv_to_pickle(file: Path) -> None:
   pickle_list = []
   with open(file, 'r', newline='', encoding='utf-8') as f_read:
       csv_file = csv.reader(f_read, dialect='excel-tab')
       for i, line in enumerate(csv_file):
         print(i, line)
         if i == 0:
              pickle_keys = line
         else:
              pickle_dict = {k: v for k, v in zip(pickle_keys, line)}
              pickle_list.append(pickle_dict)
              print(pickle.dumps(pickle_list))

if __name__ == '__main__':
    csv_to_pickle(Path('json_in.csv'))