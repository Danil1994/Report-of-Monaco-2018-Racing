import pytest
import unittest
from unittest.mock import patch, mock_open

from src.main.exception import FileDoesNotExist
from src.main.main_class import (read_file, abbr_and_time, decoding_abbr, create_order,
                                define_laps_time, all_time, sorting_order, print_descending, print_ascending
                                )


class TestFunc(unittest.TestCase):

    @patch('src.main.functions.open', mock_open(read_data='asd'))
    def test_read_file(self):
        self.assertEqual(read_file('file_name'), ['asd'])

    @patch('src.main.functions.open')
    def test_read_file_exception(self, mock_open_wrong_path):
        mock_open_wrong_path.side_effect = [FileDoesNotExist]
        with self.assertRaises(FileDoesNotExist,
                               msg="ERROR: The specified file does not exist. Check spelling and try again"):
            read_file('wrong_path')

    def test_abbr_and_time(self):
        self.assertEqual(abbr_and_time(['SVF2018-05-24_12:02:58.917\n']), {'SVF': ['2018-05-24_12:02:58.917']})

    @pytest.mark.parametrize('laps_time', 'result', [
        (['2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332'], ['0:01:04.415'])
    ])
    def test_define_laps_time(self, laps_time, result):
        self.assertEqual(define_laps_time(laps_time), result)

    def test_decoding_abbr(self):
        self.assertEqual(decoding_abbr(['SVF_Sebastian Vettel_FERRARI\n']), {'SVF': ['Sebastian Vettel', 'FERRARI']})

    @patch('src.main.functions.define_laps_time', return_value='0:01:04.415')
    def test_all_time(self, mock_laps_time):
        self.assertEqual(all_time({'SVF': ['2018-05-24_12:02:58.917']}, {'SVF': ['2018-05-24_12:04:03.332']}),
                         {'SVF': ['2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332', '0:01:04.415']})
        mock_laps_time.assert_called_once()

    @patch('src.main.functions.read_file')
    @patch('src.main.functions.abbr_and_time')
    @patch('src.main.functions.all_time',
           return_value={'SVF': ['2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332', '0:01:04.415']})
    @patch('src.main.functions.decoding_abbr', return_value={'SVF': ['Sebastian Vettel', 'FERRARI']})
    def test_create_order(self, mock_decoding, mock_all_time, mock_abbr_and_time, mock_read_file):
        mock_read_file.side_effect = ['SVF2018-05-24_12:02:58.917', 'SVF2018-05-24_12:04:03.332',
                                      'SVF_Sebastian Vettel_FERRARI']
        mock_abbr_and_time.side_effect = [{'SVF': ['2018-05-24_12:02:58.917']}, {'SVF': ['2018-05-24_12:04:03.332']}]
        self.assertEqual(create_order(mock_read_file, mock_read_file, mock_read_file),
                         {'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                                  '0:01:04.415']})
        mock_all_time.assert_called_once()
        mock_decoding.assert_called()
        mock_read_file.assert_called()
        mock_abbr_and_time.assert_called()

    def test_sorting_order(self):
        self.assertEqual(sorting_order(
            {'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                     '0:01:04.415']}), ['1. Sebastian Vettel  FERRARI                        0:01:04.415'])

    @patch('src.main.functions.sorting_order',
           return_value=['1. Sebastian Vettel  FERRARI                        0:01:04.415'])
    def test_print_ascending(self, mock_sorting_order):
        self.assertEqual(print_ascending(
            {'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                     '0:01:04.415']}), None)
        mock_sorting_order.assert_called_once()

    @patch('src.main.functions.sorting_order',
           return_value=['1. Sebastian Vettel  FERRARI                        0:01:04.415'])
    def test_print_descending(self, mock_sorting_order):
        self.assertEqual(print_descending(
            {'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                     '0:01:04.415']}), None)
        mock_sorting_order.assert_called_once()
