import argparse
import unittest
from unittest.mock import patch

from src.main.cli import parser
from src.main.exception import NotArgument


class TestParser(unittest.TestCase):

    @patch('src.main.cli.build_report',
           return_value=['1.Sebastian Vettel  |FERRARI                        |0:01:04.415'])
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(files='../data', asc=True, desc=None, driver=None))
    def test_asc_command(self, mock_args, mock_report):
        self.assertEqual(parser(), None)
        mock_args.assert_called_once()
        mock_report.assert_called_once()
        mock_report.assert_called_with('../data/start.log', '../data/end.log')

    @patch('src.main.cli.build_report',
           return_value=['1.Sebastian Vettel  |FERRARI                        |0:01:04.415'])
    @patch('src.main.cli.decoding_abbr',
           return_value=[['DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER\n']])
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(files='../data', asc=None, desc=True, driver=None))
    def test_desc_command(self, mock_args, mock_decoding, mock_order):
        self.assertEqual(parser(), None)
        mock_args.assert_called_once()
        mock_decoding.assert_called_once()
        mock_decoding.assert_called_with('../data/abbreviations.txt')
        mock_order.assert_called_once()

    @patch('src.main.cli.build_report',
           return_value=['1.Sebastian Vettel  |FERRARI                        |0:01:04.415'])
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(files='../data', asc=None, desc=None, driver='daniel ricciardo'))
    def test_driver_command(self, mock_driver, mock_order):
        self.assertEqual(parser(), None)
        mock_driver.assert_called_once()
        mock_order.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(files='asd', asc=None, desc=None,
           driver=None))
    def test_wrong_path(self, mock_path):
        self.assertRaises(NotArgument, msg="Use '--files' command")
        mock_path.assert_not_called()
