import csv
from abc import ABC, abstractmethod

question = ["How much does the project is based on the real-life issues?",
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
    def analyze_feedback_for_improvement(self, feedback_id):
        pass

    @abstractmethod
    def update_feedback(self, feedback_id, new_content):
        pass

    @abstractmethod
    def delete_feedback(self, feedback_id):
        pass


class FeedbackCollectionSystemImplementation(FeedbackCollectionSystem):
    def load_users(self):
        with open("E:/python/pythonProject2/users.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                username, password = row
                self.users[username] = User(username, password)

    def save_users(self):
        with open("E:/python/pythonProject2/users.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Password"])
            for user in self.users.values():
                writer.writerow([user.username, user.password])

    def authenticate_usr(self, username, password):
        if username in self.users and self.users[username].password == password:
            return True
        else:
            return False

    def add_user(self, user, admin_password):
        if admin_password == self.admin_password:
            self.users[user.username] = user
            self.save_users()
            return True
        else:
            return False

    def delete_user(self, username, admin_password):
        if admin_password == self.admin_password:  # Check admin password
            if username in self.users:
                del self.users[username]
                self.save_users()
                return True
        return False

    def update_user_password(self, username, new_password, admin_password):
        if admin_password == self.admin_password:  # Check admin password
            if username in self.users:
                self.users[username].password = new_password
                self.save_users()
                return True
        return False

    def load_feedback(self):
        with open("E:/python/pythonProject2/feedback.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                feedback_id, ratings = row
                self.feedback_data[feedback_id] = FeedbackImplementation(feedback_id, ratings)

    def save_feedbacks(self):
        with open("E:/python/pythonProject2/feedback.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Feedback id", "Ratings"])
            for feedback_ in self.feedback_data.values():
                writer.writerow([feedback_.feedback_id, feedback_.ratings])

    def add_feedback(self, feedback):
        if feedback.feedback_id in self.feedback_data:
            return False
        else:
            self.feedback_data[feedback.feedback_id] = feedback
            self.save_feedbacks()
            return True

    def get_feedback(self, feedback_id):
        feed_ = self.feedback_data.get(feedback_id)
        return feed_.ratings

    def analyze_feedback_for_improvement(self, feedback_id):
        # Analyze feedback data to identify areas for improvement
        rating_score = 0
        feed_dct = {}

        feed_ = self.feedback_data.get(feedback_id)
        ratings__ = feed_.ratings.split(",")
        for i in ratings__:
            feed_dct[i.split(":")[0]] = i.split(":")[1].strip()

        for rating__ in feed_dct.values():
            if rating__.lower() == "'good'":
                rating_score += 2
            elif rating__.lower() == "'bad'":
                rating_score += 0.5
            elif rating__.lower() == "'better":
                rating_score += 1

        print("Feedback analysis for improvement:")
        if 8 <= rating_score <= 10:
            print("Good")
        elif 5 <= rating_score <= 7.9:
            print("Better, But need to improve")
        elif 0 <= rating_score <= 4.9:
            print("Need to Improve ")

    def update_feedback(self, feedback_id, new_content):
        if feedback_id in self.feedback_data:
            self.feedback_data[feedback_id].content = new_content
            self.save_feedbacks()
            return True
        else:
            return False

    def delete_feedback(self, feedback_id):
        if feedback_id in self.feedback_data:
            del self.feedback_data[feedback_id]
            self.save_feedbacks()
            return True
        else:
            return False


class FeedbackImplementation(Feedback):
    def __init__(self, feedback_id, ratings):
        super().__init__(feedback_id, ratings)


def collect_project_feedback():
    feedback_id = input("Enter feedback ID: ")
    ratings = {}
    for q in question:
        rating = input(f"{q} \n Enter rating (good/bad/better): ")
        ratings[q] = rating
    return FeedbackImplementation(feedback_id, ratings)


def manage_users(feedback_system):
    while True:
        print("User Management")
        print("1. Add User")
        print("2. Delete User")
        print("3. Update User Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter new username: ")
            password = input("Enter password: ")
            admin_password = input("Enter admin password: ")
            if feedback_system.add_user(User(username, password), admin_password):
                print("User added successfully")
            else:
                print("Admin password incorrect")
        elif choice == "2":
            username = input("Enter username to delete: ")
            admin_password = input("Enter admin password: ")
            if feedback_system.delete_user(username, admin_password):
                print("User deleted successfully")
            else:
                print("Admin password incorrect or user not found")
        elif choice == "3":
            username = input("Enter username to update password: ")
            new_password = input("Enter new password: ")
            admin_password = input("Enter admin password: ")
            if feedback_system.update_user_password(username, new_password, admin_password):
                print("User password updated successfully")
            else:
                print("Admin password incorrect or user not found")
        elif choice == "4":
            print("\n----👍Thank you👍-----\n")
            break
        else:
            print('enter correct choice')


feedback_system = FeedbackCollectionSystemImplementation()
while True:
    login_option = int(input("Enter an option:\n1. Admin Access. \n2. Give feedback. \n3. Exit.\n"))

    if login_option == 1:
        while True:
            print("\n 1.add or remove \n 2.admin login \n 3.Exit")
            op = int(input())
            if op == 1:
                admin_pwd = input("Enter the admin password: ")
                if admin_pwd == feedback_system.admin_password:
                    print("---Welcome---")
                    manage_users(feedback_system)

            elif op == 2:
                admin_username = input(" Enter admin username?")
                pwd = input(" Enter admin password?")
                if admin_username == 'admin' and pwd == feedback_system.admin_password:
                    while True:
                        print("Entering into the Feedback management system-----")
                        print("Enter an option: \n 1. Read Feedback\n 2. Update Feedback \n 3. Delete Feedback \n 4. Analyse Feedback \n 5.Exit")
                        opt = input()
                        if opt == "1":
                            feed_id = input("Enter the Feedback_id to read")
                            print(feedback_system.get_feedback(feed_id))
                        elif opt == "2":
                            feed = collect_project_feedback()
                            if feedback_system.update_feedback(feed.feedback_id, feed.ratings):
                                print(f"Successfully updated the feedback for {feed.feedback_id}")
                            else:
                                print(f"Failed to update the feedback for {feed.feedback_id}")
                        elif opt == "3":
                            f_id = input("Enter the Feedback_id to delete the feed back")
                            if feedback_system.delete_feedback(f_id):
                                print("Successfully deleted the feedback")
                            else:
                                print("Failed to delete the feedback")
                        elif opt == "4":
                            feed_id = input("Enter feedback id for anaylsis\n")
                            feedback_system.analyze_feedback_for_improvement(feed_id)
                        elif opt == "5":
                            print("\n----👍Thank you👍-----\n")
                            break
                        else:
                            print('Enter valid option')

            elif op == 3:
                print("\n----👍Thank you👍-----\n")
                break

            else:
                print("correct option")

    if login_option == 2:
        username = input("Please enter your username: ")
        passwrd = input("Please enter your password: ")
        if feedback_system.authenticate_usr(username, passwrd):
            print("-----welcome to the Feedback---")
            feedback = collect_project_feedback()
            if feedback_system.add_feedback(feedback):
                print("\nFeedback created successfully\n")
                print("\n----👍Thank you👍-----\n")
            else:
                print("Failed to create the feedback")
        else:
            print("Username or password are incorrect")

    elif login_option == 3:
        print("\n----👍Thank you👍-----\n")
        break
    else:
        print("Enter correct option")
