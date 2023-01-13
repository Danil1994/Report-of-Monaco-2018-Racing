from src.main.cli import parser, driver, create_info_dict, desc
from src.main.functions import sort_order

if __name__ == '__main__':
    cli_command = parser()
    info_dict = create_info_dict(cli_command)
    if cli_command.asc:
        print(info_dict)
    if cli_command.desc:
        drivers_list = desc(info_dict)
        for abbr_name_car in drivers_list:
            print(abbr_name_car)
    if cli_command.sort:
        sorted_order = sort_order(info_dict)
        for position_name_car_time in sorted_order:
            print(position_name_car_time)
    if cli_command.driver:
        print(driver(info_dict, cli_command.driver))
