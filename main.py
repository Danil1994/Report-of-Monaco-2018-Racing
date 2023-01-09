from src.main.cli import parser, asc, desc, driver, create_order

if __name__ == '__main__':
    cli_command = parser()
    order = create_order(cli_command)
    if cli_command.asc:
        asc(order)
    if cli_command.desc:
        desc(order)
    if cli_command.driver:
        driver(order, cli_command.driver)
