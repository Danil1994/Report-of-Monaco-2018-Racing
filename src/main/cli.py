import argparse
import os.path
from argparse import Namespace

from .main_class import Driver, _create


def parser() -> Namespace:
    cli_command = argparse.ArgumentParser()
    cli_command.add_argument('--files', required=True, help='Path to the file')
    cli_command.add_argument('--driver', help='Print driver info')
    group = cli_command.add_mutually_exclusive_group()
    group.add_argument('--asc', action='store_true', default=True)
    group.add_argument('--desc', action='store_true')
    return cli_command.parse_args()


def create_list_object(file_path: str) -> list[Driver]:
    start = os.path.join(file_path, 'start.log')
    finish = os.path.join(file_path, 'end.log')
    abbreviations = os.path.join(file_path, 'abbreviations.txt')
    return _create(start, finish, abbreviations)
