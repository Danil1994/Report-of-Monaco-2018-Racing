import argparse
import os.path
from argparse import Namespace

from .exception import NotArgument
from .functions import build_report


def parser() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', required=True)
    parser.add_argument('--asc', action='store_true')
    parser.add_argument('--desc', action='store_true')
    parser.add_argument('--driver')
    return parser.parse_args()


def create_order(obj: Namespace) -> dict:
    if obj.files is None:
        raise NotArgument("Use '--files' command and enter ptah to the file")
    start = os.path.join(obj.files, 'start.log')
    finish = os.path.join(obj.files, 'end.log')
    abbreviations = os.path.join(obj.files, 'abbreviations.txt')
    return build_report(start, finish, abbreviations)


def asc(order: dict):
    for line in order:
        print(order[line])


def desc(order: dict):
    print('Abbr |   Name             |      Car\n''--------------------------------------------------------')
    for info in order:
        print(info.ljust(5, ' '), order[info][0].ljust(20, ' '), order[info][1])


def driver(order: dict, name: str) -> str:
    for line in order:
        if order[line][0] == name:
            print('     Name            |   Car   |       Start time         |        Finish time       | Laps time\n'
                  '-------------------------------------------------------------------------------------------------\n',
                  order[line])
        else:
            return "No info about this racer. Check that you used right name and try again"
