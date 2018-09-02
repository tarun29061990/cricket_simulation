import sys, os
import copy
from unittest import TestCase

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

from player import Player


class PlayerTestCase(TestCase):
    def setUp(self):
        print("", end='\n\n')
        print("Running test cases for Player", end="\n\n")

        self.p1 = Player('Kirat Boli', batting_order=1, probability_distribution=[5, 30, 25, 10, 15, 1, 9, 5])

    def test_create_player(self):
        self.assertEqual('Kirat Boli', self.p1.name)

        print("Create Player test case executed successfully", end='\n\n')

    def test_change_position(self):
        position = self.p1.get_position_on_pitch()

        self.p1.change_position()
        self.assertEqual(position ^ 1, self.p1.position_on_pitch)

        print("Change Position of a Player test case executed successfully", end='\n\n')

    def test_play(self):
        available_runs = [0, 1, 2, 3, 4, 5, 6, None]

        self.p1.play(available_runs)

        self.assertTrue(0 <= self.p1.runs <= 6)

        print("Play of a Player test case executed successfully", end='\n\n')

    def test_balls_played(self):
        balls_played = copy.copy(self.p1.get_balls_played())

        self.p1.set_balls_played()
        self.assertTrue(self.p1.balls_played == balls_played+1)

        print("Balls played by a Player test case executed successfully", end='\n\n')

    def test_add_runs(self):
        runs = self.p1.get_runs()

        self.p1.add_runs(2)
        self.assertTrue(self.p1.get_runs() == runs+2)

        print("Add runs of a Player test case executed successfully", end='\n\n')

    def tearDown(self):
        print("Test cases executed successfully for Player", end="\n\n")
