import sys, os
import copy
from unittest import TestCase

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

from player import Player
from game import Game
from team import Team

class GameTestCase(TestCase):
    def setUp(self):
        print("", end='\n\n')
        print("Running test case for Game", end="\n\n")
        self.game = Game(name='cricketT20', overs=4, balls_per_over=6)
        self.team1 = Team('team1')
        self.team2 = Team('team2')

    def test_add_team(self):
        teams = copy.copy(self.game.get_teams())

        self.game.add_team(self.team1)

        self.assertTrue(len(teams)+1 == len(self.game.get_teams()))

        print("Add Team test case for Game executed successfully", end="\n\n")

    def test_check_who_won(self):
        self.team1.set_runs(40)
        self.team2.set_runs(41)

        self.game.add_team(self.team1)
        self.game.add_team(self.team2)

        team = self.game.check_who_won()

        self.assertTrue(team == self.team2)  # can compare objects directly in python

        print("Check which team won test case for Game executed successfully", end="\n\n")

    def test_get_target_score(self):
        self.team1.set_runs(40)
        self.team2.set_runs(41)

        self.game.add_team(self.team1)
        self.game.add_team(self.team2)

        target = self.game.get_target_score(self.team1)

        self.assertTrue(target == 41)

        print("Get target score for a specific team test case for Game executed successfully", end="\n\n")

    def test_play(self):
        self.team2.set_runs(40)

        p1 = Player('Kirat Boli', batting_order=1, probability_distribution=[0, 0, 0, 0, 0, 0, 100, 0])
        p2 = Player('N S Nodhi', batting_order=2, probability_distribution=[0, 0, 0, 0, 0, 0, 100, 0])


        self.team1.add_players(p1)
        self.team1.add_players(p2)

        self.game.add_team(self.team1)
        self.game.add_team(self.team2)

        result_object = self.game.play()

        self.assertEqual(result_object["winning_team"], self.team1)
        self.assertEqual(result_object["losing_team"], self.team2)

    def tearDown(self):
        print("Test cases executed successfully for Game", end="\n\n")