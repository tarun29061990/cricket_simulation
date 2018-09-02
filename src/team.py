from commentary import Commentary
from game import Game


class Team():
    def __init__(self, name):
        self.name = name
        self.no_of_players = 0
        self.total_players = []

        self.active_players = []

        # 0 - batting
        # 1 - fielding
        self.state = 0

        # index to keep track of the player
        self.player_index = 0

        self.current_player = object()
        self.current_active_player_index = 0

        # Each team total runs
        self.runs_scored = 0

        # total overs and each team has to play
        self.total_overs = 0

        self.balls_per_over = 0

        # Each team total balls and total overs
        self.total_balls_played = 0

        self.total_overs_played = 0

    def add_players(self, p):
        if p not in self.total_players:
            self.total_players.append(p)
            self.no_of_players += 1

    def get_players(self):
        return self.total_players

    def set_state(self, state):
        if state is not None:
            self.state = state

    def get_state(self):
        return self.state

    def get_runs(self):
        return self.runs_scored

    def set_runs(self, runs):
        if runs is not None:
            self.runs_scored += runs

    def get_next_player(self):
        self.player_index += 1
        if self.player_index < len(self.total_players):
            return self.total_players[self.player_index]

    def set_active_players(self):
        # setting state of first two players to active
        self.total_players[0].set_state(1)
        self.total_players[1].set_state(1)

        self.active_players = []
        for p in self.total_players:
            if p.state:
                self.active_players.append(p)

        self.player_index = self.total_players.index(self.active_players[len(self.active_players) - 1])

    def play(self, overs, balls_per_over, target):
        self.total_overs = overs
        self.balls_per_over = balls_per_over

        # set state of a team to batting
        self.set_state(1)

        # set active players
        self.set_active_players()

        runs_to_win = target - self.runs_scored

        current_over = 0
        while current_over < overs and runs_to_win >= 0:
            if target:
                Commentary.generate_commentary_over_wise(self.total_overs - current_over, runs_to_win)
            else:
                Commentary.generate_commentary_over_wise(self.total_overs - current_over)

            current_ball = 1
            while current_ball <= balls_per_over and runs_to_win >= 0:

                self.total_balls_played += 1

                self.current_player = self.active_players[self.current_active_player_index]

                if self.current_player.get_position_on_pitch() == 0:
                    self.current_player.set_position_on_pitch(1)

                runs = self.current_player.play(Game.available_runs)

                # Generate ball by ball commentary
                Commentary.generate_commentary(current_over, current_ball, self.current_player.name, runs)

                # updating total runs of a team
                if runs is not None:
                    self.set_runs(runs)
                    runs_to_win = target - self.runs_scored

                if runs == 1 or runs == 3 or runs == 5:
                    self.change_positions()

                # when a player is out
                if runs is None:
                    # setting current player state to out i.e. 0
                    self.current_player.set_state(0)

                    # changing active players and setting it to next player
                    next_player = self.get_next_player()
                    if next_player:
                        self.active_players[self.current_active_player_index] = next_player
                    else:
                        return self.runs_scored

                current_ball += 1

            current_over += 1

            self.total_overs_played += 1

            # change position after every over
            self.change_positions()

        # set state of the team again
        self.set_state(1)

        return self.runs_scored

    def change_positions(self):
        # changing position of player
        self.current_player.change_position()

        # changing active player index
        self.current_active_player_index = self.current_active_player_index ^ 1