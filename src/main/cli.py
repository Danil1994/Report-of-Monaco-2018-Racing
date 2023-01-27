import argparse
import os.path
from argparse import Namespace
from typing import List

from .main_class import Driver, create


def parser() -> Namespace:
    cli_command = argparse.ArgumentParser()
    cli_command.add_argument('--files', required=True, help='Path to the file')
    cli_command.add_argument('--driver', help='Print driver info')
    group = cli_command.add_mutually_exclusive_group()
    group.add_argument('--asc', action='store_false')
    group.add_argument('--desc', action='store_true')
    return cli_command.parse_args()


def create_list_object(file_path: str) -> List[Driver]:
    start = os.path.join(file_path, 'start.log')
    finish = os.path.join(file_path, 'end.log')
    abbreviations = os.path.join(file_path, 'abbreviations.txt')
    return create(start, finish, abbreviations)
