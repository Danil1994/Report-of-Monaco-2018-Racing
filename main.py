from src.main.functions import build_report, define_position, print_report


if __name__ == '__main__':
    build_report('C:/Users/38067/PycharmProjects/foxmind/data/start.log',
                 'C:/Users/38067/PycharmProjects/foxmind/data//end.log',
                 'C:/Users/38067/PycharmProjects/foxmind/data//abbreviations.txt')

    define_position(build_report('C:/Users/38067/PycharmProjects/foxmind/data/start.log',
                                 'C:/Users/38067/PycharmProjects/foxmind/data//end.log',
                                 'C:/Users/38067/PycharmProjects/foxmind/data//abbreviations.txt'))

    print_report('C:/Users/38067/PycharmProjects/foxmind/data/start.log',
                 'C:/Users/38067/PycharmProjects/foxmind/data//end.log',
                 'C:/Users/38067/PycharmProjects/foxmind/data//abbreviations.txt')
