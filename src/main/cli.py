import argparse
import os.path
from argparse import Namespace

from .exception import NotDriver
from .main_class import create


def parser() -> Namespace:
    cli_command = argparse.ArgumentParser()
    cli_command.add_argument('--files', required=True)
    cli_command.add_argument('--order', choices=['asc', 'desc'])
    cli_command.add_argument('--driver')
    return cli_command.parse_args()


def create_list_object(file_path: str) -> list[object]:
    start = os.path.join(file_path, 'start.log')
    finish = os.path.join(file_path, 'end.log')
    abbreviations = os.path.join(file_path, 'abbreviations.txt')
    return create(start, finish, abbreviations)


def find_driver(order: list[object], name) -> None:
    answer = None
    for driver in order:
        if driver.name == name:
            name = getattr(driver, 'name')
            car = getattr(driver, 'car')
            lap_time = getattr(driver, 'lap_time')
            answer = f"{name} {car} {lap_time}"
    if answer is not None:
        print(answer)
    else:
        raise NotDriver("No info about this racer. Check that you used right name and try again")


