import csv
from abc import ABC, abstractmethod

class Questionnaire:
    questions = ["time management:",
                 " rate the work so far:",
                 "communication between the team members",
                 "How satisfied are you with current project process?",
                 "What do you feel about the project approch?"]

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Feedback(ABC):
    def __init__(self, feedback_id, ratings):
        self.feedback_id = feedback_id
        self.ratings = ratings

class FeedbackData(Feedback):
    def __init__(self, feedback_id, ratings):
        super().__init__(feedback_id, ratings)

class FeedbackCollectionSystem(ABC):
    def __init__(self):
        self._feedback_data = {}
        self._users = {}
        self._admin_password = "priya@123"
        self.load_users()
        self.load_feedback()

    @abstractmethod
    def load_users(self):
        pass

    @abstractmethod
    def save_users(self):
        pass

    @abstractmethod
    def authenticate_user(self, username, password):
        pass

    @abstractmethod
    def add_user(self, user, admin_password):
        pass

    @abstractmethod
    def delete_user(self, username, admin_password):
        pass

    @abstractmethod
    def update_user_password(self, username, new_password, admin_password):
        pass

    @abstractmethod
    def load_feedback(self):
        pass

    @abstractmethod
    def save_feedbacks(self):
        pass

    @abstractmethod
    def add_feedback(self, feedback):
        pass

    @abstractmethod
    def get_feedback(self, feedback_id):
        pass

    @abstractmethod
    def analyze_all_feedback_for_improvement(self):
        pass

    @abstractmethod
    def update_feedback(self, feedback_id, new_content):
        pass

    @abstractmethod
    def delete_feedback(self, feedback_id):
        pass


