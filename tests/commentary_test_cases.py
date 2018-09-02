import sys, os
import copy

from unittest import TestCase

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

from team import Team
from player import Player
from commentary import Commentary


class CommentaryTestCase(TestCase):
    def setUp(self):
        print("", end='\n\n')
        print("Running test cases for Commentary", end="\n\n")

    def test_generate_commentory(self):
        test_message_string = "3.2 Test Player scores 2 run"
        test_out_message_string = "3.2 Test Player out"

        message_string = Commentary.generate_commentary(current_over=3, current_ball=2, name='Test Player', run=2)
        message_out_string = Commentary.generate_commentary(current_over=3, current_ball=2, name='Test Player', run=None)

        self.assertEqual(test_message_string,message_string)
        self.assertEqual(test_out_message_string, message_out_string)

        print("Generate Commentory test case executed successfully", end='\n\n')

    def test_generate_commentary_over_wise(self):
        test_message_string = "1 overs remaining and 11 runs to win"

        message_string = Commentary.generate_commentary_over_wise(overs_left=1, runs_to_win=11)

        self.assertEqual(test_message_string, message_string)

        print("Generate Commentory over wise test case executed successfully", end='\n\n')

    def test_generate_summary(self):
        test_message_string = "Match Drawn"

        message_string = Commentary.generate_summary(losing_team=None, winning_team=None)

        self.assertEqual(test_message_string, message_string)

        print("Generate Summary for match drawn test case executed successfully", end='\n\n')

    def test_generate_winning_team_summary(self):
        test_winning_message_string = "team1 won by 1 wicket and 3 over 0 balls remaining Kirat Boli - 36* (6 balls ) N S Nodhi - 0* (0 balls )"

        team1 = Team("team1")

        p1 = Player('Kirat Boli', batting_order=1, probability_distribution=[0, 0, 0, 0, 0, 0, 100, 0])
        p2 = Player('N S Nodhi', batting_order=2, probability_distribution=[0, 0, 0, 0, 0, 0, 100, 0])

        team1.add_players(p1)
        team1.add_players(p2)

        team1.play(overs=4, balls_per_over=6, target=35)

        winning_message_string = Commentary.generate_team_summary(team1, is_winner=1)

        self.assertEqual(test_winning_message_string, winning_message_string)

        print("Generate Summary for winning team test case executed successfully", end='\n\n')

    def test_generate_losing_team_summary(self):
        test_losing_message_string = "team2 lost by 1 wicket  Kirat Boli - 36* (6 balls ) N S Nodhi - 0* (0 balls )"

        team2 = Team("team2")

        p3 = Player('Kirat Boli', batting_order=1, probability_distribution=[0, 0, 0, 0, 0, 0, 100, 0])
        p4 = Player('N S Nodhi', batting_order=2, probability_distribution=[0, 0, 0, 0, 0, 0, 100, 0])

        team2.add_players(p3)
        team2.add_players(p4)

        team2.play(overs=1, balls_per_over=6, target=40)

        losing_message_string = Commentary.generate_team_summary(team2, is_winner=0)

        self.assertEqual(test_losing_message_string, losing_message_string)

        print("Generate Summary for losing team test case executed successfully", end='\n\n')

    def tearDown(self):
        print("Test cases executed successfully for Commentory", end="\n\n")
