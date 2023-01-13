import argparse
import os.path
from argparse import Namespace

from .exception import NotArgument
from .functions import create_order


def parser() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', required=True)
    parser.add_argument('--asc', action='store_true')
    parser.add_argument('--desc', action='store_true')
    parser.add_argument('--sort', action='store_true')
    parser.add_argument('--driver')
    return parser.parse_args()


def create_info_dict(obj: Namespace) -> dict[str, list[str]]:
    if obj.files is None:
        raise NotArgument("Use '--files' command and enter ptah to the file")
    start = os.path.join(obj.files, 'start.log')
    finish = os.path.join(obj.files, 'end.log')
    abbreviations = os.path.join(obj.files, 'abbreviations.txt')
    return create_order(start, finish, abbreviations)


def desc(order: dict) -> list[str]:
    list_abb_name_car = ['ABB |' + ' Name' + ' ' * 14 + '|Car' + ' ' * 10 + '\n' + '-' * 55]
    for info in order:
        list_abb_name_car.append(info.ljust(5, ' ') + order[info][0].ljust(20, ' ') + order[info][1])
    return list_abb_name_car


def driver(order: dict, name: str) -> str:
    for abbr in order:
        if order[abbr][0] == name:
            return order[abbr]
    return "No info about this racer. Check that you used right name and try again"
