from commentary import Commentary


class Game():
    # 0 - dot ball
    # None - Out
    # rest are self explanatory
    available_runs = [0, 1, 2, 3, 4, 5, 6, None]

    def __init__(self, name, overs, balls_per_over):
        self.name = name
        self.overs = overs
        self.balls_per_over = balls_per_over
        self.teams = []

    def add_team(self, team):
        if team not in self.teams:
            self.teams.append(team)
        return team

    def get_teams(self):
        return self.teams

    def start_toss(self):
        # Let's say Chennai(team2) won the toss and played their innings
        # Now it's Bengaluru(team1) turn to play
        if len(self.teams):
            return self.teams[0]

    def get_target_score(self, team_to_play):
        for t in self.teams:
            if t != team_to_play:
                return t.runs_scored

    def play(self):
        team_to_play = self.start_toss()

        target = self.get_target_score(team_to_play)

        team_to_play.play(self.overs, self.balls_per_over, target)  # for 1st inning target will be 0

        winning_team = self.check_who_won()

        losing_team = None
        if winning_team:
            losing_team = self.teams[self.teams.index(winning_team) ^ 1]

        return {
            "winning_team": winning_team,
            "losing_team": losing_team
        }

    def check_who_won(self):
        # only two teams will play
        team1 = self.teams[0]
        team2 = self.teams[1]

        if team1.runs_scored > team2.runs_scored:
            winning_team = team1
        elif team1.runs_scored < team2.runs_scored:
            winning_team = team2
        else:
            return None  # match drawn

        return winning_team
