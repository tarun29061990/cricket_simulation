import sys
import os
import unittest
from unittest import TestCase

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

from team_test_cases import TeamTestCase
from player_test_cases import PlayerTestCase
from game_test_cases import GameTestCase
from commentary_test_cases import CommentaryTestCase

class Runner(TestCase):
    def setUp(self):
        return

    def run_test_cases(self):
        suite1 = unittest.TestLoader().loadTestsFromTestCase(TeamTestCase)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(PlayerTestCase)
        suite3 = unittest.TestLoader().loadTestsFromTestCase(GameTestCase)
        suite4 = unittest.TestLoader().loadTestsFromTestCase(CommentaryTestCase)
        alltests = unittest.TestSuite([suite1, suite2, suite3, suite4])

    def tearDown(self):
        return



if __name__ == '__main__':
    unittest.main()