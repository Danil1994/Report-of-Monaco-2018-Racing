from src.main.cli import parser, create_info_dict, find_driver
from src.main.main_class import print_ascending, print_descending


cli_command = parser()
info_dict = create_info_dict(cli_command.files)
if cli_command.order == 'asc':
    print_ascending(info_dict)
if cli_command.order == 'desc':
    print_descending(info_dict)
if cli_command.driver:
    info_driver = find_driver(info_dict, cli_command.driver)
