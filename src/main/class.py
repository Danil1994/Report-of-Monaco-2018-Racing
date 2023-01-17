from dataclasses import dataclass
import datetime

from exception import FileDoesNotExist


def read_file(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as file_:
            return file_.readlines()
    except FileNotFoundError:
        raise FileDoesNotExist("Wrong path to the file.")


def decoding_abbr(data: list[str]) -> list[list[str]]:
    abbr_name_car = []
    del_n_symbol = slice(0, -1)
    for line in data:
        abbr_name_car.append(line[del_n_symbol].split('_'))
    return abbr_name_car


@dataclass
class Driver:
    abbr: str
    name: str
    car: str
    start: str = None
    end: str = None
    lap_time: str = None
    table_palace: int = None


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


abbreviations = 'C:/Users/38067/PycharmProjects/foxmind/data/' + 'abbreviations.txt'
start = 'C:/Users/38067/PycharmProjects/foxmind/data/' + 'start.log'
end = 'C:/Users/38067/PycharmProjects/foxmind/data/' + 'end.log'

data_about_start = read_file(start)
start_info = abbr_and_time(data_about_start)

data_about_end = read_file(end)
end_info = abbr_and_time(data_about_end)

abbreviations_data = read_file(abbreviations)
decoded_list = decoding_abbr(abbreviations_data)

# create
list_of_drivers = []
for abbr_name_car in decoded_list:
    list_of_drivers.append(Driver(abbr=abbr_name_car[0], name=abbr_name_car[1], car=abbr_name_car[2]))

# add time
for driver in list_of_drivers:
    time_value = [start_info[driver.abbr], end_info[driver.abbr]]
    time_value.sort()
    driver.start = time_value[0]
    driver.end = time_value[1]

# add lap time
for time_data in list_of_drivers:
    lap_time = define_laps_time(time_data.start, time_data.end)
    time_data.lap_time = lap_time

print(list_of_drivers)


# sort
def sorting(info_drivers: dataclass()) -> list[list]:
    list_ = []
    for i in info_drivers:
        list_.append(i.lap_time)
    list_.sort()
    return list_


sorted_time = sorting(list_of_drivers)

for time in sorted_time:
    place = sorted_time.index(time)+1
    for driver in list_of_drivers:
        if driver.lap_time == time:
            driver.table_palace = place
print(list_of_drivers)
