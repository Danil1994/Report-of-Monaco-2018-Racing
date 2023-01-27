import unittest
from datetime import datetime
from unittest.mock import mock_open, patch

from src.main.exception import FileDoesNotExist
from src.main.main_class import (Driver, _abbr_and_time, _abbr_name_car,
                                 _add_lap_time, _add_start_end_time,
                                 _build_position_list, _calculate_laps_time,
                                 _init_abb_name_car, _read_file, create,
                                 find_driver, print_ascending, print_driver)

time_format = '%Y-%m-%d_%H:%M:%S.%f'
drivers = [Driver(abbr='DRR',
                  name='Daniel Ricciardo',
                  car='RED BULL RACING TAG HEUER',
                  start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                  end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                  lap_time='0:01:04.415'),
           Driver(abbr='SVF',
                  name='Sebastian Vettel',
                  car='FERRARI',
                  start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                  end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                  lap_time='0:01:04.415'),
           Driver(abbr='LHM',
                  name='Lewis Hamilton',
                  car='MERCEDES',
                  start_time=datetime.strptime('2018-05-24_12:11:32.585', time_format),
                  end_time=datetime.strptime('2018-05-24_12:18:20.125', time_format),
                  lap_time='0:06:47.540')]


class TestFunc(unittest.TestCase):
    @patch('src.main.main_class.find_driver')
    def test_print_driver(self, mock_find_driver):
        self.assertEqual(print_driver(drivers, 'Sebastian Vettel'), None)
        mock_find_driver.assert_called_once()

    @patch('src.main.main_class.open', mock_open(read_data='asd'))
    def test_read_file(self):
        self.assertEqual(_read_file('file_name'), ['asd'])

    @patch('src.main.main_class.open')
    def test_read_file_exception(self, mock_open_wrong_path):
        mock_open_wrong_path.side_effect = [FileDoesNotExist]
        with self.assertRaises(FileDoesNotExist,
                               msg="Wrong path to the file"):
            _read_file('wrong_path')

    def test_abbr_name_car(self):
        self.assertEqual(_abbr_name_car(['DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER\n']),
                         [['DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER']])

    def test_abbr_and_time(self):
        self.assertEqual(_abbr_and_time(['SVF2018-05-24_12:02:58.917\n']), {'SVF': '2018-05-24_12:02:58.917'})

    def test_calculate_laps_time(self):
        time_data = [['2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332', '0:01:04.415'],
                     ['2018-05-24_12:02:58.917', '2018-05-24_12:05:03.332', '0:02:04.415'],
                     ['2018-05-24_12:02:58.917', '2018-05-24_12:06:33.332', '0:03:34.415']]
        for time in time_data:
            self.assertEqual(_calculate_laps_time(time[0], time[1]), time[2])

    def test_init_abb_name_car(self):
        self.assertEqual(_init_abb_name_car([['DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER']]),
                         [Driver(abbr='DRR',
                                 name='Daniel Ricciardo',
                                 car='RED BULL RACING TAG HEUER',
                                 start_time=None,
                                 end_time=None,
                                 lap_time=None)])

    def test_add_start_end_time(self):
        driver = [Driver(abbr='DRR',
                         name='Daniel Ricciardo',
                         car='RED BULL RACING TAG HEUER',
                         start_time=None,
                         end_time=None,
                         lap_time=None)]
        start_time = {'DRR': '2018-05-24_12:02:58.917'}
        end_time = {'DRR': '2018-05-24_12:04:03.332'}
        self.assertEqual(_add_start_end_time(driver, start_time, end_time),
                         [Driver(abbr='DRR',
                                 name='Daniel Ricciardo',
                                 car='RED BULL RACING TAG HEUER',
                                 start_time='2018-05-24_12:02:58.917',
                                 end_time='2018-05-24_12:04:03.332',
                                 lap_time=None)]
                         )

    @patch('src.main.main_class._calculate_laps_time', return_value='0:01:04.415')
    def test_add_lap_time(self, mock_lap_time):
        driver = [Driver(abbr='DRR',
                         name='Daniel Ricciardo',
                         car='RED BULL RACING TAG HEUER',
                         start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                         end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                         lap_time=None)]
        self.assertEqual(_add_lap_time(driver), [drivers[0]])
        mock_lap_time.assert_called_once()

    @patch('src.main.main_class._read_file')
    @patch('src.main.main_class._abbr_and_time')
    @patch('src.main.main_class._abbr_name_car',
           return_value=[['SVF', 'Sebastian Vettel', 'FERRARI']])
    @patch('src.main.main_class._init_abb_name_car', return_value=[Driver(abbr='DRR',
                                                                          name='Daniel Ricciardo',
                                                                          car='RED BULL RACING TAG HEUER',
                                                                          start_time=None,
                                                                          end_time=None,
                                                                          lap_time=None)])
    @patch('src.main.main_class._add_start_end_time', return_value=[Driver(abbr='DRR',
                                                                           name='Daniel Ricciardo',
                                                                           car='RED BULL RACING TAG HEUER',
                                                                           start_time=datetime.strptime(
                                                                               '2018-05-24_12:02:58.917', time_format),
                                                                           end_time=datetime.strptime(
                                                                               '2018-05-24_12:04:03.332', time_format),
                                                                           lap_time=None)])
    @patch('src.main.main_class._add_lap_time', return_value=[Driver(abbr='DRR',
                                                                     name='Daniel Ricciardo',
                                                                     car='RED BULL RACING TAG HEUER',
                                                                     start_time=datetime.strptime(
                                                                         '2018-05-24_12:02:58.917', time_format),
                                                                     end_time=datetime.strptime(
                                                                         '2018-05-24_12:04:03.332', time_format),
                                                                     lap_time='0:01:04.415')])
    def test_create(self, mock_add_lap_time, mock_add_start_end_time, mock_init_abb_name_car, mock_abbr_name_car,
                    mock_abbr_and_time,
                    mock_read_file):
        mock_read_file.side_effect = ['DRR2018-05-24_12:02:58.917', 'DRR2018-05-24_12:04:03.332',
                                      'DRR_aniel Ricciardo_RED BULL RACING TAG HEUER']
        mock_abbr_and_time.side_effect = [{'DRR': ['2018-05-24_12:02:58.917']}, {'SVF': ['2018-05-24_12:04:03.332']}]
        self.assertEqual(create(mock_read_file, mock_read_file, mock_read_file),
                         [drivers[0]])
        mock_abbr_name_car.assert_called_once()
        mock_init_abb_name_car.assert_called_once()
        mock_add_start_end_time.assert_called_once()
        mock_add_lap_time.assert_called_once()
        mock_read_file.assert_called()
        mock_abbr_and_time.assert_called()

    def test_build_position_list(self):
        self.assertEqual(_build_position_list(drivers),
                         ['1.  Daniel Ricciardo   | RED BULL RACING TAG HEUER  | 0:01:04.415',
                          '2.  Sebastian Vettel   | FERRARI                    | 0:01:04.415',
                          '3.  Lewis Hamilton     | MERCEDES                   | 0:06:47.540',
                          '-' * 59])

    @patch('src.main.main_class._build_position_list',
           return_value=['1. Daniel Ricciardo  |RED BULL RACING TAG HEUER |0:01:04.415',
                         '-' * 59])
    def test_print_ascending(self, mock_build_position_list):
        self.assertEqual(print_ascending(drivers), None)
        mock_build_position_list.assert_called_once()

    def test_find_driver(self):
        self.assertEqual(find_driver(drivers, 'Daniel Ricciardo'),
                         Driver(abbr='DRR',
                                name='Daniel Ricciardo',
                                car='RED BULL RACING TAG HEUER',
                                start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                                end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                                lap_time='0:01:04.415')
                         )

    def test_find_driver_not_name(self):
        self.assertEqual(find_driver(drivers, "Bad name"), None)
