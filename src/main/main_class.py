from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, NoReturn, Optional

from .exception import FileDoesNotExist


@dataclass
class Driver:
    abbr: str
    name: str
    car: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    lap_time: Optional[str] = None

    def __str__(self):
        return f"{self.name} {self.car} {self.lap_time}"


def _read_file(file_name: str) -> List[str]:
    try:
        with open(file_name, 'r', encoding='utf-8') as file_:
            return file_.readlines()
    except FileNotFoundError:
        raise FileDoesNotExist("Wrong path to the file.")


def _abbr_name_car(data: List[str]) -> List[List[str]]:
    abbr_name_car_list = []
    for line in data:
        line = line.strip('\n')
        abbr_name_car_list.append(line.split('_'))
    return abbr_name_car_list


def _abbr_and_time(data: List[str]) -> Dict[str, str]:
    dict_ = {}
    abbr_slice = slice(3)
    time_slice = slice(3, -1)
    for line in data:
        dict_[line[abbr_slice]] = line[time_slice]
    return dict_


def _calculate_laps_time(start_time: str, finish_time: str) -> str:
    time_format = '%Y-%m-%d_%H:%M:%S.%f'
    start_time = datetime.strptime(start_time, time_format)
    finish_time = datetime.strptime(finish_time, time_format)
    time_up_to_three_millisecond = slice(11)
    return str(finish_time - start_time)[time_up_to_three_millisecond]


def _init_abb_name_car(decoded_list) -> List[Driver]:
    list_of_drivers = []
    for driver_abbr_name_car in decoded_list:
        list_of_drivers.append(
            Driver(abbr=driver_abbr_name_car[0], name=driver_abbr_name_car[1], car=driver_abbr_name_car[2]))
    return list_of_drivers


def _add_start_end_time(list_of_drivers: List[Driver], start_info: Dict[str, str],
                        end_info: Dict[str, str]) -> List[Driver]:
    for driver in list_of_drivers:
        time_value = [start_info[driver.abbr], end_info[driver.abbr]]
        time_value.sort()
        driver.start_time = time_value[0]
        driver.end_time = time_value[1]
    return list_of_drivers


def _add_lap_time(list_of_drivers: List[Driver]) -> List[Driver]:
    list_with_lap_time = list_of_drivers
    for driver in list_with_lap_time:
        lap_time = _calculate_laps_time(str(driver.start_time), str(driver.end_time))
        driver.lap_time = lap_time
    return list_with_lap_time


def create(start: str, end: str, abbreviations: str) -> List[Driver]:
    data_about_start = _read_file(start)
    start_info = _abbr_and_time(data_about_start)

    data_about_end = _read_file(end)
    end_info = _abbr_and_time(data_about_end)

    abbreviations_data = _read_file(abbreviations)
    decoded_list = _abbr_name_car(abbreviations_data)

    init_list = _init_abb_name_car(decoded_list)
    obj_list_and_time = _add_start_end_time(init_list, start_info, end_info)
    order_list = _add_lap_time(obj_list_and_time)
    return order_list


def _build_position_list(order: List[Driver]) -> List[str]:
    answer = []
    for position, obj in enumerate(order, 1):
        info = f"{str(position) + '.':<3} {obj.name:<18} | {obj.car:<26} | {obj.lap_time}"
        answer.append(info)
    line = '-' * 59
    answer.insert(15, line)
    return answer


def sorting(order: List[Driver]) -> List[Driver]:
    order.sort(key=lambda x: x.lap_time)
    return order


def print_ascending(order: List[Driver]) -> NoReturn:
    sorted_order = sorting(order)
    list_with_position = _build_position_list(sorted_order)
    for line in list_with_position:
        print(line)


def print_descending(order: List[Driver]) -> NoReturn:
    sorted_order = sorting(order)
    list_with_position = _build_position_list(sorted_order)
    list_with_position.reverse()
    for line in list_with_position:
        print(line)


def find_driver(order: List[Driver], name: str) -> Driver | None:
    answer = None
    for driver in order:
        if driver.name == name:
            answer = driver
    return answer


def print_driver(order: List[Driver], name: str) -> NoReturn:
    name = name.strip(' ')
    driver = find_driver(order, name)
    print(driver)
