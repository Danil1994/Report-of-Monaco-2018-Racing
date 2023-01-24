import argparse
import os.path
from argparse import Namespace

from .exception import NotDriver
from .main_class import create, Driver


def parser() -> Namespace:
    cli_command = argparse.ArgumentParser()
    cli_command.add_argument('--files', required=True)
    cli_command.add_argument('--order', choices=['asc', 'desc'])
    cli_command.add_argument('--driver')
    return cli_command.parse_args()


def create_list_object(file_path: str) -> list[Driver]:
    start = os.path.join(file_path, 'start.log')
    finish = os.path.join(file_path, 'end.log')
    abbreviations = os.path.join(file_path, 'abbreviations.txt')
    return create(start, finish, abbreviations)


def find_driver(order: list[Driver], name: str) -> str:
    answer = None
    for driver in order:
        if driver.name == name:
            answer = f"{driver.name} {driver.car} {driver.lap_time}"
    if answer is not None:
        return answer
    else:
        raise NotDriver("No info about this racer. Check that you used right name and try again")


def print_driver(order: list[Driver], name: str) -> None:
    answer = find_driver(order, name)
    print(answer)
