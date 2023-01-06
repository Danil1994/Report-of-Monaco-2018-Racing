import argparse
import unittest
from unittest.mock import patch

from src.main.cli import parser
from src.main.exception import NotArgument


class TestParser(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(files='C:/Users/38067/PycharmProjects/foxmind/data', asc=True, desc=None,
                                           driver=None))
    def test_asc_command(self, mock_report):
        self.assertEqual(parser(), None)
        mock_report.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(files='C:/Users/38067/PycharmProjects/foxmind/data', asc=None, desc=True,
                                           driver=None))
    def test_desc_command(self, mock_args):
        self.assertEqual(parser(), None)
        mock_args.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(files='C:/Users/38067/PycharmProjects/foxmind/data', asc=None, desc=None,
                                           driver='Daniel Ricciardo'))
    def test_driver_command(self, mock_driver):
        self.assertEqual(parser(), None)
        mock_driver.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(files='asd', asc=None, desc=None,
                                                                                 driver=None))
    def test_wrong_path(self, mock_path):
        self.assertRaises(NotArgument, msg="Use '--files' command")
        mock_path.assert_not_called()
