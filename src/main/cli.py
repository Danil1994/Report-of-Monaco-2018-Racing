import argparse

from task_6_danil_shvecov.functions import build_report, decoding_abbr
from task_6_danil_shvecov.exception import NotArgument


def parser() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', required=True)
    parser.add_argument('--asc', action='store_true')
    parser.add_argument('--desc', action='store_true')
    parser.add_argument('--driver')
    obj = parser.parse_args()

    if obj.files is None:
        raise NotArgument("Use '--files' command and enter ptah to the file")

    start = obj.files + '/start.log'
    finish = obj.files + '/end.log'
    order = build_report(start, finish)

    if obj.asc:
        for line in order:
            print(line)

    if obj.desc:
        path = obj.files + '/abbreviations.txt'
        info_list = decoding_abbr(path)
        print(start, finish)
        print('Abbr |   Name             |      Car\n''--------------------------------------------------------')
        for info in info_list:
            print(info[0].ljust(5, ' '), info[1].ljust(25, ' '), info[2])

    if obj.driver:
        name = obj.driver
        name = name.title()

        print('№      Name         |     Car                      | Laps time\n'
              '---------------------------------------------------------------')
        for line in order:
            if line.count(name):
                return print(line)
        print("No info about this racer. Check that you used right name and try again")


if __name__ == '__main__':
    parser()
