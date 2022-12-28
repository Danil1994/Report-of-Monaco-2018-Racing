import datetime

from task_6_danil_shvecov.exception import FileDoesNotExist


def read_file(file_name: str) -> dict:
    """create dict{abb:[time]...}"""
    dict_ = {}
    try:
        with open(file_name, 'r') as file_:
            for line in file_:
                dict_[line[:3]] = [line[3:26]]
            return dict_
    except FileNotFoundError:
        raise FileDoesNotExist("Wrong path to the file.")


def decoding_abbr(path='../data/abbreviations.txt') -> list:
    """create dict [['DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER\n']...]"""
    try:
        with open(path, 'r') as abbreviations:
            abbr = []
            for line in abbreviations:
                abbr.append(line.split('_'))
            return abbr
    except FileNotFoundError:
        raise FileDoesNotExist("ERROR: The specified file does not exist. Check spelling and try again")


def create_string_position(date_racer_about: dict) -> str:
    """made great info string like 'Lewis Hamilton    |MERCEDES                      |0:06:47.540'
                              from '['LHM', 'Lewis Hamilton', 'MERCEDES\n', '0:06:47.540000', 'LHM']' """
    name = str(date_racer_about[1])
    car = str(date_racer_about[2][:-1])
    time = str(date_racer_about[3])
    return name.ljust(18, ' ') + '|' + car.ljust(30, ' ') + '|' + time[:-3]


def build_report(start='../data/start.log', finish='../data/end.log'):
    """connect dict{abb:[start_time, finish_time]...}"""
    list_abbr_and_time = read_file(start)
    end_info = read_file(finish)
    for abbr in list_abbr_and_time:
        list_abbr_and_time[abbr].append(end_info[abbr][0])
    # list_abbr_and_time ="'SVF': ['2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332']"

    """define lap`s time {'SVF': '0:01:04.415000'...}"""
    for racer in list_abbr_and_time:
        list_abbr_and_time[racer].sort()  # check that finish time more than start time
        start = datetime.datetime.strptime(list_abbr_and_time[racer][0], '%Y-%m-%d_%H:%M:%S.%f')
        finish = datetime.datetime.strptime(list_abbr_and_time[racer][1], '%Y-%m-%d_%H:%M:%S.%f')
        list_abbr_and_time[racer] = str(finish - start)
    # list_abbr_and_time={'MES': '0:01:13.265000'}

    """create table and SORT BY TIME [[lap`s time], [abbr]...]"""
    table = []
    for info in list_abbr_and_time:
        table.append([list_abbr_and_time[info], info])
    table.sort()

    """connecting all info [['SVF', 'Sebastian Vettel', 'FERRARI\n', '0:01:04.415000', 'SVF']...]"""
    abbr = decoding_abbr()
    finish_table = []
    for date in table:
        for info in abbr:
            if date[1] == info[0]:
                info.extend(date)
                finish_table.append(info)

    """build full report"""
    order = []
    for racer in finish_table:
        str_ = (str(finish_table.index(racer) + 1) + '.') + create_string_position(racer)
        order.append(str_)
    order.insert(15, '------------------------------------------------------------------')

    return order


def print_report():
    full_report = build_report()
    for line in full_report:
        print(line)


if __name__ == '__main__':
    build_report()
    print_report()
