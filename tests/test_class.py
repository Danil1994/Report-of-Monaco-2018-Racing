import unittest
from unittest.mock import patch, mock_open

from src.main.exception import FileDoesNotExist
from src.main.main_class import (read_file, abbr_and_time, Driver, abbr_name_car, init_abb_name_car, add_start_end_time,
                                 add_lap_time, define_laps_time, print_ascending, create,
                                 build_position_list
                                 )


class TestFunc(unittest.TestCase):

    @patch('src.main.main_class.open', mock_open(read_data='asd'))
    def test_read_file(self):
        self.assertEqual(read_file('file_name'), ['asd'])

    @patch('src.main.main_class.open')
    def test_read_file_exception(self, mock_open_wrong_path):
        mock_open_wrong_path.side_effect = [FileDoesNotExist]
        with self.assertRaises(FileDoesNotExist,
                               msg="ERROR: The specified file does not exist. Check spelling and try again"):
            read_file('wrong_path')

    def test_abbr_name_car(self):
        self.assertEqual(abbr_name_car(['DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER\n']),
                         [['DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER']])

    def test_abbr_and_time(self):
        self.assertEqual(abbr_and_time(['SVF2018-05-24_12:02:58.917\n']), {'SVF': '2018-05-24_12:02:58.917'})

    def test_define_laps_time(self):
        time_data = [['2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332', '0:01:04.415'],
                     ['2018-05-24_12:02:58.917', '2018-05-24_12:05:03.332', '0:02:04.415'],
                     ['2018-05-24_12:02:58.917', '2018-05-24_12:06:33.332', '0:03:34.415']]
        for time in time_data:
            self.assertEqual(define_laps_time(time[0], time[1]), time[2])

    def test_init_abb_name_car(self):
        self.assertEqual(init_abb_name_car([['DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER']]),
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
        self.assertEqual(add_start_end_time(driver, start_time, end_time),
                         [Driver(abbr='DRR',
                                 name='Daniel Ricciardo',
                                 car='RED BULL RACING TAG HEUER',
                                 start_time='2018-05-24_12:02:58.917',
                                 end_time='2018-05-24_12:04:03.332',
                                 lap_time=None)]
                         )

    @patch('src.main.main_class.define_laps_time', return_value='0:01:04.415')
    def test_add_lap_time(self, mock_lap_time):
        driver = [Driver(abbr='DRR',
                         name='Daniel Ricciardo',
                         car='RED BULL RACING TAG HEUER',
                         start_time='2018-05-24_12:02:58.917',
                         end_time='2018-05-24_12:04:03.332',
                         lap_time=None)]
        self.assertEqual(add_lap_time(driver), [Driver(abbr='DRR',
                                                       name='Daniel Ricciardo',
                                                       car='RED BULL RACING TAG HEUER',
                                                       start_time='2018-05-24_12:02:58.917',
                                                       end_time='2018-05-24_12:04:03.332',
                                                       lap_time='0:01:04.415')])
        mock_lap_time.assert_called_once()

    @patch('src.main.main_class.read_file')
    @patch('src.main.main_class.abbr_and_time')
    @patch('src.main.main_class.abbr_name_car',
           return_value=[['SVF', 'Sebastian Vettel', 'FERRARI']])
    @patch('src.main.main_class.init_abb_name_car', return_value=[Driver(abbr='DRR',
                                                                         name='Daniel Ricciardo',
                                                                         car='RED BULL RACING TAG HEUER',
                                                                         start_time=None,
                                                                         end_time=None,
                                                                         lap_time=None)])
    @patch('src.main.main_class.add_start_end_time', return_value=[Driver(abbr='DRR',
                                                                          name='Daniel Ricciardo',
                                                                          car='RED BULL RACING TAG HEUER',
                                                                          start_time='2018-05-24_12:02:58.917',
                                                                          end_time='2018-05-24_12:04:03.332',
                                                                          lap_time=None)])
    @patch('src.main.main_class.add_lap_time', return_value=[Driver(abbr='DRR',
                                                                    name='Daniel Ricciardo',
                                                                    car='RED BULL RACING TAG HEUER',
                                                                    start_time='2018-05-24_12:02:58.917',
                                                                    end_time='2018-05-24_12:04:03.332',
                                                                    lap_time='0:01:04.415')])
    def test_create(self, mock_add_lap_time, mock_add_start_end_time, mock_init_abb_name_car, mock_abbr_name_car,
                    mock_abbr_and_time,
                    mock_read_file):
        mock_read_file.side_effect = ['DRR2018-05-24_12:02:58.917', 'DRR2018-05-24_12:04:03.332',
                                      'DRR_aniel Ricciardo_RED BULL RACING TAG HEUER']
        mock_abbr_and_time.side_effect = [{'DRR': ['2018-05-24_12:02:58.917']}, {'SVF': ['2018-05-24_12:04:03.332']}]
        self.assertEqual(create(mock_read_file, mock_read_file, mock_read_file),
                         [Driver(abbr='DRR',
                                 name='Daniel Ricciardo',
                                 car='RED BULL RACING TAG HEUER',
                                 start_time='2018-05-24_12:02:58.917',
                                 end_time='2018-05-24_12:04:03.332',
                                 lap_time='0:01:04.415')])
        mock_abbr_name_car.assert_called_once()
        mock_init_abb_name_car.assert_called_once()
        mock_add_start_end_time.assert_called_once()
        mock_add_lap_time.assert_called_once()
        mock_read_file.assert_called()
        mock_abbr_and_time.assert_called()

    def test_build_position_list(self):
        self.assertEqual(build_position_list([Driver(abbr='DRR',
                                                     name='Daniel Ricciardo',
                                                     car='RED BULL RACING TAG HEUER',
                                                     start_time='2018-05-24_12:02:58.917',
                                                     end_time='2018-05-24_12:04:03.332',
                                                     lap_time='0:01:04.415')]),
                         ['1. Daniel Ricciardo  |RED BULL RACING TAG HEUER |0:01:04.415',
                          '-----------------------------------------------------------'])

    @patch('src.main.main_class.build_position_list',
           return_value=['1. Daniel Ricciardo  |RED BULL RACING TAG HEUER |0:01:04.415',
                         '-----------------------------------------------------------'])
    def test_print_ascending(self, mock_build_position_list):
        self.assertEqual(print_ascending([Driver(abbr='DRR',
                                                 name='Daniel Ricciardo',
                                                 car='RED BULL RACING TAG HEUER',
                                                 start_time='2018-05-24_12:02:58.917',
                                                 end_time='2018-05-24_12:04:03.332',
                                                 lap_time='0:01:04.415')]), None)
        mock_build_position_list.assert_called_once()
