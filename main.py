from src.main.cli import create_list_object, parser
from src.main.main_class import print_driver, print_report

if __name__ == '__main__':
    cli_command = parser()
    object_list = create_list_object(cli_command.files)
    if cli_command.report:
        print_report(object_list, cli_command.report)
    elif cli_command.driver:
        print_driver(object_list, cli_command.driver)
    else:
        print("Object list has been success created, but you did n`t use optional command")
