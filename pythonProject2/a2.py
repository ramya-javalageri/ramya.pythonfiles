from a1 import *
import json
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

    def analyze_all_feedback_for_improvement(self):
        # Initialize variables to store counts
        good_feedback_count = 0
        better_feedback_count = 0
        bad_feedback_count = 0

        # Iterate over feedback data
        for feedback in self.feedback_data.values():
            ratings_dict = feedback.ratings
            if isinstance(ratings_dict, dict):
                for rating_value in ratings_dict.values():
                    if rating_value == "good":
                        good_feedback_count += 1
                    elif rating_value == "better":
                        better_feedback_count += 1
                    elif rating_value == "bad":
                        bad_feedback_count += 1

        total_feedback_count = len(self.feedback_data)

        # Calculate percentages
        if total_feedback_count > 0:
            good_percentage = (good_feedback_count / total_feedback_count) * 100
            better_percentage = (better_feedback_count / total_feedback_count) * 100
            bad_percentage = (bad_feedback_count / total_feedback_count) * 100
        else:
            good_percentage = 0
            better_percentage = 0
            bad_percentage = 0

        return {
            "Good Feedback Percentage": good_percentage,
            "Better Feedback Percentage": better_percentage,
            "Bad Feedback Percentage": bad_percentage
        }

    @classmethod
    def update_question(cls, index, new_question):
        if 0 <= index < len(cls.questions):
            cls.questions[index] = new_question
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
class FeedbackData(Feedback):
    def __init__(self, feedback_id, ratings):
        super().__init__(feedback_id, ratings)



def collect_project_feedback():
    feedback_id = input("Enter feedback ID: ")
    ratings = {}
    for i, q in enumerate(Questionnaire.questions):
        new_question = input(f"Current question: {q}\nEnter updated question or press Enter to keep it the same: ")
        if new_question.strip():  # Check if input is not empty
            if not Questionnaire.update_question(i, new_question):
                print("Invalid index provided, question not updated.")
        ratings[q] = input(f"{q} \n Enter rating (good/bad/better): ")
    return FeedbackData(feedback_id, ratings)


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
                            analysis_results = feedback_system.analyze_all_feedback_for_improvement()
                            print("Analysis Results:")
                            for key, value in analysis_results.items():
                                print(f"{key}: {value}%")

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
