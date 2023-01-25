import argparse
import os.path
from argparse import Namespace

from .main_class import Driver, create


def parser() -> Namespace:
    cli_command = argparse.ArgumentParser()
    cli_command.add_argument('--files', required=True, help='Path to the file')
    cli_command.add_argument('--report', choices=['asc', 'desc'], help='Print order')
    cli_command.add_argument('--driver', help='Print driver info')
    return cli_command.parse_args()


def create_list_object(file_path: str) -> list[Driver]:
    start = os.path.join(file_path, 'start.log')
    finish = os.path.join(file_path, 'end.log')
    abbreviations = os.path.join(file_path, 'abbreviations.txt')
    return create(start, finish, abbreviations)
