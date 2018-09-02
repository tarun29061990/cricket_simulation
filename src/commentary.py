class Commentary():
    def __init__(self):
        return

    @staticmethod
    def generate_commentary(current_over, current_ball, name, run):

        if run is not None:
            message_string = str(current_over) + "." + str(current_ball) + " " + name + " scores " + str(run) + " run"
            print(message_string)
        else:
            message_string = str(current_over) + "." + str(current_ball) + " " + name + " out"
            print(message_string)

        return message_string

    @staticmethod
    def generate_commentary_over_wise(overs_left, runs_to_win=""):
        print("", end="\n")

        message_string = str(overs_left)+" overs remaining and "+str(runs_to_win)+" runs to win"
        print(message_string)

        return message_string

    @staticmethod
    def generate_summary(winning_team, losing_team):
        print("", end="\n\n")

        if winning_team is not None and losing_team is not None:
            Commentary.generate_team_summary(winning_team, 1)
            Commentary.generate_team_summary(losing_team, 0)

        else:
            print("Match Drawn")
            return "Match Drawn"

    @staticmethod
    def generate_team_summary(team, is_winner):
        print("", end="\n\n")

        winning_text = "won" if is_winner else "lost"
        wickets_left_message = ''

        if team.player_index < len(team.total_players):
            wickets_left = len(team.total_players) - team.player_index
            wickets_left_message = "by " + str(wickets_left) + " wicket"

        total_balls = team.total_overs * team.balls_per_over

        remaining_balls = total_balls - team.total_balls_played

        balls_left_message = ""
        if remaining_balls:
            remaining_overs = int(remaining_balls / team.balls_per_over)
            remaining_balls = int(remaining_balls % team.balls_per_over)

            if remaining_overs > 0:
                balls_left_message = "and " + str(remaining_overs) + " over " + str(
                    remaining_balls) + " balls remaining"
            else:
                balls_left_message = "and " + str(remaining_balls) + " balls remaining"

        message_string = team.name + " " + winning_text+" " + wickets_left_message + " " + balls_left_message
        print(message_string)

        if len(team.total_players):
            total_players = team.total_players
            for p in total_players:
                not_out_message = ""
                if p.state:
                    not_out_message = "*"

                player_message_string = p.name + " - " + str(p.runs) + not_out_message + " (" + str(p.balls_played) + " balls )"
                print(player_message_string)

                message_string += " "+player_message_string

        return message_string
