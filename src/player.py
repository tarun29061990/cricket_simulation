import numpy as np

class Player():
    def __init__(self, name, batting_order, probability_distribution):
        self.name = name
        self.runs = 0
        self.balls_played = 0

        # 0 - Out
        # 1 - Active
        self.state = 0

        # 0 - striker end
        # 1 - non striker end
        self.position_on_pitch = 0
        self.batting_order = batting_order

        self.runs_probability_distribution = []
        self.set_probability_distribution(probability_distribution)

    def set_probability_distribution(self, probability_distribution):
        for p in probability_distribution:
            self.runs_probability_distribution.append(p/100)

    def get_probability_distribution(self):
        return self.runs_probability_distribution

    def set_state(self, state):
        self.state = state
        return

    def get_state(self):
        return self.state

    def add_runs(self, runs):
        if runs is not None:
            self.runs += runs
            return self.runs

    def get_runs(self):
        return self.runs

    def get_balls_played(self):
        return self.balls_played

    def set_balls_played(self):
        self.balls_played += 1

    def get_position_on_pitch(self):
        return self.position_on_pitch

    def set_position_on_pitch(self, position):
        self.position_on_pitch = position

    def change_position(self):
        self.set_position_on_pitch(self.get_position_on_pitch() ^ 1)

    def play(self, total_available_runs):
        runs = np.random.choice(total_available_runs, p=self.runs_probability_distribution)
        self.add_runs(runs)
        self.set_balls_played()
        return runs
