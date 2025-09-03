import pandas as pd
import matplotlib.pyplot as plt

class Player:
    def __init__(self, player_id, name, team):
        self.player_id = player_id
        self.name = name
        self.team = team
        self.matches_played = 0
        self.runs_scored = 0
        self.wickets_taken = 0
        self.catches_taken = 0
        self.runouts_effected = 0

    def update_performance(self, runs, wickets, catches, runouts):
        self.matches_played += 1
        self.runs_scored += runs
        self.wickets_taken += wickets
        self.catches_taken += catches
        self.runouts_effected += runouts

    def get_performance(self):
        return {
            'Matches Played': self.matches_played,
            'Runs Scored': self.runs_scored,
            'Wickets Taken': self.wickets_taken,
            'Catches Taken': self.catches_taken,
            'Runouts Effected': self.runouts_effected
        }

class Team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name
        self.players = {}

    def add_player(self, player):
        self.players[player.player_id] = player

    def get_players(self):
        return self.players

class IPL:
    def __init__(self):
        self.teams = {}

    def add_team(self, team):
        self.teams[team.team_id] = team

    def get_team(self, team_id):
        return self.teams[team_id]

    def analyze_player_performance(self, player_id):
        for team in self.teams.values():
            if player_id in team.players:
                player = team.players[player_id]
                performance = player.get_performance()
                print(performance)
                return

    def plot_player_performance(self, player_id):
        for team in self.teams.values():
            if player_id in team.players:
                player = team.players[player_id]
                performance = player.get_performance()
                labels = list(performance.keys())
                values = list(performance.values())
                plt.bar(labels, values)
                plt.xlabel('Performance Metrics')
                plt.ylabel('Values')
                plt.title('Player Performance')
                plt.show()
                return

# Example usage
ipl = IPL()

team1 = Team(1, 'Mumbai Indians')
team2 = Team(2, 'Chennai Super Kings')

player1 = Player(1, 'Rohit Sharma', 'Mumbai Indians')
player2 = Player(2, 'MS Dhoni', 'Chennai Super Kings')

team1.add_player(player1)
team2.add_player(player2)

ipl.add_team(team1)
ipl.add_team(team2)

player1.update_performance(50, 0, 1, 0)
player2.update_performance(30, 2, 0, 1)

ipl.analyze_player_performance(1)
ipl.plot_player_performance(1)

