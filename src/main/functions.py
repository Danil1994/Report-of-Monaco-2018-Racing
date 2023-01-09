import datetime

from .exception import FileDoesNotExist


def read_file(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as file_:
            return file_.readlines()
    except FileNotFoundError:
        raise FileDoesNotExist("Wrong path to the file.")


def abbr_and_time(data: list[str]) -> dict[str, list[str]]:
    dict_ = {}
    abbr_slice = slice(3)
    time_slice = slice(3, -1)
    for line in data:
        dict_[line[abbr_slice]] = [line[time_slice]]
    return dict_


def define_laps_time(start_finish: list) -> str:
    start = datetime.datetime.strptime(start_finish[0], '%Y-%m-%d_%H:%M:%S.%f')
    finish = datetime.datetime.strptime(start_finish[1], '%Y-%m-%d_%H:%M:%S.%f')
    cutting = slice(11)
    return str(finish - start)[cutting]


def decoding_abbr(data: list[str]) -> dict[str, list[str]]:
    abbr = {}
    abbr_slice = slice(3)
    name_car_slice = slice(4, -1)
    for line in data:
        abbr[line[abbr_slice]] = line[name_car_slice].split('_')
    return abbr


def all_time(start_time: dict[str, list[str]], finish_time: dict[str, list[str]]) -> dict[str, list[str]]:
    for abbr in start_time:
        start_time[abbr].append(finish_time[abbr][0])
        start_time[abbr].sort()
        laps_time = define_laps_time(start_time[abbr])
        start_time[abbr].append(laps_time)
    return start_time


def build_report(start: str, finish: str, abbreviations: str) -> dict:
    start_data = read_file(start)
    list_info = abbr_and_time(start_data)
    finish_data = read_file(finish)
    end_info = abbr_and_time(finish_data)

    list_info = all_time(list_info, end_info)

    abbreviations_data = read_file(abbreviations)
    decoder_list = decoding_abbr(abbreviations_data)
    for abbr in decoder_list:
        time = list_info[abbr]
        info = decoder_list[abbr]
        list_info[abbr] = info + time
    return list_info


def print_report(start: str, finish: str, abbreviations: str):
    print(build_report(start, finish, abbreviations))


def define_position(date_racer_about: dict) -> str:
    position_list = []
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


if __name__ == '__main__':
    build_report('C:/Users/38067/PycharmProjects/foxmind/data/start.log',
                 'C:/Users/38067/PycharmProjects/foxmind/data//end.log',
                 'C:/Users/38067/PycharmProjects/foxmind/data//abbreviations.txt')
