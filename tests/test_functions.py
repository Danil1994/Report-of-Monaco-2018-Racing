import unittest
from unittest.mock import patch, mock_open

from src.main.exception import FileDoesNotExist
from src.main.functions import read_file, abbr_and_time, \
    print_sort_order, decoding_abbr, create_order, define_laps_time


class TestFunc(unittest.TestCase):

    def test_define_laps_time(self):
        self.assertEqual(define_laps_time(['2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332']), '0:01:04.415')

    def test_abbr_and_time(self):
        self.assertEqual(abbr_and_time(['SVF2018-05-24_12:02:58.917\n']), {'SVF': ['2018-05-24_12:02:58.917']})

    @patch('src.main.functions.open', mock_open(read_data='asd'))
    def test_read_file(self):
        self.assertEqual(read_file('file_name'), ['asd'])

    def test_read_file_exception(self):
        with self.assertRaises(FileDoesNotExist,
                               msg="ERROR: The specified file does not exist. Check spelling and try again"):
            read_file('wrong_path')

    def test_decoding_abbr(self):
        self.assertEqual(decoding_abbr(['SVF_Sebastian Vettel_FERRARI\n']), {'SVF': ['Sebastian Vettel', 'FERRARI']})

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

    def test_sort_order(self):
        self.assertEqual(print_sort_order(
            {'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                     '0:01:04.415']}), None)
