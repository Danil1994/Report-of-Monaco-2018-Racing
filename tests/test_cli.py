import argparse
import unittest
from unittest.mock import patch

from src.main.cli import create_list_object, parser
from src.main.main_class import Driver

drivers = [Driver(abbr='DRR',
                  name='Daniel Ricciardo',
                  car='RED BULL RACING TAG HEUER',
                  start_time='2018-05-24_12:02:58.917',
                  end_time='2018-05-24_12:04:03.332',
                  lap_time='0:01:04.415'),
           Driver(abbr='SVF',
                  name='Sebastian Vettel',
                  car='FERRARI',
                  start_time='2018-05-24_12:02:58.917',
                  end_time='2018-05-24_12:04:03.332',
                  lap_time='0:01:04.415'),
           Driver(abbr='LHM',
                  name='Lewis Hamilton',
                  car='MERCEDES',
                  start_time='2018-05-24_12:11:32.585',
                  end_time='2018-05-24_12:18:20.125',
                  lap_time='0:06:47.540')]


class TestParser(unittest.TestCase):

    @patch('src.main.cli.create', return_value=drivers[0])
    def test_create_list_object(self, mock_create):
        self.assertEqual(create_list_object('Path/to/the/data'),
                         drivers[0])
        mock_create.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(files='C:/Users/38067/PycharmProjects/foxmind/data', asc=True, desc=None,
                                           driver=None))
    def test_parser(self, mock_args):
        self.assertEqual(parser(),
                         argparse.Namespace(files='C:/Users/38067/PycharmProjects/foxmind/data', asc=True, desc=None,
                                            driver=None))
        mock_args.assert_called_once()
