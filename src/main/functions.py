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
    time_format = '%Y-%m-%d_%H:%M:%S.%f'
    start = datetime.datetime.strptime(start_finish[0], time_format)
    finish = datetime.datetime.strptime(start_finish[1], time_format)
    time_up_to_three_millisec = slice(11)
    return str(finish - start)[time_up_to_three_millisec]


def decoding_abbr(data: list[str]) -> dict[str, list[str]]:
    abbr = {}
    abbr_slice = slice(3)
    name_car_slice = slice(4, -1)
    for line in data:
        abbr[line[abbr_slice]] = line[name_car_slice].split('_')
    return abbr


def all_time(start_time: dict[str, list[str]], finish_time: dict[str, list[str]]) -> dict[str, list[str]]:
    start_finish_laps_time = {}
    for abbr in start_time:
        time_value = start_time.get(abbr) + finish_time.get(abbr)
        time_value.sort()
        laps_time = define_laps_time(time_value)
        time_value.append(laps_time)
        start_finish_laps_time[abbr] = time_value
    return start_finish_laps_time


def create_order(start: str, end: str, abbreviations: str) -> dict[str, list[str]]:
    data_about_start = read_file(start)
    start_info = abbr_and_time(data_about_start)

    data_about_end = read_file(end)
    end_info = abbr_and_time(data_about_end)

    abbreviations_data = read_file(abbreviations)
    decoded_list = decoding_abbr(abbreviations_data)

    abbr_and_all_time = all_time(start_info, end_info)
    order = {}
    for abbr in decoded_list:
        all_racers_time = abbr_and_all_time[abbr]
        abbr_name_car = decoded_list[abbr]
        order[abbr] = abbr_name_car + all_racers_time
    return order


def sort_order(date_racer_about: dict) -> list[str]:
    position_list = []
    for abbr in date_racer_about:
        date = [date_racer_about[abbr][-1], abbr]
        position_list.append(date)
    position_list.sort()

    place = 1
    sorted_order = []
    for info in position_list:
        name, car = date_racer_about[info[1]][0], date_racer_about[info[1]][1]
        position = str(place) + '.'
        sorted_order.append(position.ljust(3, ' ') + name.ljust(18, ' ') + car.ljust(30, ' ') + ' ' + str(info[0]))
        if place == 15:
            sorted_order.append('-'*63)
        place += 1
    return sorted_order
