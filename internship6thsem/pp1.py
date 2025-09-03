import os
import pandas as pd
import matplotlib.pyplot as plt
from getpass import getpass
import csv
from abc import ABC,abstractmethod
class IPLStatsManager(ABC):
    def __init__(self, csv_file):
        self.csv_file = csv_file
        # Check if file exists and has data
        if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
            try:
                self.stats = pd.read_csv(csv_file)
            except pd.errors.EmptyDataError:
                print("Warning: CSV file is empty. Initializing with an empty DataFrame.")
                self._initialize_empty_dataframe()
        else:
            print("CSV file not found or empty. Creating a new file.")
            self._initialize_empty_dataframe()
            self.stats.to_csv(csv_file, index=False)  # Save empty CSV file

    def _initialize_empty_dataframe(self):
        """Initializes an empty DataFrame with the required columns."""
        self.stats = pd.DataFrame(columns=['player_id', 'player_name', 'team', 'match_date', 'runs', 'wickets', 'catches'])

    # Add new match record
    def add_match_data(self):
        """Takes user input for a new match record."""
        try:
            player_id = int(input("Enter Player ID: "))
            player_name = input("Enter Player Name: ")
            team = input("Enter Team Name: ")
            match_date = input("Enter Match Date (YYYY-MM-DD): ")
            runs = int(input("Enter Runs Scored: "))
            wickets = int(input("Enter Wickets Taken: "))
            catches = int(input("Enter Catches Taken: "))

            # Check if player ID already exists
            existing_player_data = self.stats[self.stats['player_id'] == player_id]
            if not existing_player_data.empty:
                existing_player_name = existing_player_data.iloc[0]['player_name']
                if player_name.lower() != existing_player_name.lower():
                    print(f"⚠ Warning: Player ID {player_id} already exists with name '{existing_player_name}'. Please use the correct player name.")
                    return

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
            print(f"✅ Match data added for {player_name}")
        except ValueError:
            print("❌ Invalid input! Please enter the correct data types.")

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
        if avg_runs >= 60:
            return "🔥 Excellent form!"
        elif avg_runs >= 45:
            return "👍 Good, but needs consistency."
        else:
            return "⚠ Needs improvement."

    # Plot performance over time
    def plot_performance(self, player_id):
        player_data = self.get_player_stats(player_id)
        if isinstance(player_data, str):
            print(player_data)
            return
        # Create a copy to avoid modifying the original DataFrame
        player_data = player_data.copy()
        # Convert match_date to datetime format
        player_data['match_date'] = pd.to_datetime(player_data['match_date'])
        # Sort data by date
        player_data = player_data.sort_values('match_date')
        # Plot player performance
        plt.figure(figsize=(10, 5))
        plt.plot(player_data['match_date'], player_data['runs'], marker='o', color='blue')
        plt.title(f"{player_data.iloc[0]['player_name']} Performance")
        plt.xlabel("Match Date")
        plt.ylabel("Runs")
        plt.grid(True)
        plt.show()


while True:
    ip = input("login or logout:")
    if ip=='login':
        username=input("Enter user name:").lower()
        password=input("Enter password:").lower()
        if username=='admin' :
            if password=='123':
                csv_file = r"E:/python/internship6thsem/ipl1_data.csv"

                # Initialize the IPLStatsManager
                manager =IPLStatsManager(csv_file)
                # User Menu for Interaction
                while True:
                    print("\n🏏 IPL Stats Manager 🏏")
                    print("1️⃣ Add Match Data")
                    print("2️⃣ Analyze Player")
                    print("3️⃣ Provide Feedback")
                    print("4️⃣ Plot Player Performance")
                    print("5️⃣ Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        manager.add_match_data()
                    elif choice == "2":
                        player_id = int(input("Enter Player ID to analyze: "))
                        print(manager.analyze_player(player_id))
                    elif choice == "3":
                        player_id = int(input("Enter Player ID for feedback: "))
                        print(manager.provide_feedback(player_id))
                    elif choice == "4":
                        player_id = int(input("Enter Player ID to plot performance: "))
                        manager.plot_performance(player_id)
                    elif choice == "5":
                        print("📢 Exiting... Thank you!")
                        break
                    else:
                        print("❌ Invalid choice! Please enter a valid option.")

            else:
                print("Enter valid password")
        else:
            print("Enter valid username")

    elif ip=='logout':
        print("Thank you")
        break

    else:
        print("Enter valid input")


