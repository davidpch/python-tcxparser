import os
from unittest import TestCase

from tcxparser import TCXParser


class TestParseCyclingPowerTCX(TestCase):

    def setUp(self):
        tcx_file = 'test_power.tcx'
        path = os.path.join(os.path.dirname(__file__), 'files', tcx_file)
        self.tcx = TCXParser(path)

    def test_max_power_is_correct(self):
        self.assertEqual(self.tcx.power_max, 1058)

    def test_power_avg_is_correct(self):
        self.assertEqual(self.tcx.power_avg, 214)
