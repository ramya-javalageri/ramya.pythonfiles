# class Feedback:
#     def init(self, id, message):
#         self.id = id
#         self.message = message
#
# class FeedbackManager:
#     def init(self):
#         self.feedback_list = []
#
#     def create_feedback(self,message):
#         feedback = Feedback(message)
#         self.feedback_list.append(feedback)
#
#     def read_feedback(self):
#         for feedback in self.feedback_list:
#             print(f"ID: {feedback.id}, Message: {feedback.message}")
#
#     def update_feedback(self, id, new_message):
#         for feedback in self.feedback_list:
#             if feedback.id == id:
#                 feedback.message = new_message
#                 print("Feedback updated successfully.")
#                 return
#         print("Feedback not found.")
#
#     def delete_feedback(self, id):
#         for feedback in self.feedback_list:
#             if feedback.id == id:
#                 self.feedback_list.remove(feedback)
#                 print("Feedback deleted successfully.")
#                 return
#         print("Feedback not found.")# Function to handle user input and switch operations
# def main():
#     feedback_manager = FeedbackManager()
#     user_name = input('Enter your name:')
#
#     stakeholders_name = ['a', 'b', 'c', 'd']
#
#     if user_name in stakeholders_name:
#         print('hello')
#         user_id = input('Enter your id:')
#         if user_id == 'abc@123':
#             user_project = int(input('Enter project id:'))
#             project_id = [11, 22, 33, 44, 55, 66]
#             if user_project in project_id:
#                 print('access granted to give feedback')
#                 while True:
#                     print("\n1. give feedback")
#                     print("2. view  feedback")
#                     print("3. Exit")
#                     choice = input("Enter your choice: ")
#                     if choice == "1":
#                         message=input('enter your feedback:')
#
#                     elif choice=='2':
#
#
#                     else:
#                         print("Invalid choice. Please try again.")
#             else:
#                 print('Enter valid project_id')
#         else:
#             print('Enter correct id')
#     else:
#         print('Enter valid name')
#
#
#
#
# Feedback()
# main()
# class Feedback:
#     def __init__(self, name, feedback):
#         self.name = name
#         self.feedback = feedback
#
#     def analyze_feedback(self):
#         positive_words = ['good', 'great', 'excellent', 'impressive', 'innovative']
#         negative_words = ['bad', 'terrible', 'poor', 'disappointing', 'unimpressive','not good']
#         num_positive_words = 0
#         num_negative_words = 0
#
#         words = self.feedback.split()
#         for word in words:
#             if word.lower() in positive_words:
#                 num_positive_words += 1
#
#             elif word.lower() in negative_words:
#                 num_negative_words += 1
#
#
#
#         if num_positive_words > num_negative_words:
#             return 'Positive'
#         elif num_negative_words > num_positive_words:
#             return 'Negative'
#         else:
#             return 'Neutral'
#
# stakeholders = [
#     Feedback('John Doe', 'The project is great and I am very impressed with the results.'),
#     Feedback('abc', 'The project is not bad and I am not happy with the results.'),
#     Feedback('123', 'The project is unimpressive and do better.')
# ]
#
# for stakeholder in stakeholders:
#     analysis = stakeholder.analyze_feedback()
#     print(f'Feedback from {stakeholder.name}: {analysis}')

# def give_feedback_question():
#     print("Please provide feedback on the following questions:")
#     print("1. How satisfied are you with our product/service? (1-5)")
#     print("2. What do you like most about our product/service?")
#     print("3. What aspects do you think need improvement?")
#     print("4. Any additional comments or suggestions?")
#
# def get_feedback():
#     feedback = {}
#     feedback['satisfaction'] = int(input("Enter your satisfaction rating (1-5): "))
#     feedback['likes'] = input("What do you like most? ")
#     feedback['improvements'] = input("What needs improvement? ")
#     feedback['comments'] = input("Any additional comments? ")
#     return feedback
#
# def main():
#     give_feedback_question()
#     user_feedback = get_feedback()
#     print("\nThank you for your feedback!")
#     print("Here's a summary of your feedback:")
#     print("Satisfaction Rating:", user_feedback['satisfaction'])
#     print("Likes:", user_feedback['likes'])
#     print("Improvements:", user_feedback['improvements'])
#     print("Comments:", user_feedback['comments'])
#
# # if _name_ == "_main_":
# main()
class Feedback:
    def _init_(self,feedback_list):
        self.feedback_list = []

    def add_feedback(self,q1,q2,q3,q4):

        self.feedback_list=[]
        self.feedback_list.extend(q1)
        self.feedback_list.extend(q2)
        self.feedback_list.extend(q3)
        self.feedback_list.extend(q4)
        print(self.feedback_list)
        print("Feedback added successfully!")

    def view_feedback(self):

        if not self.feedback_list:
            print("No feedback available.")

        else:
            print("Feedback List:")
            for i, feedback in enumerate(self.feedback_list, 1):
                # print(i,'.',"['",feedback,"']")
                print(f"{i}. {feedback}")

    def update_feedback(self, index, updated_feedback):

        if index < 1 or index > len(self.feedback_list):
            print("Invalid index.")

        else:
            self.feedback_list[index - 1] = updated_feedback
            print(self.feedback_list)
            print("Feedback updated successfully!")

    def delete_feedback(self, index):

        if index < 1 or index > len(self.feedback_list):
            print("Invalid index.")

        else:
            del self.feedback_list[index - 1]
            print(self.feedback_list)
            print("Feedback deleted successfully!")


def main():

    feedback_manager = Feedback()

    user_name = input('Enter your name:')

    stakeholders_name = ['jack','virat','smirithi','shreyanka']

    if user_name in stakeholders_name:
        print('hello ',user_name)
        user_id = input('Enter your id:')

        if user_id == 'ectech@24':
            user_project = input('Enter project id:')

            if user_project =='bitm24':
                print('access granted to give feedback')

                while True:
                    print("\n1.Give Feedback")
                    print("2. View Feedback")
                    print("3. Update Feedback")
                    print("4. Delete Feedback")
                    print("5. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '1':

                        print('please provide feedback for the following questions? ')
                        #feedback=input("Enter your satisfaction rating (1-5):\n What do you like most \n What needs improvement? \n Any additional comments?\n" ).split(',')
                        q1=input("Enter your satisfaction rating (1-5):").split(' ')
                        q2=input("What do you like most ").split(' ')
                        q3=input("What needs improvement?").split(' ')
                        q4=input(" Any additional comments?").split(' ')
                        feedback_manager.add_feedback(q1,q2,q3,q4)

                    elif choice == '2':

                        feedback_manager.view_feedback()

                    elif choice == '3':

                        index = int(input("Enter index of feedback to update: "))
                        updated_feedback = input("Enter updated feedback: ")
                        feedback_manager.update_feedback(index, updated_feedback)

                    elif choice == '4':

                        index = int(input("Enter index of feedback to delete: "))
                        feedback_manager.delete_feedback(index)

                    elif choice == '5':

                        print("Exiting program.")
                        break

                    elif choice=='0':
                        main()

                else:
                    print("Invalid choice. Please try again.")

            else:
                print('Enter valid project_id')

        else:
            print('Enter correct id')

    else:
        print('Enter valid name')

main()

