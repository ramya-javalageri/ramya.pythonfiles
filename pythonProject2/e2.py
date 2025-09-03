from e1 import *
class FeedbackSystem(FeedbackCollectionSystem):
    def load_users(self):
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                username, password = row
                self._users[username] = User(username, password)

    def save_users(self):
        with open("users.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Password"])
            for user in self._users.values():
                writer.writerow([user.username, user.password])

    def authenticate_user(self, username, password):
        if username in self._users and self._users[username].password == password:
            return True
        else:
            return False

    def add_user(self, user, admin_password):
        if admin_password == self._admin_password:
            self._users[user.username] = user
            self.save_users()
            return True
        else:
            return False

    def delete_user(self, username, admin_password):
        if admin_password == self._admin_password and username in self._users:
            del self._users[username]
            self.save_users()
            return True
        return False

    def update_user_password(self, username, new_password, admin_password):
        if admin_password == self._admin_password and username in self._users:
            self._users[username].password = new_password
            self.save_users()
            return True
        return False

    def load_feedback(self):
        with open("feedback.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                feedback_id, ratings = row
                self._feedback_data[feedback_id] = FeedbackData(feedback_id, ratings)

    def save_feedbacks(self):
        with open("feedback.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Feedback ID", "Ratings"])
            for feedback in self._feedback_data.values():
                writer.writerow([feedback.feedback_id, feedback.ratings])

    def add_feedback(self, feedback):
        if feedback.feedback_id not in self._feedback_data:
            self._feedback_data[feedback.feedback_id] = feedback
            self.save_feedbacks()
            return True
        return False

    def get_feedback(self, feedback_id):
        feedback = self._feedback_data.get(feedback_id)
        if feedback:
            return feedback.ratings
        return None

    def analyze_all_feedback_for_improvement(self):
        # Initialize variables to store counts
        good_feedback_count = 0
        better_feedback_count = 0
        bad_feedback_count = 0

        # Iterate over feedback data
        for feedback in self._feedback_data.values():
            ratings_dict = feedback.ratings
            if isinstance(ratings_dict, dict):
                for rating_value in ratings_dict.values():
                    if rating_value == "good":
                        good_feedback_count += 1
                    elif rating_value == "better":
                        better_feedback_count += 1
                    elif rating_value == "bad":
                        bad_feedback_count += 1

        total_feedback_count = len(self._feedback_data)

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
    def update_feedback(self, feedback_id, new_content):
        feedback = self._feedback_data.get(feedback_id)
        if feedback:
            feedback.ratings = new_content

            # Update questions in the Questionnaire class
            for key, value in new_content.items():
                if key in Questionnaire.questions:
                    index = Questionnaire.questions.index(key)
                    Questionnaire.questions[index] = new_content[key]

            self.save_feedbacks()
            return True
        return False

    def delete_feedback(self, feedback_id):
        if feedback_id in self._feedback_data:
            del self._feedback_data[feedback_id]
            self.save_feedbacks()
            return True
        return False

class FeedbackData(Feedback):
    def __init__(self, feedback_id, ratings):
        super().__init__(feedback_id, ratings)

def collect_project_feedback():
    feedback_id = input("Enter feedback ID: ")
    ratings = {}
    for q in Questionnaire.questions:
        rating = input(f"{q} \n Enter rating (good/bad/better): ")
        ratings[q] = rating
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

feedback_system = FeedbackSystem()
while True:
    login_option = int(input("Enter an option:\n1. Admin Access. \n2. Give feedback. \n3. Exit.\n"))

    if login_option == 1:
        while True:
            print("\n 1. Add or Remove User \n 2. Admin Login \n 3. Exit")
            op = int(input())
            if op == 1:
                admin_pwd = input("Enter the admin password: ")
                if admin_pwd == feedback_system._admin_password:
                    print("---Welcome---")
                    manage_users(feedback_system)
            elif op == 2:
                admin_username = input("Enter admin username?")
                pwd = input("Enter admin password?")
                if admin_username == 'admin' and pwd == feedback_system._admin_password:
                    while True:
                        print("Entering into the Feedback management system-----")
                        print(
                            "Enter an option: \n 1. Read Feedback\n 2. Update Feedback \n 3. Delete Feedback \n 4. Analyse Feedback \n 5. Exit")
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
                            f_id = input("Enter the Feedback_id to delete the feedback")
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
        if feedback_system.authenticate_user(username, passwrd):
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
