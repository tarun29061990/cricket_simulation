from game import Game
from player import Player
from team import Team
from commentary import Commentary

game = Game('cricketT20', overs=4, balls_per_over=6)

team1 = Team('Bengaluru')

team2 = Team('Chennai')
team2.set_runs(40)

p1 = Player('Kirat Boli', batting_order = 1, probability_distribution=[5, 30, 25, 10, 15, 1, 9, 5] )
p2 = Player('N S Nodhi', batting_order = 2, probability_distribution=[10, 40, 20, 5, 10, 1, 4, 10] )
p3 = Player('R Rumrah', batting_order = 3, probability_distribution=[20, 30, 15, 5, 5, 1, 4, 20] )
p4 = Player('Shashi Henra', batting_order = 4, probability_distribution=[30, 25, 5, 0, 5, 1, 4, 30] )

team1.add_players(p1)
team1.add_players(p2)
team1.add_players(p3)
team1.add_players(p4)

game.add_team(team1)
game.add_team(team2)

result_object = game.play()

Commentary.generate_summary(result_object["winning_team"], result_object["losing_team"])
