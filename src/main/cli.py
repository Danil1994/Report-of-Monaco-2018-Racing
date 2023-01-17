import argparse
import os.path
from argparse import Namespace

from .exception import NotDriver
from .functions import create_order


def parser() -> Namespace:
    cli_command = argparse.ArgumentParser()
    cli_command.add_argument('--files', required=True)
    cli_command.add_argument('order', choices=['--asc', '--desc'])
    cli_command.add_argument('--driver')
    return cli_command.parse_args()


def create_info_dict(file_path: str) -> dict[str, list[str]]:
    start = os.path.join(file_path, 'start.log')
    finish = os.path.join(file_path, 'end.log')
    abbreviations = os.path.join(file_path, 'abbreviations.txt')
    return create_order(start, finish, abbreviations)


def find_driver(order: dict, name: str) -> str:
    answer = None
    for abbr in order:
        if order[abbr][0] == name:
            answer = order[abbr]
    if answer is not None:
        return answer
    else:
        raise NotDriver("No info about this racer. Check that you used right name and try again")


def print_driver(name: str) -> print():
    print(name)
