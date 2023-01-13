import argparse
import unittest
from unittest.mock import patch

from src.main.cli import parser, create_info_dict, print_abb_name_car, print_driver
from src.main.exception import NotArgument


class TestParser(unittest.TestCase):
    @patch('src.main.cli.create_order',
           return_value="{SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332]}")
    def test_create_info_dict(self, mock_create_order):
        self.assertEqual(create_info_dict(argparse.Namespace(files='Path/to/the/data', asc=True, desc=None,
                                                             driver=None)),
                         "{SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332]}")
        mock_create_order.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(files='C:/Users/38067/PycharmProjects/foxmind/data', asc=True, desc=None,
                                           driver=None))
    def test_parser(self, mock_args):
        self.assertEqual(parser(),
                         argparse.Namespace(files='C:/Users/38067/PycharmProjects/foxmind/data', asc=True, desc=None,
                                            driver=None))
        mock_args.assert_called_once()

    def test_print_abb_name_car(self):
        self.assertEqual(
            print_abb_name_car(
                {'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                         '0:01:04.415']
                 }), None)

    def test_print_driver(self):
        self.assertEqual(
            print_driver({'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                                  '0:01:04.415']
                          }, 'Sebastian Vettel'), None)

    def test_driver_not_name(self):
        self.assertEqual(
            print_driver({'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                                  '0:01:04.415']
                          }, 'Bad name'), None)

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(files='asd', asc=None, desc=None,
                                                                                 driver=None))
    def test_wrong_path(self, mock_path):
        self.assertRaises(NotArgument, msg="Use '--files' command")
        mock_path.assert_not_called()
