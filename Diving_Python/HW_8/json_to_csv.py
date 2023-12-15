"""
Задание №3
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате `CSV`.
"""


import json
import csv
import os
from pathlib import Path


def reader_json(file: Path) -> dict[str, str, str]:
    json_file = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_file = json.load(js)
    return json_file


def write_csv(json_file: dict, file_out: Path) -> None:
    rows = []
    for level, value in json_file.items():
        for id, name in value.items():
            rows.append({'level': level, 'user_id': id, 'name': name})

    with open(file_out, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['level', 'user_id', 'name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def json_to_csv(file_in: Path, file_out: Path) -> None:
    write_csv(reader_json(file_in), file_out)


if __name__ == '__main__':
    json_to_csv(Path('data1.json'), Path('file_out1.csv'))