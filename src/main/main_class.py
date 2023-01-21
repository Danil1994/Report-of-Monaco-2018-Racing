from dataclasses import dataclass
import datetime

from .exception import FileDoesNotExist


def read_file(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as file_:
            return file_.readlines()
    except FileNotFoundError:
        raise FileDoesNotExist("Wrong path to the file.")


def abbr_name_car(data: list[str]) -> list[list[str]]:
    abbr_name_car_list = []
    del_n_symbol = slice(0, -1)
    for line in data:
        abbr_name_car_list.append(line[del_n_symbol].split('_'))
    return abbr_name_car_list


@dataclass
class Driver:
    abbr: str
    name: str
    car: str
    start: datetime = None
    end: datetime = None
    lap_time: str = None


def abbr_and_time(data: list[str]) -> dict[str, str]:
    dict_ = {}
    abbr_slice = slice(3)
    time_slice = slice(3, -1)
    for line in data:
        dict_[line[abbr_slice]] = line[time_slice]
    return dict_


def define_laps_time(start_time: str, finish_time: str) -> str:
    time_format = '%Y-%m-%d_%H:%M:%S.%f'
    start_time = datetime.datetime.strptime(start_time, time_format)
    finish_time = datetime.datetime.strptime(finish_time, time_format)
    time_up_to_three_millisec = slice(11)
    return str(finish_time - start_time)[time_up_to_three_millisec]


def init_abb_name_car(decoded_list):
    list_of_drivers = []
    for driver_abbr_name_car in decoded_list:
        list_of_drivers.append(
            Driver(abbr=driver_abbr_name_car[0], name=driver_abbr_name_car[1], car=driver_abbr_name_car[2]))
    return list_of_drivers


def add_start_end_time(list_of_drivers, start_info, end_info):
    for driver in list_of_drivers:
        time_value = [start_info[driver.abbr], end_info[driver.abbr]]
        time_value.sort()
        driver.start = time_value[0]
        driver.end = time_value[1]
    return list_of_drivers


def add_lap_time(list_of_drivers):
    for time_data in list_of_drivers:
        lap_time = define_laps_time(time_data.start, time_data.end)
        time_data.lap_time = lap_time
    return list_of_drivers


def create(start: str, end: str, abbreviations: str) -> list[object]:
    data_about_start = read_file(start)
    start_info = abbr_and_time(data_about_start)

    data_about_end = read_file(end)
    end_info = abbr_and_time(data_about_end)

    abbreviations_data = read_file(abbreviations)
    decoded_list = abbr_name_car(abbreviations_data)

    init_list = init_abb_name_car(decoded_list)
    obj_list_and_time = add_start_end_time(init_list, start_info, end_info)
    order_list = add_lap_time(obj_list_and_time)

    return order_list


def print_ascending(order: list[object]) -> print(str):
    order.sort(key=lambda x: x.lap_time)
    count = 1
    for obj in order:
        if count == 16:
            print('-' * 64)
        print(f"{count}.".ljust(3, ' '), obj.name.ljust(18, ' '), '|', obj.car.ljust(25, ' '), '|', obj.lap_time)
        count += 1


def print_descending(order: list[object]) -> print(str):
    order.sort(key=lambda x: x.lap_time)
    order.reverse()
    count = 1
    for obj in order:
        if count == 16:
            print('-' * 64)
        print(f"{count}.".ljust(3, ' '), obj.name.ljust(18, ' '), '|', obj.car.ljust(25, ' '), '|', obj.lap_time)
        count += 1
