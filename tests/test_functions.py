import unittest
from unittest.mock import patch, mock_open

from src.main.exception import FileDoesNotExist
from src.main.functions import read_file, abbr_and_time, \
    define_position, decoding_abbr, build_report, define_laps_time
from src.main.functions import print_report


class TestFunc(unittest.TestCase):

    def test_define_laps_time(self):
        self.assertEqual(define_laps_time(['2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332']), '0:01:04.415')

    @patch('src.main.functions.read_file', return_value="SVF2018-05-24_12:02:58.917\n")
    def test_abbr_and_time(self, mock_file):
        self.assertEqual(abbr_and_time(mock_file), {'SVF': ['2018-05-24_12:02:58.917']})
        mock_file.assert_called_once()

    @patch('src.main.functions.open', mock_open(read_data='asd'))
    def test_read_file(self):
        self.assertEqual(read_file('file_name'), 'asd')

    def test_read_file_exception(self):
        with self.assertRaises(FileDoesNotExist,
                               msg="ERROR: The specified file does not exist. Check spelling and try again"):
            read_file('wrong_path')

    @patch('src.main.functions.read_file', return_value='SVF_Sebastian Vettel_FERRARI\n')
    def test_decoding_abbr(self, mock_file):
        self.assertEqual(decoding_abbr('path'), {'SVF': ['Sebastian Vettel', 'FERRARI']})
        mock_file.assert_called_once()

    def test_decoding_abbr_exception(self):
        with self.assertRaises(FileDoesNotExist,
                               msg="ERROR: The specified file does not exist. Check spelling and try again"):
            decoding_abbr('path')

    @patch('src.main.functions.decoding_abbr', return_value={'SVF': ['Sebastian Vettel', 'FERRARI']})
    @patch('src.main.functions.define_laps_time', return_value='0:01:04.415')
    @patch('src.main.functions.abbr_and_time')
    def test_build_report(self, mock_abbr_and_time, mock_laps_time, mock_abbr):
        mock_abbr_and_time.side_effect = [{'SVF': ['2018-05-24_12:02:58.917']}, {'SVF': ['2018-05-24_12:04:03.332']}]
        self.assertEqual(build_report(mock_abbr_and_time, mock_abbr_and_time, mock_abbr_and_time),
                         {'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                                  '0:01:04.415']})
        mock_abbr.assert_called_once()
        mock_laps_time.assert_called_once()
        mock_abbr_and_time.assert_called()

    @patch('src.main.functions.build_report',
           return_value={'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                                 '0:01:04.415']})
    def test_print_report(self, mock_build_report):
        self.assertEqual(print_report('start', 'finish', 'abbreviations'), None)
        mock_build_report.assert_called_once()

    def test_define_position(self):
        self.assertEqual(define_position(
            {'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                     '0:01:04.415']}), None)
