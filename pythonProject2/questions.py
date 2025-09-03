question = ["How much does the project is based on the real-life issues?",
            "Whether all the team members are interactive?",
            "How was the communication between the team members?",
            "How is the communication between you and guide?",
            "Whether the whole project had made you learn something?"]


class Feedback:
    def _init_(self):
        self.feedback_id = feedback_id
        self.ratings = ratings


class FeedbackCollectionSystem:
    def _init_(self):
        self.feedback_data = {}
        self.admin_password = "admin@123"  # Admin password

    def add_feedback(self, feedback, admin_password=None):
        if admin_password == self.admin_password:  # Check admin password
            self.feedback_data[feedback.feedback_id] = feedback
            return True
        else:
            return False

    def get_feedback(self, feedback_id):
        return self.feedback_data.get(feedback_id)

    def analyze_feedback_for_improvement(self):
        # Analyze feedback data to identify areas for improvement
        rating_score = 0

        for feedback_ in self.feedback_data.values():
            ratings__ = feedback_.ratings.values()
            for rating__ in ratings__:
                if rating__.lower() == "good":
                    rating_score += 2
                elif rating__.lower() == "bad":
                    rating_score += 0.5
                elif rating__.lower() == "better":
                    rating_score += 1

        print("Feedback analysis for improvement:")
        if 8 <= rating_score <= 10:
            print("Good")
        elif 5 <= rating_score <= 7.9:
            print("Better, But need to improve")
        elif 0 <= rating_score <= 4.9:
            print("Need to Improve a lot")

    def update_feedback(self, feedback_id, new_content):
        if feedback_id in self.feedback_data:
            self.feedback_data[feedback_id].content = new_content
            return True
        else:
            return False

    def delete_feedback(self, feedback_id):
        if feedback_id in self.feedback_data:
            del self.feedback_data[feedback_id]
            return True
        else:
            return False


# Collect feedback with rating
def collect_project_feedback():
    feedback_id = input("Enter feedback ID: ")
    ratings = {}
    for q in question:
        rating = input(f"{q} Enter rating (good/bad/better): ")
        ratings[q] = rating
    # print(feedback_id,ratings)
    return Feedback(feedback_id, ratings)


# Usage example
feedback_system = FeedbackCollectionSystem()

# Admin creates feedback
admin_password = input("Enter admin password: ")
feedback = collect_project_feedback()
if feedback_system.add_feedback(feedback, admin_password):
    print("Feedback created successfully")
    feedback_system.analyze_feedback_for_improvement()
else:
    print("Admin password incorrect")
