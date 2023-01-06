import datetime

from src.main.exception import FileDoesNotExist


def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r') as file_:
            return file_.read()
    except FileNotFoundError:
        raise FileDoesNotExist("Wrong path to the file.")


def abbr_and_time(file_: str) -> dict:
    dict_: dict[{'ABBR': ['time']}] = {}
    file_ = read_file(file_)
    file_ = file_.split('\n')
    for line in file_:
        dict_[line[:3]] = [line[3:26]]
    dict_.pop('')
    return dict_


def define_laps_time(start_finish: list) -> str:
    start = datetime.datetime.strptime(start_finish[0], '%Y-%m-%d_%H:%M:%S.%f')
    finish = datetime.datetime.strptime(start_finish[1], '%Y-%m-%d_%H:%M:%S.%f')
    return str(finish - start)[:-3]


def decoding_abbr(path: str) -> list:
    abbr: dict["{'ABBR':['Name', 'Car']}"] = {}
    abbreviations = read_file(path)
    abbreviations = abbreviations.split('\n')
    for line in abbreviations:
        abbr[line[:3]] = line[4:].split('_')
    abbr.popitem()
    return abbr


def build_report(start: str, finish: str, abbreviations: str) -> dict:
    list_info: dict["{ABBR:[name, car, start_time, finish_time, laps_time]}"] = abbr_and_time(start)
    end_info = abbr_and_time(finish)

    for abbr in list_info:
        list_info[abbr].append(end_info[abbr][0])
        list_info[abbr].sort()
        list_info[abbr].append(define_laps_time(list_info[abbr]))

    decoder = decoding_abbr(abbreviations)
    for abbr in decoder:
        list_info[abbr].insert(0, decoder[abbr][1])
        list_info[abbr].insert(0, decoder[abbr][0])

    return list_info


def print_report(start: str, finish: str, abbreviations: str):
    print(build_report(start, finish, abbreviations))


def define_position(date_racer_about: dict) -> str:
    position_list: list['time', 'abbr', 'position'] = []
    place = 1
    for abbr in date_racer_about:
        date = [date_racer_about[abbr][-1], abbr]
        position_list.append(date)
        position_list.sort()

    for info in position_list:
        name, car = date_racer_about[info[1]][0], date_racer_about[info[1]][1]
        position = str(place) + '.'
        print(position.ljust(3, ' ') + name.ljust(18, ' ') + car.ljust(30, ' ') + ' ' + str(info[0]))
        if place == 15:
            print('---------------------------------------------------------------')
        place += 1
