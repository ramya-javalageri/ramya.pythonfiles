from pp1 import *


class IPLStatsManager(ABC):
    def __init__(self, csv_file):
        pass

    @abstractmethod
    def _initialize_empty_dataframe(self):
        pass

    @abstractmethod
    def add_match_data(self):
        pass

    @abstractmethod
    def get_player_stats(self, player_id):
        pass

    @abstractmethod
    def analyze_player(self, player_id):
        pass

    @abstractmethod
    def provide_feedback(self, player_id):
        pass

    @abstractmethod
    def plot_performance(self, player_id):
        pass

