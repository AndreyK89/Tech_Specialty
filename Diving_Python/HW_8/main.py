from pathlib import Path

from pickle_to_csv import pickle_to_csv
from csv_to_json import csv_to_json
from json_to_csv import json_to_csv
from direct_info import direct_info
from get_from_user import get_from_user, read_json
from txt_to_json import txt_to_json

if __name__ == '__main__':
    txt_to_json(Path('C:\\Users\\BETEPOK\\Documents\\Tech_Specialty\\Diving_Python\\HW_7\\files_manager\\task_3.txt'))
    get_from_user(Path('C:\\Users\\BETEPOK\\Documents\\Tech_Specialty\\Diving_Python\\HW_8\\data.json'))
    print(type(read_json(Path('C:\\Users\\BETEPOK\\Documents\\Tech_Specialty\\Diving_Python\\HW_8\\data.json'))))
    json_to_csv(Path('C:\\Users\\BETEPOK\\Documents\\Tech_Specialty\\Diving_Python\\HW_8\\file_out.csv')))
    csv_to_json(Path('file_out.csv'), Path('json_in.json'))
    pickle_to_csv(Path('json_in.pickle'))
    direct_info(Path(r'F:\GIT\Python_Seminar\first_project\Python_next_deep\Seminar_8'), 'name')