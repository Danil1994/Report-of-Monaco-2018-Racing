import argparse
import unittest
from unittest.mock import patch

from src.main.cli import parser, create_info_dict, desc, driver
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

    def test_desc(self):
        self.assertEqual(
            desc({'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                          '0:01:04.415']
                  }), ['ABB | Name              |Car          \n'
                       '-------------------------------------------------------',
                       'SVF  Sebastian Vettel    FERRARI'])

    def test_driver_command(self):
        self.assertEqual(
            driver({'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                            '0:01:04.415']
                    }, 'Sebastian Vettel'),
            ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332', '0:01:04.415']
        )

    def test_driver_not_name(self):
        self.assertEqual(
            driver({'SVF': ['Sebastian Vettel', 'FERRARI', '2018-05-24_12:02:58.917', '2018-05-24_12:04:03.332',
                            '0:01:04.415']
                    }, 'Bad name'), "No info about this racer. Check that you used right name and try again")

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(files='asd', asc=None, desc=None,
                                                                                 driver=None))
    def test_wrong_path(self, mock_path):
        self.assertRaises(NotArgument, msg="Use '--files' command")
        mock_path.assert_not_called()
