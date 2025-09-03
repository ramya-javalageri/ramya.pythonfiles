import pandas as pd
import matplotlib.pyplot as plt
import os

class IPLStatsManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        try:
            self.stats = pd.read_csv("E:/python/internship6thsem/ipl_data.csv")
        except FileNotFoundError:
            self.stats = pd.DataFrame(columns=['player_id', 'player_name', 'team', 'match_date', 'runs', 'wickets', 'catches'])

    # Add new match record
    def add_match_data(self, player_id, player_name, team, match_date, runs, wickets, catches):
        new_record = {
            'player_id': player_id,
            'player_name': player_name,
            'team': team,
            'match_date': match_date,
            'runs': runs,
            'wickets': wickets,
            'catches': catches
        }
        self.stats = pd.concat([self.stats, pd.DataFrame([new_record])], ignore_index=True)
        self.stats.to_csv(self.csv_file, index=False)
        print(f"Added match data for {player_name}")

    # Get stats for a specific player
    def get_player_stats(self, player_id):
        player_data = self.stats[self.stats['player_id'] == player_id]
        if player_data.empty:
            return "No data for this player."
        return player_data

    # Analyze player performance
    def analyze_player(self, player_id):
        player_data = self.get_player_stats(player_id)
        if isinstance(player_data, str):
            return player_data

        total_matches = len(player_data)
        total_runs = player_data['runs'].sum()
        avg_runs = player_data['runs'].mean()
        max_runs = player_data['runs'].max()

        return (
            f"Player: {player_data.iloc[0]['player_name']} ({player_data.iloc[0]['team']})\n"
            f"Total Matches: {total_matches}\n"
            f"Total Runs: {total_runs}\n"
            f"Average Runs: {avg_runs:.2f}\n"
            f"Highest Runs: {max_runs}\n"
        )

    # Provide feedback
    def provide_feedback(self, player_id):
        player_data = self.get_player_stats(player_id)
        if isinstance(player_data, str):
            return player_data

        avg_runs = player_data['runs'].mean()
        if avg_runs >= 50:
            return "Excellent form!"
        elif avg_runs >= 30:
            return "Good, but needs consistency."
        else:
            return "Needs improvement."

    # Plot performance over time
    def plot_performance(self, player_id):
        player_data = self.get_player_stats(player_id)
        if isinstance(player_data, str):
            print(player_data)
            return

        player_data['match_date'] = pd.to_datetime(player_data['match_date'])
        player_data = player_data.sort_values('match_date')

        plt.figure(figsize=(10, 5))
        plt.plot(player_data['match_date'], player_data['runs'], marker='o', color='blue')
        plt.title(f"{player_data.iloc[0]['player_name']} Performance")
        plt.xlabel("Match Date")
        plt.ylabel("Runs")
        plt.grid(True)
        plt.show()

csv_file = "E:/python/internship6thsem/ipl_data.csv"
manager = IPLStatsManager(csv_file)

# Add some match data
manager.add_match_data(player_id=1, player_name="Virat Kohli", team="RCB", match_date="2025-03-05", runs=85, wickets=0, catches=1)
manager.add_match_data(player_id=2, player_name="Rohit Sharma", team="MI", match_date="2025-03-06", runs=50, wickets=1, catches=2)

# Analyze player data
print(manager.analyze_player(1))  # Analyzing Virat Kohli
print(manager.analyze_player(2))  # Analyzing Rohit Sharma

# Provide performance feedback
print(manager.provide_feedback(1))  # Feedback for Virat Kohli
print(manager.provide_feedback(2))  # Feedback for Rohit Sharma

# Plot performance for a player
manager.plot_performance(1)
