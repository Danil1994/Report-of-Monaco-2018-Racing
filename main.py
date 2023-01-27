from src.main.cli import create_list_object, parser
from src.main.main_class import print_driver, print_ascending, print_descending

if __name__ == '__main__':
    cli_command = parser()
    object_list = create_list_object(cli_command.files)
    if cli_command.desc:
        print_descending(object_list)
    elif cli_command.driver:
        print_driver(object_list, cli_command.driver)
    else:
        print_ascending(object_list)
