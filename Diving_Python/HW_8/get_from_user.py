"""
Задание №2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и
уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json

from pathlib import Path
from typing import Any
from typing import Dict


def add_data(level: int, person_id: int, name: str) -> dict[int, dict[int, str]]:
    return {level: {person_id: name}}


def write_json(data: Dict) -> None:
    file = 'data.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_json(file: Path) -> dict[Any, Any] | Any:
    with open(file, "r", encoding='utf-8') as read_file:
        data = read_file.read()
        if data:
            return {}
        data_from_file = json.load(read_file)
    return data_from_file


def get_from_user(file: Path):
    base_dict = read_json(file)
    exit_program = False
    print('Добро пожаловать в программу. Введите данные для создания файлов ...')
    while not exit_program:
        level: int = int(input('Введите уровень доступа: '))
        personal_id: int = int(input('Введите id: '))
        name: str = input('Введите имя: ')
        continue_program = input('Хотите продлжить? y/n ')
        if continue_program == 'n':
            exit_program = True
        add_data(level, personal_id, name)
        if level in base_dict:
            base_dict[level].update({personal_id: name})
        else:

            base_dict[level] = {personal_id: name}
    write_json(base_dict)


if __name__ == "__main__":
    get_from_user(Path('data.json'))
