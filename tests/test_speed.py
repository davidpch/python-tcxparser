import os
from unittest import TestCase

from tcxparser import TCXParser


class TestParseCyclingSpeedTCX(TestCase):

    def setUp(self):
        tcx_file = 'test_power.tcx'
        path = os.path.join(os.path.dirname(__file__), 'files', tcx_file)
        self.tcx = TCXParser(path)

    def test_max_speed_is_correct(self):
        self.assertEqual(self.tcx.speed_max, 23.1)

    def test_speed_avg_is_correct(self):
        self.assertEqual(self.tcx.avg_speed, 7)

    def test_time_stopped_is_correct(self):
        self.assertEqual(self.tcx.time_stopped, 113)

    def test_moving_time_is_correct(self):
        self.assertEqual(self.tcx.moving_time, 5909)
