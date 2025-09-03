import csv
from abc import ABC, abstractmethod

class Questionnaire:
    questions = ["How much does the project is based on the real-life issues?",
                 "Whether all the team members are interactive?",
                 "Who was the communication between the team members?",
                 "Who is the communication between you and guide?",
                 "Whether the whole project had made you learn something?"]





class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Feedback(ABC):
    def __init__(self, feedback_id, ratings):
        self.feedback_id = feedback_id
        self.ratings = ratings


class FeedbackCollectionSystem(ABC):
    def __init__(self):
        self.feedback_data = {}
        self.users = {}
        self.admin_password = "admin@123"  # Admin password
        self.load_users()
        self.load_feedback()

    @abstractmethod
    def load_users(self):
        pass

    @abstractmethod
    def save_users(self):
        pass

    @abstractmethod
    def authenticate_usr(self, username, password):
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
    def update_question(cls, index, new_question):
        pass

    @abstractmethod
    def delete_feedback(self, feedback_id):
        pass





