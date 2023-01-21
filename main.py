from src.main.cli import parser, create_list_object, find_driver
from src.main.main_class import print_ascending, print_descending


cli_command = parser()
object_list = create_list_object(cli_command.files)
if cli_command.order == 'asc':
    print_ascending(object_list)
if cli_command.order == 'desc':
    print_descending(object_list)
if cli_command.driver:
    find_driver(object_list, cli_command.driver)
