import argparse
import os.path

from src.main.exception import NotArgument
from src.main.functions import build_report


def parser() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', required=True)
    parser.add_argument('--asc', action='store_true')
    parser.add_argument('--desc', action='store_true')
    parser.add_argument('--driver')
    obj = parser.parse_args()

    if obj.files is None:
        raise NotArgument("Use '--files' command and enter ptah to the file")

    def create_order():
        start = os.path.join(obj.files, 'start.log')
        finish = os.path.join(obj.files, 'end.log')
        abbreviations = os.path.join(obj.files, 'abbreviations.txt')
        return build_report(start, finish, abbreviations)

    order = create_order()

    def asc():
        for line in order:
            print(order[line])

    if obj.asc:
        asc()

    def desc():
        print('Abbr |   Name             |      Car\n''--------------------------------------------------------')
        for info in order:
            print(info.ljust(5, ' '), order[info][0].ljust(20, ' '), order[info][1])

    if obj.desc:
        desc()

    def driver():
        name = obj.driver
        print('     Name            |   Car   |       Start time         |        Finish time       | Laps time\n'
              '----------------------------------------------------------------------------------------------------')
        for line in order:
            if order[line][0] == name:
                return order[line]
        return "No info about this racer. Check that you used right name and try again"

    if obj.driver:
        print(driver())
