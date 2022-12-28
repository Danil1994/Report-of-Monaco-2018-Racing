import unittest
from unittest.mock import patch, mock_open

from src.main.exception import FileDoesNotExist
from src.main.functions import read_file, decoding_abbr, create_string_position, build_report
from src.main.functions import print_report


class TestFunc(unittest.TestCase):

    @patch('src.main.functions.open', mock_open(read_data='asd'))
    def test_read_file(self):
        self.assertEqual(read_file('file_name'), {'asd': ['']})

    def test_read_file_exception(self):
        with self.assertRaises(FileDoesNotExist,
                               msg="ERROR: The specified file does not exist. Check spelling and try again"):
            read_file('wrong_path')

    @patch('src.main.functions.open', mock_open(read_data='SVF_Sebastian Vettel_FERRARI'))
    def test_decoding_abbr(self):
        self.assertEqual(decoding_abbr('file_name'), [['SVF', 'Sebastian Vettel', 'FERRARI']])

    def test_decoding_abbr_exception(self):
        with self.assertRaises(FileDoesNotExist,
                               msg="ERROR: The specified file does not exist. Check spelling and try again"):
            decoding_abbr()

    @patch('src.main.functions.decoding_abbr', return_value=[['SVF', 'Sebastian Vettel', 'FERRARI']])
    @patch('src.main.functions.read_file')
    def test_build_report(self, mock_data, mock_abbr):
        mock_data.side_effect = [{'SVF': ['2018-05-24_12:02:58.917']}, {'SVF': ['2018-05-24_12:04:03.332']}]
        self.assertEqual(build_report(mock_data, mock_data),
                         ['1.Sebastian Vettel  |FERRAR                        |0:01:04.415',
                          '------------------------------------------------------------------'])
        mock_abbr.assert_called_once()
        mock_data.assert_called()

    @patch('src.main.functions.build_report',
           return_value=['1.Sebastian Vettel  |FERRAR                        |0:01:04.415'])
    def test_print_report(self, mock_build_report):
        self.assertEqual(print_report(), None)
        mock_build_report.assert_called_once()

    def test_create_string_position(self):
        self.assertEqual(create_string_position(['LHM', 'Lewis Hamilton', 'MERCEDES\n', '0:06:47.540000', 'LHM']),
                         'Lewis Hamilton    |MERCEDES                      |0:06:47.540')
