import sys, os
import copy

from unittest import TestCase

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

from team import Team
from player import Player

class TeamTestCase(TestCase):
    def setUp(self):
        print("",end='\n\n')
        print("Running test cases for Team", end="\n\n")
        self.t1 = Team('team1')

    def test_create_team(self):

        self.assertEqual('team1', self.t1.name)
        print("Create Team test case executed successfully", end='\n\n')

    def test_add_player(self):
        players = copy.copy(self.t1.get_players())

        p1 = Player('Kirat Boli', batting_order = 1, probability_distribution=[5, 30, 25, 10, 15, 1, 9, 5] )
        self.t1.add_players(p1)

        self.assertEqual(len(players)+1, len(self.t1.total_players))

        print("Add Player to the Team test case executed successfully", end='\n\n')

    def test_get_next_player(self):
        p1 = Player('Kirat Boli', batting_order=1, probability_distribution=[5, 30, 25, 10, 15, 1, 9, 5])
        p2 = Player('N S Nodhi', batting_order=2, probability_distribution=[10, 40, 20, 5, 10, 1, 4, 10])

        self.t1.add_players(p1)
        self.t1.add_players(p2)

        next_player = self.t1.get_next_player()
        self.assertEqual(p2.name, next_player.name)

        print("Get Next Player of the Team test case executed successfully", end='\n\n')

    def test_set_active_players(self):
        active_players = self.t1.active_players

        p1 = Player('Kirat Boli', batting_order=1, probability_distribution=[5, 30, 25, 10, 15, 1, 9, 5])
        p2 = Player('N S Nodhi', batting_order=2, probability_distribution=[10, 40, 20, 5, 10, 1, 4, 10])

        self.t1.add_players(p1)
        self.t1.add_players(p2)

        self.t1.set_active_players()

        self.assertEqual(len(active_players)+2, len(self.t1.active_players))

        print("Set Active Players of the Team test case executed successfully", end='\n\n')

    def test_play(self):
        p1 = Player('Kirat Boli', batting_order=1, probability_distribution=[5, 30, 25, 10, 15, 1, 9, 5])
        p2 = Player('N S Nodhi', batting_order=2, probability_distribution=[10, 40, 20, 5, 10, 1, 4, 10])
        p3 = Player('R Rumrah', batting_order=3, probability_distribution=[20, 30, 15, 5, 5, 1, 4, 20])
        p4 = Player('Shashi Henra', batting_order=4, probability_distribution=[30, 25, 5, 0, 5, 1, 4, 30])

        self.t1.add_players(p1)
        self.t1.add_players(p2)
        self.t1.add_players(p3)
        self.t1.add_players(p4)

        self.t1.play(overs=4, balls_per_over=6, target=40)

        self.assertTrue(0 <= self.t1.runs_scored <= 46)

        print("Play of the Team test case executed successfully", end='\n\n')

    def tearDown(self):
        print("Test cases executed successfully for Team", end="\n\n")