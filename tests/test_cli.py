import argparse
import unittest
from unittest.mock import patch

from src.main.cli import parser, create_list_object, find_driver
from src.main.exception import NotDriver
from src.main.main_class import Driver


class TestParser(unittest.TestCase):
    @patch('src.main.cli.create', return_value=[Driver(abbr='DRR',
                                                       name='Daniel Ricciardo',
                                                       car='RED BULL RACING TAG HEUER',
                                                       start_time='2018-05-24_12:02:58.917',
                                                       end_time='2018-05-24_12:04:03.332',
                                                       lap_time='0:01:04.415')])
    def test_create_list_object(self, mock_create):
        self.assertEqual(create_list_object('Path/to/the/data'),
                         [Driver(abbr='DRR',
                                 name='Daniel Ricciardo',
                                 car='RED BULL RACING TAG HEUER',
                                 start_time='2018-05-24_12:02:58.917',
                                 end_time='2018-05-24_12:04:03.332',
                                 lap_time='0:01:04.415')])
        mock_create.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(files='C:/Users/38067/PycharmProjects/foxmind/data', asc=True, desc=None,
                                           driver=None))
    def test_parser(self, mock_args):
        self.assertEqual(parser(),
                         argparse.Namespace(files='C:/Users/38067/PycharmProjects/foxmind/data', asc=True, desc=None,
                                            driver=None))
        mock_args.assert_called_once()

    def test_find_driver(self):
        self.assertEqual(find_driver([Driver(abbr='DRR',
                                             name='Daniel Ricciardo',
                                             car='RED BULL RACING TAG HEUER',
                                             start_time='2018-05-24_12:02:58.917',
                                             end_time='2018-05-24_12:04:03.332',
                                             lap_time='0:01:04.415')], 'Daniel Ricciardo'),
                         'Daniel Ricciardo RED BULL RACING TAG HEUER 0:01:04.415')

    def test_find_driver_not_name(self):
        self.assertRaises(NotDriver,
                          find_driver, [Driver(abbr='DRR',
                                               name='Daniel Ricciardo',
                                               car='RED BULL RACING TAG HEUER',
                                               start_time='2018-05-24_12:02:58.917',
                                               end_time='2018-05-24_12:04:03.332',
                                               lap_time='0:01:04.415')], 'Bad name')
