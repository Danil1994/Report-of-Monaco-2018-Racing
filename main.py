from src.main.cli import parser, print_driver, create_info_dict, print_abb_name_car
from src.main.functions import print_sort_order

if __name__ == '__main__':
    cli_command = parser()
    if cli_command.asc:
        create_info_dict(cli_command)
    if cli_command.desc:
        info_dict = create_info_dict(cli_command)
        print_abb_name_car(info_dict)
    if cli_command.sort:
        info_dict = create_info_dict(cli_command)
        print_sort_order(info_dict)
    if cli_command.driver:
        info_dict = create_info_dict(cli_command)
        print_driver(info_dict, cli_command.driver)
