from dataclasses import dataclass
import datetime
from typing import Optional

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
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    lap_time: Optional[str] = None


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


def init_abb_name_car(decoded_list) -> list[object]:
    list_of_drivers = []
    for driver_abbr_name_car in decoded_list:
        list_of_drivers.append(
            Driver(abbr=driver_abbr_name_car[0], name=driver_abbr_name_car[1], car=driver_abbr_name_car[2]))
    return list_of_drivers


def add_start_end_time(list_of_drivers: list[object], start_info: dict[str, str], end_info: dict[str, str]) -> list[
    object]:
    list_with_time = list_of_drivers
    for driver in list_with_time:
        time_value = [start_info[driver.abbr], end_info[driver.abbr]]
        time_value.sort()
        driver.start_time = time_value[0]
        driver.end_time = time_value[1]
    return list_with_time


def add_lap_time(list_of_drivers: list[object]) -> list[object]:
    list_with_lap_time = list_of_drivers
    for driver in list_with_lap_time:
        lap_time = define_laps_time(driver.start_time, driver.end_time)
        driver.lap_time = lap_time
    return list_with_lap_time


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


def build_position_list(order: list[object]) -> list[str]:
    order.sort(key=lambda x: x.lap_time)
    count = 1
    answer = []
    for obj in order:
        info = f"{count}.".ljust(3, ' ') + obj.name.ljust(18, ' ') + '|' + obj.car.ljust(26, ' ') + '|' + obj.lap_time
        answer.append(info)
        count += 1
    line = '-' * 59
    answer.insert(15, line)
    return answer


def print_ascending(order: list[object]) -> None:
    order_list = build_position_list(order)
    for line in order_list:
        print(line)


def print_descending(order: list[object]) -> None:
    order_list = build_position_list(order)
    order_list.reverse()
    for line in order_list:
        print(line)
